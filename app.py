from spin_sdk import http
from spin_sdk.http import Request, Response, send


class IncomingHandler(http.IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        try:
            res = send(Request("GET", "https://example.com", {}, None))
            return Response(
                res.status,
                {"content-type": "text/plain"},
                f"example.com returned {res.status}\n".encode(),
            )
        except Exception as e:
            return Response(500, {"content-type": "text/plain"}, f"outbound failed: {e}\n".encode())
