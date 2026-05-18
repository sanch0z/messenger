from core.repositories.UserRepository import UserRepository

class Login:
    def __init__(
            self,
            user_repo:UserRepository
                 ):
        self.user_repo = user_repo

    def execute(self,username:str,client_channel)  -> tuple[bool,str]:
        if not username:
            return False, "Введите имя пользователя"
        if self.user_repo.create(username,client_channel):
            return True , "Успешно авторизировались"
        else:
            return False , "Пользователь уже зарегистрирован"

