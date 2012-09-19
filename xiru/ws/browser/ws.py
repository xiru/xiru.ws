from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from suds.client import Client
import json

class WS(grok.View):
    """A view that enable Plone to call WSDL/SOAP webservices using suds.
    """

    grok.context(INavigationRoot)
    grok.name('webservices')
    grok.require('zope2.View')

    def render(self):
        """ Run the webservice and return json
        """
        r = self.request
        ret = self._execute(**r.form)
        return json.dumps(ret)

    def run(self, **kwargs):
        """ Run the webservice and return the computed value
        """
        return self._execute(**kwargs)

    def _execute(self, **kwargs):
        """ Generic method to execute the webservice.
        """

        # wsdl
        wsdl = kwargs.get('wsdl', None)
        if wsdl is None:
            wsdl = 'http://192.168.1.26:8080/axis/Xiru.jws?wsdl'

        # method
        method = kwargs.get('m', None)
        if method is None:
            method = 'echo'

        client = Client(wsdl)
        return getattr(client.service, method)(**kwargs)
