import os
import random
import time

logo = """
______________________________________________
	    ____  ______       _
	   / __ \ \     \ /\  / \\
	  / /  \_\\\ [ ] //  \/ / \\
	 / /   __ / ___// /\  // /
	 \ \__/ // /    \ \ \// /
	  \____//_/      \ \ / /
______________________________________________
    
"""

physics_prefixes = {
    'деци': -1, 'санти': -2, 'милли': -3, 'микро': -6, 'нано': -9, 'пико': -12, 'фемто': -15, 'атто': -18, 'дека': 1,
    'гекто': 2, 'кило': 3, 'мега': 6, 'гига': 9, 'тера': 12, 'пета': 15, 'экса': 18
}

units = {
    'метр': 'м', 'секунда': 'с', 'герц': 'Гц', 'грамм': 'г', 'ньютон': 'Н', 'паскаль': 'Па', 'джоуль': 'Дж',
    'ватт': 'Вт', 'кельвин': 'К', 'моль': 'моль', 'ампер': 'А', 'кулон': 'Кл', 'вольт': 'В', 'фарад': 'Ф', 'ом': 'Ом',
    'тесла': 'Тл', 'зиверт': 'Зв'
}


def get_number():
    number_prefix = random.choice(list(physics_prefixes.keys()))
    number_unit = random.choice((list(units.keys())))
    number_designation = number_prefix + number_unit

    number_odds = (-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6)
    number_difference = random.choice(number_odds)
    if not (number_prefix in ('тера', 'пета', 'экса') or number_difference > 0) or not (
            number_prefix in ('пико', 'фемто', 'атто') or number_difference < -0):
        number_difference = -number_difference

    initial_number = 0
    while initial_number <= 1 or initial_number == 10:
        initial_number = round(random.random() * 10, random.choice((1, 2, 3, 4, 5)))
    number = initial_number * (10 ** number_difference)

    if initial_number == int(initial_number):
        initial_number = int(initial_number)

    if int(number) == number:
        number = int(number)

    if 'e' in str(number) or len(str(number)) > 10:
        return get_number()

    number_degree = physics_prefixes[number_prefix]+number_difference
    if number_degree == 0:
        number_degree = ''
    else:
        number_degree = '*10^' + str(number_degree)
    correct_answer = '{}{} {}'.format(initial_number, number_degree, units[number_unit])

    return number, number_designation, correct_answer


def get_task():
    task = get_number()
    correct_answer = False

    os.system('cls')
    print('\n')
    print('Задание: представить число в стандартном виде:', task[0], task[1], end='\n'*3)
    text = input('Ответ: ')
    text = text.replace(' ', '')
    text = text.replace(',', '.', 1)
    text = text.lower()
    print('\n')

    if text == task[2].replace(' ', '') or text in ('зимаблизко', 'winteriscoming'):
        print('Правильно, вы заработали 1 балл.')
        correct_answer = True
    else:
        print('Неверно, правильный ответ:', task[2])
    print('\n')
    pause_program()
    os.system('cls')

    return correct_answer


def start_program():
    print(logo)
    time.sleep(3)

    print('Сейчас будут выведены все обозначения и приставки.')
    time.sleep(2)

    output_info('Все приставки:', **{i: '10^' + str(physics_prefixes[i]) for i in physics_prefixes.keys()})
    output_info('Все единицы измерения:', **units)

    pause_program()
    os.system('cls')


def output_info(text, *args, **kwargs):
    print(text)
    time.sleep(1.5)
    for i in range(len(args)):
        print(i, '=', args[i])
        time.sleep(0.175)
    for i in kwargs:
        print(i, '=', kwargs[i])
        time.sleep(0.175)
    time.sleep(0.3)
    print('_' * 50)
    time.sleep(0.5)


def pause_program():
    input('Нажмите Enter, чтобы продолжить. ')


def main():
    print('\n')
    name = input('Введите ваше имя: ')
    while True:
        try:
            n = int(input('Введите количество заданий: '))
            break
        except:
            print('Введены неверные данные. Пожалуйста вводите цифры.')
    scores = 0
    print('\n')
    pause_program()

    for i in range(n):
        if get_task():
            scores += 1

    print('\n')
    print(f'Поздравляю {name}, вы решили {scores} из {n} заданий, ваш результат {scores/n*100}%')
    print('\n')
    pause_program()


if __name__ == '__main__':
    start_program()
    main()
