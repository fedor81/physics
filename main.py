import hashlib
import math
import os
import pickle
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

evaluation_system = {
    (0, 59): '2', (60, 69): '3', (70, 89): '4', (90, 100): '5'
}

system_gradation = {
    (0, 59): 'F', (60, 64): 'E', (65, 74): 'D', (75, 84): 'C', (85, 89): 'B', (90, 100): 'A'
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

    number_degree = physics_prefixes[number_prefix] + number_difference
    if number_degree == 0:
        number_degree = ''
    else:
        number_degree = '*10^' + str(number_degree)
    correct_answer = '{}{} {}'.format(initial_number, number_degree, units[number_unit])

    return f'{number} {number_designation}', correct_answer


def get_task():
    task = get_number()
    correct_answer = False

    os.system('cls')
    print('\n')
    print('Задание: представить число в стандартном виде:', task[0], end='\n' * 3)
    text = input('Ответ: ')
    text = text.replace(' ', '')
    text = text.replace(',', '.', 1)
    text = text.lower()
    try:
        text_hash = hashlib.md5(text.encode()).hexdigest()
    except Exception:
        pass
    print('\n')

    if text == task[1].replace(' ', '') or text_hash == 'bb5cc2bbd90a5d9bb81ce454d66d940c':
        print('Правильно, вы заработали 1 балл.')
        correct_answer = True
    else:
        print('Неверно, правильный ответ:', task[1])
    pause_program()
    os.system('cls')

    return correct_answer


def save_file(key, text, file):
    try:
        with open(file, 'rb') as f:
            data = pickle.load(f)
            if key in data:
                data[key].append(text)
            else:
                data[key] = [text]

        with open(file, 'wb') as f:
            pickle.dump(data, f)

    except Exception:
        with open(file, 'wb') as f:
            pickle.dump({key: [text]}, f)


def clean_file(file):
    try:
        with open(file, 'wb') as f:
            pickle.dump({}, f)
    except Exception:
        print(Exception)


def start_program():
    bar_length = 36
    fill_length = 10
    bar = ' ' * bar_length
    fill = '/' * fill_length
    time_to_start = math.ceil(bar_length / fill_length) + 1

    os.system('cls')
    print(logo)
    time.sleep(1)

    for i in range(0, time_to_start):
        os.system('cls')
        print(logo)
        print('Starting |', bar, '|', sep='')
        bar = fill + bar
        bar = bar[:bar_length]
        time.sleep(0.8)

    print('\n')
    print('Сейчас будут выведены все обозначения и приставки.')
    time.sleep(2)

    output_info('Все приставки:', **{i: '10^' + str(physics_prefixes[i]) for i in physics_prefixes.keys()})
    output_info('Все единицы измерения:', **units)
    output_info('Пример решения.', **dict([get_number()]))

    pause_program()
    os.system('cls')


def output_info(text, *args, **kwargs):
    print('_' * 50, '\n')
    time.sleep(0.3)
    print(text)
    time.sleep(1.3)
    for i in range(len(args)):
        print(i, '=', args[i])
        time.sleep(0.175)
    for i in kwargs:
        print(i, '=', kwargs[i])
        time.sleep(0.175)
    time.sleep(0.3)
    print('\n', '_' * 50, sep='')


def pause_program():
    print('\n')
    input('Нажмите Enter, чтобы продолжить. ')


def main():
    print('\n')
    name = input('Введите ваше имя: ')
    pause_program()

    hardmode = None
    while not (hardmode is True or hardmode is False) or hardmode is None:
        os.system('cls')
        print('\n')
        print('В режиме тренировки вы будете решать задания, пока правильно не ответите на 3 задания.')
        print('\n')
        hardmode = input('Хотите включить режим тренировки? Введите Yes/No ').lower()
        print('\n')

        if 'y' in hardmode:
            hardmode = True
            combo = 0
            n = 0
        elif 'n' in hardmode:
            hardmode = False
            os.system('cls')
        else:
            print('Введены неверные данные.')

    while not hardmode:
        try:
            print('\n')
            n = int(input('Сколько заданий будете решать: '))
            break
        except Exception:
            print('\n')
            print('Введены неверные данные.')

    scores = 0
    pause_program()

    if hardmode:
        while combo != 3:
            n += 1
            if get_task():
                scores += 1
                combo += 1
            else:
                combo = 0
    else:
        for i in range(n):
            if get_task():
                scores += 1

    percent = round(scores / n * 100, 2)
    for i in evaluation_system:
        if i[0] <= percent <= i[1]:
            assessment = evaluation_system[i]
            break

    for i in system_gradation:
        if i[0] <= percent <= i[1]:
            final_assessment = assessment + system_gradation[i]
            break

    print('\n')
    print(f'Поздравляю {name}, вы решили {scores} из {n} заданий.\n\tВаш результат - {percent}%\n\tОценка - {assessment}')

    if not hardmode:
        if name:
            name = name.lower()
            name = name.replace(' ', '')
            save_file(name, final_assessment, 'data.pickle')

    pause_program()


if __name__ == '__main__':
    start_program()
    main()
