class Television(object):

    def __init__(self, channel=1, volume=0):
        """Инициализация атрибутов"""
        self.channel = channel
        self.volume = volume

    def change_channel(self):
        """изменение канала"""
        ch = int(input("Введите номер канала от 1 до 50: "))
        self.channel = ch
        if 1 <= ch < 50:
            print("Вы выбрали канал № ", self.channel)
        else:
            print("Выбран канал вне диапазона!")

    def volume_up(self):
        """Увеличение громкости"""
        print("Текущий уровень громкости -", self.volume)
        up = int(input("На сколько увеличить уровень громкости? "))
        self.volume = self.volume + up
        if up == 0:
            print("Звук отключен! ")
        elif 1 < up < 100:
            print("Установлена горомкость -", self.volume)
        else:
            print("Громкость вне диапазона!")

    def volume_down(self):
        """Уменьшение громкости"""
        print("Текущий уровень громкости -", self.volume)
        if self.volume == 0:
            print("Звук отключен! ")
        down = int(input("На сколько уменьшить уровень громкости? "))
        self.volume = self.volume - down
        if self.volume < 0:
            self.volume = 0
            print("Звук отключен! ")
        elif 1 < down < 100:
            print("Установлена горомкость -", self.volume)
        else:
            print("Громкость вне диапазона!")

    def current(self):
        """Просмотр текущих значений"""
        print("Текущий канал -", self.channel, "Текущая громкость -", self.volume)


def main():
    tv = Television()

    print(
        """
        \tМеню
        0 - Выключение
        1 - Изменение канала
        2 - Увеличение громкости
        3 - Уменьшение громкости
        4 - Текущие значения
        
        """
    )

    choice = None

    while choice != "0":

        choice = input("Выберите пункт меню: ")

        if choice == "0":
            print("Выключение приставки")
        elif choice == "1":
            tv.change_channel()
        elif choice == "2":
            tv.volume_up()
        elif choice == "3":
            tv.volume_down()
        elif choice == "4":
            tv.current()
        else:
            print("Такого пункта меню нет! ")


main()
