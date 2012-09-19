import json
from suds.client import Client
from zope.interface import implements
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.Five import BrowserView
from xiru.ws.interfaces import IWS

def _execute(**kwargs):
    """ Run webservice call.
    """
    w = kwargs.get('w', 'http://192.168.1.26:8080/axis/Xiru.jws?wsdl')
    m = kwargs.get('m', 'echo')
    return getattr(Client(w).service, m)(**kwargs)

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
