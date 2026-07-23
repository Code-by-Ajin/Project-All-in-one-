import http.server
import socketserver
import socket
import os

PORT = 5500

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable, just forces the socket to bind to the local IP
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Change directory to the root of the project so relative paths work
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
os.chdir(project_root)

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        ip = get_local_ip()
        print("="*70)
        print("🚀 OMNIUTILS SECURE LOCAL SERVER IS RUNNING!")
        print("="*70)
        print("To test the QR codes with your phone over Wi-Fi, open this EXACT URL on your PC browser:")
        print(f"\n👉 http://{ip}:{PORT}/src/tools/qr_generator/qr_generator.html\n")
        print("="*70)
        print("Keep this terminal window open. Press Ctrl+C to stop the server.")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 10048:
        print(f"Port {PORT} is already in use. Please close other local servers (like Live Server) and try again.")
    else:
        print(f"Error starting server: {e}")
