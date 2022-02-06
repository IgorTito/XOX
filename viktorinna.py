import sys

text_records = open("records.txt", "w")
text_records.write("Ivan : 100" "|" "Igor : 55" "|" "Lena : 75")
text_records.close()

def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Невозможно открыьт файл", file_name, "работа программы будет завершена", e)
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла"""
    new_stroka = the_file.readline()

    return new_stroka


def next_block(the_file):
    """Возвращает очередной блок данных из файла"""

    category = next_line(the_file)

    question = next_line(the_file)
    try:
        global nom_score
        nom_score = int(next_line(the_file))
    except ValueError:
        print("Это был последний вопрос")
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)

    if correct:
        correct = correct[0]

    return category, question, answers, correct, nom_score


def welcome(title):
    """Приветствует игрока и сообщает тему игры"""
    print("Добро пожаловать в 'Викторину'")
    print(title)


def main():
    viktorina_file = open_file("viktorina.txt", "r")
    text_records = open("records.txt", "r")
    line = text_records.readline()
    print(line)
    title = next_line(viktorina_file)

    welcome(title)
    score = 0
    sum = 0

    category, question, answers, correct, nom_score = next_block(viktorina_file)

    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i + 1, "-", answers[i])

        answer = input("Ваш ответ: ")

        if answer == correct:
            print("Да!")
            score += 1
            sum = nom_score + sum


        else:
            print("нет!")

        print("Счет =", score)
        print("Номинальный счет ", "-----", sum)


        category, question, answers, correct, nom_score = next_block(viktorina_file)

    viktorina_file.close()


main()


