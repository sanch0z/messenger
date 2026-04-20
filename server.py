import socket
import threading



def handle_clients( client_address,client_socket):
    print(f"Клиент {client_address} подключился")
    try:
    
        while True :
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Получено:{data.decode("utf-8")}")
            client_socket.send(data)
    except ConnectionResetError:
        print("Произошла ошибка")
    finally:
        client_socket.close()




def main():
    HOST = "127.0.0.1"
    PORT = 1234
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)



    server.bind((HOST,PORT))
    server.listen(1)
    print(f"Эхо сервер запущен на {HOST}:{PORT}")
    try:
        while True:
            client_socket,client_address = server.accept()
            thread = threading.Thread(target=handle_clients, args=(client_address,client_socket))
            thread.start()
    except  KeyboardInterrupt: 
        print("Получен сигнал остановки")
    finally:         
        socket.close()

    




main()  
