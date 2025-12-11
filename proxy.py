import socket
import threading

#Configuration 
LISTEN_PORT = 8888
BUFFER_SIZE = 4096

def handle_client(client_socket):

    """
    Handles a single connection from the browser.
    """
    try:
        # 1. Recieve the request from the browser.
        request = client_socket.recv(BUFFER_SIZE)

        if not request:
            return
        # Cyber twist: log the request to see what the browser is sending
        print(f"[*] Captured Request:\n{request.decode('utf-8',errors='ignore')}\n")

        # 2. Parse the first line of the request to get the host and port.
        first_line = request.split(b'\n')[0]
        url = first_line.split(b' ')[1]
# Finding the web server's address (stripping http://)
        http_pos = url.find(b'://')
        if http_pos == -1:
            temp =url
        else:
            temp = url[(http_pos +3):]

        port_pos = temp.find(b':')
# Default to port 80 (HTTP) if no port is specified
        webserver_pos = temp.find(b'/')
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1

        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]    

        else:
            port = int((temp[(port_pos +1):])[:webserver_pos - port_pos -1])
            webserver = temp[:port_pos]

        # 3. Create a socket to connect to the real web server.
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.connect((webserver, port))

        # 4. Forward the request to the web server.
        request = request.replace(b'gzip', b'    ') 
        request = request.replace(b'deflate', b'       ')
        print(f"[*] Request sent to server (Compression stripped?):\n{request.decode('utf-8', errors='ignore')}\n")
        proxy_socket.send(request)

        # 5. Receive the response from the web server and forward it to the browser.
        # 5. Receive the response from the web server and forward it to the browser.
        while True:
            response = proxy_socket.recv(BUFFER_SIZE)

            if len(response) > 0:
                
                # DEBUG CHECK: Did we catch the target?
                if b'Example' in response:
                    print(f"\n[!!!] TARGET CONFIRMED: Found 'Example' in response! Injecting hack...\n")
                    
                    # IMPORTANT: 'Example' is 7 chars. 'HACKED!' is 7 chars.
                    # Keeping the length identical prevents the browser from crashing.
                    modified_response = response.replace(b'Example', b'HACKED!')
                    
                    client_socket.send(modified_response)
                
                else:
                    # No target found in this chunk, just forward it
                    client_socket.send(response)
                    
            else:
                break

        proxy_socket.close()
        client_socket.close()

    except Exception as e:
        pass

def start_proxy():
    """
    Starts the proxy server to listen for incoming connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', LISTEN_PORT))
    server.listen(5)

    print(f"[*] Listening on port 127.0.0.1 : {LISTEN_PORT}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_proxy()



