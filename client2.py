import socket


def main():
    HOST = "127.0.0.1"
    PORT = 3000
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    


    print(f"Подлючение к серверу {HOST}:{PORT}")

    client_socket.connect((HOST,PORT))
    while True :
        messege = input("Введите сообщение:")
        if messege.lower() == "стоп":
            break
        

        
        
        client_socket.send(messege.encode("utf-8"))
        response = client_socket.recv(1024)
        print(f"Ответ сервера:{response.decode("utf-8")}")
    socket.close()
    client_socket.close()
    print("Клиент завершил работу")



main()  
