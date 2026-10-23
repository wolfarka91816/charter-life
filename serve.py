#!/usr/bin/env python3
"""Runs Charter Life on this computer. Double-click the Play launcher (or run: python3 serve.py).
Downloads React and Three.js into vendor/ the first time (needs internet once), then works offline."""
import http.server, os, socketserver, sys, threading, urllib.request, webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
LIBS = [('vendor/three.min.js', 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'), ('vendor/react.production.min.js', 'https://cdnjs.cloudflare.com/ajax/libs/react/18.3.1/umd/react.production.min.js'), ('vendor/react-dom.production.min.js', 'https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.3.1/umd/react-dom.production.min.js')]

def get_libs():
    os.makedirs(os.path.join(HERE, "vendor"), exist_ok=True)
    for local, url in LIBS:
        path = os.path.join(HERE, local)
        if os.path.exists(path) and os.path.getsize(path) > 1000: continue
        try:
            print("Downloading", url)
            with urllib.request.urlopen(url, timeout=30) as r, open(path, "wb") as f: f.write(r.read())
        except Exception as e:
            print("  could not download (%s). The game will try again from the internet when it starts." % e)
            if os.path.exists(path): os.remove(path)

class Quiet(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".webmanifest": "application/manifest+json", ".js": "text/javascript"}
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

def main():
    os.chdir(HERE)
    get_libs()
    socketserver.TCPServer.allow_reuse_address = True
    for port in range(8137, 8160):
        try: srv = socketserver.ThreadingTCPServer(("127.0.0.1", port), Quiet); break
        except OSError: continue
    else:
        print("No free port found."); sys.exit(1)
    url = "http://localhost:%d/index.html" % port
    print("\nCharter Life Demo is running at", url, "\nLeave this window open while you play. Close it to stop.")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try: srv.serve_forever()
    except KeyboardInterrupt: pass

if __name__ == "__main__":
    main()
