"""
Telegram Theme Converter Server
Local HTTP server with CORS proxy and Telegram theme scraper.
Uses only Python standard library (no pip dependencies required).
"""

import http.server
import socketserver
import urllib.request
import urllib.parse
import json
import re
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class ThemeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == '/api/theme-info':
            self.handle_theme_info(params)
        elif path == '/api/fetch':
            self.handle_proxy_fetch(params)
        else:
            super().do_GET()

    def handle_theme_info(self, params):
        target = params.get('url', [''])[0].strip() or params.get('slug', [''])[0].strip()
        if not target:
            self.send_json_error("Missing 'url' or 'slug' parameter", 400)
            return

        # Extract slug if a URL was provided
        slug = target
        m = re.search(r'addtheme[/:=]([a-zA-Z0-9_-]+)', target)
        if m:
            slug = m.group(1)
        elif target.startswith('http') and not 'addtheme' in target:
            # Not an addtheme link - pass through to fetch directly
            self.handle_direct_url_info(target)
            return

        # Clean slug
        slug = re.sub(r'[^a-zA-Z0-9_-]', '', slug)
        if not slug:
            self.send_json_error("Invalid theme slug or URL", 400)
            return

        tme_url = f"https://t.me/addtheme/{slug}"
        try:
            req = urllib.request.Request(
                tme_url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')

            # Extract title
            title_m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
            title = title_m.group(1) if title_m else f"Theme {slug}"
            title = re.sub(r'^Telegram Theme:\s*', '', title).strip()

            # Extract background / wallpaper colors
            colors_m = re.search(r'data-colors="([0-9a-fA-F,]+)"', html)
            colors = colors_m.group(1).split(',') if colors_m else []

            # Check if dark or light
            is_dark = 'theme_dark' in html or any(k in html.lower() for k in ['night', 'dark'])

            # Description
            desc_m = re.search(r'class="tgme_page_description">([^<]*<strong>.*?</strong>[^<]*)', html, re.DOTALL)
            desc = re.sub(r'<[^>]+>', '', desc_m.group(1)).strip() if desc_m else ""

            response_data = {
                "success": True,
                "type": "telegram_slug",
                "slug": slug,
                "title": title,
                "colors": colors,
                "isDark": is_dark,
                "description": desc,
                "url": tme_url
            }
            self.send_json(response_data)

        except Exception as e:
            self.send_json_error(f"Failed to fetch Telegram theme '{slug}': {str(e)}", 500)

    def handle_direct_url_info(self, target_url):
        try:
            req = urllib.request.Request(
                target_url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                ct = resp.headers.get('Content-Type', '')

            self.send_json({
                "success": True,
                "type": "direct_file",
                "url": target_url,
                "size": len(data),
                "contentType": ct
            })
        except Exception as e:
            self.send_json_error(f"Failed to fetch URL: {str(e)}", 500)

    def handle_proxy_fetch(self, params):
        target_url = params.get('url', [''])[0].strip()
        if not target_url:
            self.send_json_error("Missing 'url' parameter", 400)
            return

        try:
            req = urllib.request.Request(
                target_url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                content_type = resp.headers.get('Content-Type', 'application/octet-stream')

            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(data)

        except Exception as e:
            self.send_json_error(f"Proxy fetch error: {str(e)}", 500)

    def send_json(self, data, status=200):
        body = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def send_json_error(self, message, status=400):
        self.send_json({"success": False, "error": message}, status)

def run():
    with socketserver.TCPServer(("", PORT), ThemeHandler) as httpd:
        print(f"Telegram Theme Converter running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == '__main__':
    run()
