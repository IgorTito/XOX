# Сделать игру Морской бой, используя ООП
# Испольовать исключения
#
#
import random
from Exception import *


def start(question):
    answer = ""

    while answer not in ("да", "нет"):
        answer = input(question).lower()
    return answer


# Классы

class Sea:

    # Игровое поле
    def __init__(self):
        self.sea = """
         
        
        |_A0_|_A1_|_A2_|_A3_|_A4_|_A5_|_A6_|_A7_|_A8_|_A9_|
        |_B0_|_B1_|_B2_|_B3_|_B4_|_B5_|_B6_|_B7_|_B8_|_B9_|
        |_C0_|_C1_|_C2_|_C3_|_C4_|_C5_|_C6_|_C7_|_C8_|_C9_|
        |_D0_|_D1_|_D2_|_D3_|_D4_|_D5_|_D6_|_D7_|_D8_|_D9_|
        |_E0_|_E1_|_E2_|_E3_|_E4_|_E5_|_E6_|_E7_|_E8_|_E9_|
        |_F0_|_F1_|_F2_|_F3_|_F4_|_F5_|_F6_|_F7_|_F8_|_F9_|
        |_G0_|_G1_|_G2_|_G3_|_G4_|_G5_|_G6_|_G7_|_G8_|_G9_|
        |_H0_|_H1_|_H2_|_H3_|_H4_|_H5_|_H6_|_H7_|_H8_|_H9_|
        |_I0_|_I1_|_I2_|_I3_|_I4_|_I5_|_I6_|_I7_|_I8_|_I9_|
        |_J0_|_J1_|_J2_|_J3_|_J4_|_J5_|_J6_|_J7_|_J8_|_J9_|
        
        

        """

        self.stroka = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.kolonka = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.field = [self.stroka[i] + kol for i in range(10) for kol in self.kolonka]

    def zapolnenie(self, ship_list):
        available_fields = self.field.copy()
        occupied_fields = []
        for ship in ship_list:
            while ship.busy(available_fields):
                ship.place(self.field)
            occupied_fields += ship.field
            ship.rewrite(available_fields)
        return occupied_fields, ship_list

    # ЗАМЕНЯЕМ ЭЛЕМЕНТЫ доски через replace
    def update(self, hit_list, miss_list):
        update = self.sea
        for field in hit_list:
            update = update.replace("_" + field + "_", "■■■■")
        for field in miss_list:
            update = update.replace("_" + field + "_", "****")
        return update

    def solution(self, busy_field):
        solution = self.sea
        for field in self.field:
            if field in busy_field:
                solution = solution.replace("_" + field + "_", "■■■■")
            else:
                solution = solution.replace("_" + field + "_", "****")
        return solution


#
class Ship:

    def __init__(self, size):
        self.size = size
        self.field = []
        for i in range(size):
            self.field.append("")

    def place(self, igr_pole):
        self.playing_fields = igr_pole
        self.field[0] = random_sea(igr_pole)
        if self.size > 1:
            count = igr_pole.index(self.field[0])
            dist = random_place()
            if dist == "горизонтально":
                if str(self.size - 2) in self.field[0] or str(self.size - 3) in self.field[0] or str(self.size - 4) in \
                        self.field[0]:
                    direct = "вправо"
                elif str(11 - self.size) in self.field[0] or str(12 - self.size) in self.field[0] or str(
                        13 - self.size) in self.field[0]:
                    direct = "влево"
                else:
                    direct = random_left_right()
                for i in range(self.size - 1):
                    if direct == "вправо":
                        count += 1
                        self.field[i + 1] = igr_pole[count]
                    else:
                        count -= 1
                        self.field[i + 1] = igr_pole[count]
            else:
                if count < (self.size - 1) * 10:
                    direct = "вниз"
                elif count > (len(igr_pole) - 1) - (self.size - 1) * 10:
                    direct = "вверх"
                else:
                    direct = random_up_down()
                for i in range(self.size - 1):
                    if direct == "вниз":
                        count += 10
                        self.field[i + 1] = igr_pole[count]
                    else:
                        count -= 10
                        self.field[i + 1] = igr_pole[count]
        return self.field

    # Переписываем поля, занятые кораблями
    def rewrite(self, from_fields):
        fields_to_be_rewrite = []
        available_fields = Sea().field
        for i in range(self.size):
            ind = available_fields.index(self.field[i])
            if self.field[i] == "A0":
                fields_to_be_rewrite += [available_fields[ind], available_fields[ind + 1], available_fields[ind + 10],
                                         available_fields[ind + 11]]
            elif self.field[i] == "J9":
                fields_to_be_rewrite += [available_fields[ind], available_fields[ind - 1], available_fields[ind - 10],
                                         available_fields[ind - 11]]
            elif "A" in self.field[i]:
                fields_to_be_rewrite += [available_fields[ind], available_fields[ind - 1], available_fields[ind + 1],
                                         available_fields[ind + 9], available_fields[ind + 10],
                                         available_fields[ind + 11]]
            elif "J" in self.field[i]:
                fields_to_be_rewrite += [available_fields[ind], available_fields[ind - 1], available_fields[ind - 9],
                                         available_fields[ind - 10], available_fields[ind - 11],
                                         available_fields[ind + 1]]
            elif "0" in self.field[i]:
                fields_to_be_rewrite += [available_fields[ind], available_fields[ind - 9], available_fields[ind - 10],
                                         available_fields[ind + 1], available_fields[ind + 10],
                                         available_fields[ind + 11]]
            elif "9" in self.field[i]:
                fields_to_be_rewrite += [available_fields[ind], available_fields[ind - 1], available_fields[ind - 10],
                                         available_fields[ind - 11], available_fields[ind + 9],
                                         available_fields[ind + 10]]
            else:
                fields_to_be_rewrite += [available_fields[ind], available_fields[ind - 1], available_fields[ind - 9],
                                         available_fields[ind - 10], available_fields[ind - 11],
                                         available_fields[ind + 1], available_fields[ind + 9],
                                         available_fields[ind + 10], available_fields[ind + 11]]
        for field in fields_to_be_rewrite:
            if field in from_fields:
                from_fields.pop(from_fields.index(field))
        return from_fields

    # Проверка занятости поля
    def busy(self, available_fields):
        return any(field not in available_fields for field in self.field)


