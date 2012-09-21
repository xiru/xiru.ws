import hashlib
import json
from xiru.ws import memcache
from suds.client import Client
from zope.interface import implements
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.Five import BrowserView
from xiru.ws.interfaces import IWS
from xiru.ws.config import DEFAULT_TIMEOUT, DEFAULT_CACHE

def _execute(**kwargs):
    """ Run webservice call.
    """
    
    # calcule the cache key
    m = hashlib.md5()
    m.update(repr(kwargs))
    chave = m.hexdigest()

    # create the memcached connection
    mc = memcache.Client(['127.0.0.1:11211'])  

    valor = mc.get(chave)
    if valor is None:
        wsdl = kwargs.get('wsdl', 
                   'http://192.168.1.26:8080/axis/Xiru.jws?wsdl')
        meth = kwargs.get('meth', 'echo')
        timeout = kwargs.get('timeout', DEFAULT_TIMEOUT)
        cache = kwargs.get('cache', DEFAULT_CACHE)
        client = Client(wsdl, timeout = timeout)
        valor = getattr(client.service, meth)(**kwargs)
        mc.set(chave, valor, cache)
    return valor

class WSJson(grok.View):
    """ A view that calls a webservice and return json.
    """

    grok.context(INavigationRoot)
    grok.name('wsjson')
    grok.require('zope2.View')

    def render(self):
        """ Run the webservice and return json.
        """
        r = self.request
        ret = _execute(**r.form)
        return json.dumps(ret)

class WSView(BrowserView):
    """ A view that calls a webservice and return the suds output.
    """

    implements(IWS)

    def run(self, **kwargs):
        """ Run the webservice and return the suds output.
        """
        return _execute(**kwargs)
