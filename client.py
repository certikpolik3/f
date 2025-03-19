import socket
from emproto.transport import Transport

def start_client(host='localhost', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Připojeno k serveru na {host}:{port}")

    transport = Transport()
    transport.handshake(client_socket)
    print("Výměna klíčů dokončena.")

    while True:
        try:
            message = input("Zpráva: ")
            transport.send_message(client_socket, message)
            if message.lower() == 'exit':
                break
            response = transport.receive_message(client_socket)
            print(f"Server: {response}")
        except Exception as e:
            print(f"Chyba: {e}")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