# Начало игры
place = ["горизонтально", "вертикально"]
polozenie_u_d = ["вверх", "вниз"]
polozenie_l_r = ["влево", "вправо"]
privet = "\nДобро пожаловать в игру 'Морской бой'\n"


def random_sea(choice):
    return random.choice(choice)


def random_place():
    return random.choice(place)


def random_up_down():
    return random.choice(polozenie_u_d)


def random_left_right():
    return random.choice(polozenie_l_r)


print(privet)
input("Нажмите Ввод, для начала игры")
igrok = input("\nВведите свое имя\n> ")

while igrok == "":
    igrok = input("\nПожалуйста, введите имя\n> ")
print("Очень приятно, ", igrok)
pravila = """
На игровом поле спрятаны 10 кораблей. В зависимости от выбранной сложности игры, у вас будет определенное 
количество попыток. Вам необходимо потопить все спрятанные корабли. Промах отмечается ****, попадание - ■■■■. Удачи!"""

pravila_know = start(f"\nНажмите 'Да', чтобы узнать о правилах игры. 'Нет', чтобы пропустить \n ").lower()

if pravila_know == "да":
    print(pravila)
elif pravila_know == "нет":
    print("Начинаем")


# Геймплей

def game(play_count=0, win=0, lose=0):
    playing_field = Sea()
    playing_fields = playing_field.field

    paluba4 = Ship(4)
    paluba3 = Ship(3)
    paluba3_1 = Ship(3)
    paluba2 = Ship(2)
    paluba2_1 = Ship(2)
    paluba2_2 = Ship(2)
    paluba1 = Ship(1)
    paluba1_1 = Ship(1)
    paluba1_2 = Ship(1)
    paluba1_3 = Ship(1)

    empty_sea = [paluba4, paluba3, paluba3_1, paluba2, paluba2_1, paluba2_2, paluba1, paluba1_1, paluba1_2, paluba1_3]

    # Заполнение поля

    busy_field, flot = playing_field.zapolnenie(empty_sea)

    pal4 = flot[0].field
    pal3 = flot[1].field
    pal3_1 = flot[2].field
    pal3_all = pal3 + pal3_1
    pal2 = flot[3].field
    pal2_1 = flot[4].field
    pal2_2 = flot[5].field
    pal2_all = pal2 + pal2_1 + pal2_2
    pal1 = flot[6].field + flot[7].field + flot[8].field + flot[9].field

    spisok_popadaniy = []
    spisok_promahov = []
    all_torpeds = 0
    all_hits = 0
    torpeds = 0

    sloznost = ["1", "2", "3"]
    selection = input(
        "\nВыберите уровень сложности\nЛегкий (1), Средний (2), Сложный (3) От уровня сложности будет зависить"
        " количество торпед\n> ")
    while selection not in sloznost:
        selection = input(
            "\nВыберите уровень сложности!!!\n> ")
    else:
        difficulty = int(selection)

    if difficulty == 1:
        torpeds = 60
        print("У вас будет", torpeds, 'торпед')
    if difficulty == 2:
        torpeds = 50
        print("У вас будет", torpeds, 'торпед')
    if difficulty == 3:
        torpeds = 40
        print("У вас будет", torpeds, 'торпед')

    input("\nНажмите Ввод, чтобы загрузить игровое поле")

    print(playing_field.sea)

    # Здесь сделать исключения\импорт из др файла

    for i in range(torpeds):
        target = input(">---->> ").upper()
        signal = ""
        message = ""

        try:
            if target in spisok_popadaniy or target in spisok_promahov:
                raise FieldCellException()
        except:
            print("Вы уже стреляли в эту клетку")
        try:
            if target not in playing_fields:
                raise FieldOutException()
        except:
            print("Такой координаты нет")
        if target in busy_field:
            signal = "Попал"
            spisok_popadaniy.append(target)
            all_hits += 1
        else:
            signal = "Промах"
            spisok_promahov.append(target)
        all_torpeds += 1

        print(f"\n~~~~~~ {signal.upper()} ~~~~~")

        if signal == "Попал":
            if target in pal1:
                print("\n~~~Однопалубный корабль затоплен ~~~")
                if all(field in spisok_popadaniy for field in pal1):
                    print("!!!!Все однопалубники уничтожены!!!!")
            elif target in pal2:
                if all(field in spisok_popadaniy for field in pal2):
                    print("~~~ Двухпалубный корабль затоплен ~~~")
                    if all(field in spisok_popadaniy for field in pal2_all):
                        print("!!!!Все двухпалубники уничтожены!!!!")
            elif target in pal2_1:
                if all(field in spisok_popadaniy for field in pal2_1):
                    print("~~~ Двухпалубный корабль затоплен ~~~")
                    if all(field in spisok_popadaniy for field in pal2_all):
                        print("!!!!Все трехпалубники уничтожены!!!!")
            elif target in pal2_2:
                if all(field in spisok_popadaniy for field in pal2_2):
                    print("~~~ Двухпалубный корабль затоплен ~~~")
                    if all(field in spisok_popadaniy for field in pal2_all):
                        print("!!!!Все двухпалубники уничтожены!!!!")
            elif target in pal3:
                if all(field in spisok_popadaniy for field in pal3):
                    print("~~~Трехпалубный корабль затоплен ~~~")
                    if all(field in spisok_popadaniy for field in pal3_all):
                        print("!!!!Все трехпалубники уничтожены!!!!")
            elif target in pal3_1:
                if all(field in spisok_popadaniy for field in pal3_1):
                    print("~~~ Трехпалубный корабль затоплен ~~~")

                    if all(field in spisok_popadaniy for field in pal3_all):
                        print("!!!!Все трехпалубники уничтожены!!!!")
            else:
                if all(field in spisok_popadaniy for field in pal4):
                    print("!!!!Четырехпалубный корабль уничтожен!!!!")

        else:
            print(message)
        print(playing_field.update(spisok_popadaniy, spisok_promahov))

        if all_hits == 0:
            if all_torpeds == 1:
                print("Вы выпустили " + str(all_torpeds) + " торпеду, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")

                print("Укажите следующую координату")
            elif all_torpeds == torpeds - 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            else:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                if all_torpeds == torpeds:
                    continue
                else:
                    print("Укажите следующую координату")
        elif all_hits == 1:
            if all_torpeds == 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            elif all_torpeds == torpeds - 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            else:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                if all_torpeds == torpeds:
                    continue
                else:
                    print("Укажите следующую координату")
        elif all_hits == 2:
            if all_torpeds == 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")

                print("Укажите следующую координату")
            elif all_torpeds == torpeds - 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            else:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                if all_torpeds == torpeds:
                    continue
                else:
                    print("Укажите следующую координату")
        elif all_hits == 19:
            if all_torpeds == 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            elif all_torpeds == torpeds - 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            else:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                if all_torpeds == torpeds:
                    continue
                else:
                    print("Укажите следующую координату")
        elif all_hits < 20:
            if all_torpeds == 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            elif all_torpeds == torpeds - 1:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                print("Укажите следующую координату")
            else:
                print("Вы выпустили " + str(all_torpeds) + " торпед, " + str(
                    torpeds - all_torpeds) + " торпед осталось.")
                if all_torpeds == torpeds:
                    continue
                else:
                    print("Укажите следующую координату")
        else:
            break

    if all_hits == 20:
        win += 1
        print("\n*Вы выиграли**** Все корабли противника уничтожены")
    else:
        lose += 1
        print("\n***Вы проиграли*** Вам не удалось уничтожить все корабли противника")
    play_count += 1
    print(f"\nИгр сыграно: {play_count}\Побед: {win}\nПоражений: {lose}")

    repeat = start("\nХотите сыграть еще раз? 'Да' или 'Нет' \n> ").lower()
    if repeat == "да":
        print(f"Ок, двайте попробуемеше раз, {igrok}. ")
        game(play_count, win, lose)
    else:
        print(f"Ок, {igrok}! Как-нибудь в другой раз)).")


game()
