import socket


def main():
    HOST = "127.0.0.1"
    PORT = 3000
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)



    server.bind((HOST,PORT))
    server.listen(1)
    print(f"Эхо сервер запущен на {HOST}:{PORT}")

    client_socket,client_address = server.accept()
    print(f"Подключился клиент {client_address}")
    while True :
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Получено:{data.decode("utf-8")}")
        client_socket.send(data)
    socket.close()
    client_socket.close()
    print("Сервер остановлен")



main()  
