import socket
import threading

active_clients = []
clients_lock = threading.Lock()


def broadcast(messenge,sender_socket=None):
    with clients_lock:
        for client_socket in active_clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(messenge.endcode('utf-8'))
                except Exception as e:
                    print(f"Не удалось отправить сообщение клиенту {e}")


def handle_clients( client_address,client_socket):
    print(f"Клиент {client_address} подключился")


    with clients_lock:
        active_clients.append(client_socket)


    try:
        while True :
            data = client_socket.recv(1024)
            if not data:
                break
            messenge = data.decode("utf-8")
            print(f"Количество потоков {threading.active_count()}")
            print(f"Сообщение от {client_address}: {messenge}")
            broadcast(messenge,sender_socket=client_socket)
            client_socket.send(data)
    except ConnectionResetError:
        print("Произошла ошибка")
    finally:
        with clients_lock:
            if client_socket in active_clients:
                active_clients.remove(client_socket)
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
