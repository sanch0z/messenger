import socket
import threading

active_clients = []
users = {}
clients_lock = threading.Lock()
user_lock = threading.Lock()

def broadcast(text,sender_socket=None):
    with clients_lock:
        for client_socket in active_clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(text.encode('utf-8'))
                except Exception as e:
                    print(f"Не удалось отправить сообщение клиенту {e}")

def send_privat(sender_name,target_name,message):
    with clients_lock:
        target_socket = users
        if not target_socket:
            return False,f"Пользователь {target_name} не найден"
        try:
            target_socket.send(f"Личчное от {sender_name}:{message}".encode("utf-8"))
            return True
        except:
            return False, "Не удалось досставить сообщение"
    



def handle_clients( client_address,client_socket):
    print(f"Клиент {client_address} подключился")


    with clients_lock:
        username = None
        active_clients.append(client_socket)


    try:
        client_socket.send("Сначала авторизуйтесь (/login))")
        while True :
            data = client_socket.recv(1024)
            if not data:
                break
            text = data.decode("utf-8")
            if not text:
                continue
            if text.startswith('/login'):
                parts = text.split()
                if len(parts) ==2:
                    new_name = parts[1]
                    with clients_lock:
                        if new_name in users:
                            client_socket.send("Это имя уже занято".encode("utf-8"))
                        else:
                            username = new_name
                            users[username] = client_socket
                            client_socket.send(f"OK: Авторизация успешна".encode('utf-8'))
                            broadcast(f"{username} присоединился")
                            online = ', '.join(active_clients)
                            client_socket.send(f"Пользователи онлайн {online}")
                continue

            if not username:
                client_socket.send(f"Сначала авторизуйтесь")
                continue

            if text.startswith('/msg'):
                parts = text.split()
                target = parts[0]
                message = parts[2]
                sucsess,responce = send_privat(username,target,message)
                status = 'OK' if sucsess else 'ERR'
                client_socket.send(status.encode('utf-8'))
                continue
            if text.startswith('/logout'):
                break


                
            print(f"Количество потоков {threading.active_count()}")
            print(f"Сообщение от {client_address}: {text}")
            broadcast(text,sender_socket=client_socket)
            
    except ConnectionResetError:
        print("Произошла ошибка")
    finally:
        with user_lock:
            if username in users and users[username] == active_clients:
                del users[username]
        broadcast(f"Пользователь {username} покинул чат")
 

        client_socket.close()





def main():
    HOST = "127.0.0.1"
    PORT = 1234
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)



    server.bind((HOST,PORT))
    server.listen(5)
    print(f"Эхо сервер запущен на {HOST}:{PORT}")
    try:
        while True:
            client_socket,client_address = server.accept()
            thread = threading.Thread(target=handle_clients, args=(client_address,client_socket))
            thread.start()
    except  KeyboardInterrupt: 
        print("Получен сигнал остановки")
    finally:         
        server.close()

    




main()  
