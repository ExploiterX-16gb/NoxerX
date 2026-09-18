#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser
ROOT=Path(__file__).resolve().parent
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw): super().__init__(*a,directory=str(ROOT),**kw)
if __name__=="__main__":
    url="http://127.0.0.1:8000/"
    print("NoxerX static site:",url)
    try:webbrowser.open(url)
    except Exception:pass
    s=ThreadingHTTPServer(("127.0.0.1",8000),Handler)
    try:s.serve_forever()
    except KeyboardInterrupt:s.server_close()
