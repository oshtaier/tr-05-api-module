from .api.enrich import EnrichAPI
from .api.inspect import InspectAPI
from .api.observe import ObserveAPI
from .request.authorized import AuthorizedRequest
from .request.logged import LoggedRequest
from .request.standard import StandardRequest
from .request.validated import ValidatedRequest
from .request.relative import RelativeRequest


class ThreatResponse(object):
    def __init__(self, client_id, client_password, **options):
        request = StandardRequest()
        request = ValidatedRequest(request)

        if options.get('logger'):
            request = LoggedRequest(request, options['logger'])

        request = AuthorizedRequest(request, client_id, client_password)
        request = RelativeRequest(request, 'https://visibility.amp.cisco.com/')

        self._inspect = InspectAPI(request)
        self._enrich = EnrichAPI(request)
        self._observe = ObserveAPI(request)

    @property
    def inspect(self):
        return self._inspect

    @property
    def enrich(self):
        return self._enrich

    @property
    def observe(self):
        return self._observe
