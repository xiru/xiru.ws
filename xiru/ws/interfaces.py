from zope import interface

class IWS(interface.Interface):
    """A webservices runner.
    """

    def run(**kwargs):
        """ Run the webservice and return the suds output.
        """
