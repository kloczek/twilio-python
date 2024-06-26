from twilio.base.exceptions import TwilioRestException
from twilio.http import HttpClient
from twilio.http.request import Request
import platform
from twilio import __version__


class Hologram:
    def __init__(self, request, response):
        self.request = request
        self.response = response


class Holodeck(HttpClient):
    def __init__(self):
        self._holograms = []
        self._requests = []

    def mock(self, response, request=None):
        request = request or Request()
        self._holograms.append(Hologram(request, response))

    @property
    def requests(self):
        return self._requests

    def add_standard_headers(self, request):
        standard_headers = {
            "User-Agent": "twilio-python/{} ({} {}) Python/{}".format(
                __version__,
                platform.system(),
                platform.machine(),
                platform.python_version(),
            ),
            "X-Twilio-Client": f"python-{__version__}",
            "Accept": "application/json",
            "Accept-Charset": "utf-8",
        }

        if request.method == "POST" and "Content-Type" not in standard_headers:
            standard_headers["Content-Type"] = "application/x-www-form-urlencoded"

        standard_headers.update(request.headers)
        request.headers = standard_headers
        return request

    def assert_has_request(self, request):
        for req in self.requests:
            if req == request or req == self.add_standard_headers(request):
                return

        message = "\nHolodeck never received a request matching: \n + {}\n".format(
            request
        )
        if self._requests:
            message += "Requests received:\n"
            message += "\n".join(f" * {r}" for r in self.requests)
        else:
            message += "No Requests received"

        raise AssertionError(message)

    def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        auth=None,
        timeout=None,
        allow_redirects=False,
    ):
        request = Request(method, url, auth, params, data, headers)

        self._requests.append(request)

        for hologram in self._holograms:
            if hologram.request == request:
                return hologram.response

        message = f"\nHolodeck has no hologram for: {request}\n"
        if self._holograms:
            message += "Holograms loaded:\n"
            message += "\n".join(f" - {h.request}" for h in self._holograms)
        else:
            message += "No Holograms loaded"

        raise TwilioRestException(404, url, message, method=method)
