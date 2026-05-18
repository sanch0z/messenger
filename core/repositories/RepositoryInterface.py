from abc import abstractclassmethod


class RepositoryInterface:
    @classmethod
    def create(self):
        pass

    @classmethod
    def read(self):
        pass

    @classmethod
    def update(self):
        pass

    @classmethod
    def delete(self):
        pass