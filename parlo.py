import socket
import sys

HOST = '127.0.0.1'
PORT = 6364
TIMEOUT = 2
BUFFER_SIZE = 1024

def main ():
    if len(sys.argv) < 2:
        print("ciao")
        sys.exit (1)

    messaggio = sys.argv [1]

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout (TIMEOUT)
            s.connect((HOST, PORT))
            s.sendall(messaggio.encode())
            riposta = s.recv(BUFFER_SIZE) 
    except socket.timeout:
        print("errore: timeout connesione")
    except ConnectionRefusedError:
        print ("errore: server non disponibile")
    except Exception as e:
        print (f"errore: {e}")

if __name__ == "__main__":
    main()
