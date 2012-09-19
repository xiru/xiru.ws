from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

class WS(grok.View):
    """A view that enable Plone to call WSDL/SOAP webservices using suds.
    """

    grok.context(INavigationRoot)
    grok.name('webservices')
    grok.require('zope2.View')

    def render(self):
        """ Run the webservice and return json
        """
        return "OK"
