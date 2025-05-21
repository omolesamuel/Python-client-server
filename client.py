import socket
import threading
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if msg:
                print("\n" + msg)
            else:
                break
        except:
            print("\n[ERROR] Disconnected from server.")
            sock.close()
            break

def send_messages(sock):
    while True:
        try:
            msg = input()
            sock.send(msg.encode('utf-8'))
        except:
            print("[ERROR] Unable to send message.")
            sock.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print(f"[ERROR] Unable to connect to server at {HOST}:{PORT}")
        sys.exit()

    print("[CONNECTED] Connected to the server.")
    
    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    main()
