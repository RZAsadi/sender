import socket
import os

def send_file(host, port, file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        return

    filename = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    # Send the filename
    client_socket.send(filename.encode())

    # Send the file
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            client_socket.send(chunk)
    print(f"File sent successfully: {file_path} ({file_size} bytes)")

    client_socket.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Send a file over the network.")
    parser.add_argument('host', type=str, help="Receiver's IP address or hostname")
    parser.add_argument('port', type=int, help="Receiver's port")
    parser.add_argument('file', type=str, help="Path to the file to send")
    args = parser.parse_args()

    send_file(args.host, args.port, args.file)
