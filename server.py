import socket
from emproto.transport import Transport

def start_server(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server naslouchá na {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Připojen klient z adresy: {addr}")

    transport = Transport()
    transport.handshake(conn)
    print("Výměna klíčů dokončena.")

    while True:
        try:
            message = transport.receive_message(conn)
            print(f"Klient: {message}")
            if message.lower() == 'exit':
                break
            response = input("Odpověď: ")
            transport.send_message(conn, response)
        except Exception as e:
            print(f"Chyba: {e}")
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
