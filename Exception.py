#Создать исключения, вызвать их в осн коде
# Искл за рамки поля и т.д.
class BoardException(Exception):
    pass


class FieldOutException(BoardException):
    def __str__(self):
        return "Такой координаты нет!!"
class DifficultException(BoardException):
    def __str__(self):
        return "Выберите уровень сложности из представленных"

class FieldCellException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass