import socket

HOST = '127.0.0.1'
PORT = 6364
BUFFER_SIZE = 1024

server = socket.socket()
server.bind((HOST, PORT))
server.listen (1)

print ("in ascolto su {HOST}:{PORT}")

for _ in range(6):
    conn, addr = server.accept()
    print("connesso")

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break

        richiesta = data.decode()

        if richiesta == "SHUTDOWN":
            break

        risposta = "ricevuto il messaggio {richiesta}"
        conn.sendall(risposta.encode())

    conn.close()

server.close()   
