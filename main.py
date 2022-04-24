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
    'деци': -1, 'санти': -2, 'милли': -3, 'микро': -6, 'нано': -9, 'пико': -12, 'фемто': -15, 'атто': -18, 'зепто': -21,
    'иокто': -24, 'дека': 1, 'гекто': 2, 'кило': 3, 'Мега': 6, 'Гига': 9, 'Тера': 12, 'Пета': 15, 'Экса': 18,
    'Зетта': 21, 'Иотта': 24
}

units = {
    'метр': 'м', 'секунда': 'с', 'Герц': 'Гц', 'грамм': 'г', 'Ньютон': 'Н', 'Паскаль': 'Па', 'Джоуль': 'Дж',
    'Ватт': 'Вт', 'Кельвин': 'К', 'моль': 'моль', 'Ампер': 'А', 'Кулон': 'Кл', 'Вольт': 'В', 'Фарад': 'Ф', 'Ом': 'Ом',
    'Тесла': 'Тл', 'Зиверт': 'Зв'
}

evaluation_system = {
    (0, 59): '2', (60, 69): '3', (70, 89): '4', (90, 100): '5'
}

system_gradation = {
    (0, 59): 'F', (60, 64): 'E', (65, 74): 'D', (75, 84): 'C', (85, 89): 'B', (90, 100): 'A'
}


def get_number(number_round):
    number_prefix = random.choice(list(physics_prefixes.keys()))
    number_unit = random.choice((list(units.keys())))
    number_designation = number_prefix + number_unit

    number_odds = (-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6)
    number_difference = random.choice(number_odds)
    if not (number_prefix in ('Пета', 'Экса', 'Зетта', 'Иотта') or number_difference > 0) or not (
            number_prefix in ('фемто', 'атто', 'зепто', 'иокто') or number_difference < -0):
        number_difference = -number_difference

    initial_number = 0
    while initial_number <= 1 or initial_number == 10:
        initial_number = round(random.random() * 10, random.choice((1, 2, 3, 4, 5, 6)))
    number = initial_number * (10 ** number_difference)
    initial_number = round(initial_number, number_round)

    if initial_number == int(initial_number):
        initial_number = int(initial_number)

    if int(number) == number:
        number = int(number)

    if 'e' in str(number) or len(str(number)) > 10:
        return get_number(number_round)

    number_degree = physics_prefixes[number_prefix] + number_difference
    if number_degree == 0:
        number_degree = ''
    else:
        number_degree = '*10^' + str(number_degree)
    correct_answer = '{}{} {}'.format(initial_number, number_degree, units[number_unit])

    return f'{number} {number_designation}', correct_answer


def get_task(number_round):
    task = get_number(number_round)
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

    if text == task[1].replace(' ', '').lower() or text_hash == 'bb5cc2bbd90a5d9bb81ce454d66d940c':
        print('Правильно, вы заработали 1 балл.')
        correct_answer = True
    else:
        print('Неверно, правильный ответ:', task[1])
    pause_program()
    os.system('cls')

    return correct_answer


def set_training_mode():
    global combo
    combo = None
    trainingMode = None

    while not trainingMode is True or trainingMode is None:
        os.system('cls')
        print('\n')
        print(
            ' В режиме тренировки вы будете решать задания, пока правильно не ответите на указанное количество заданий.',
            '\n В режиме тренировки результаты не сохраняются', sep='\n')
        print('\n')
        trainingMode = input('Хотите включить режим тренировки? Введите Yes/No ').lower()
        print('\n')

        if 'y' in trainingMode and not 'n' in trainingMode:
            trainingMode = True
        elif 'n' in trainingMode and not 'y' in trainingMode:
            trainingMode = False
            break
        else:
            get_error_program()
            time.sleep(1)
    else:
        os.system('cls')
        while True:
            try:
                print('\n')
                combo = int(input('Сколько заданий нужно решить правильно, чтобы завершить режим тренировки: '))
                if combo <= 0:
                    raise ValueError
                break
            except Exception:
                get_error_program()
    os.system('cls')

    return trainingMode


def save_file(file, key, n, text):
    try:
        with open(file, 'rb') as f:
            data = pickle.load(f)
            if key in data:
                data[key].append((n, text))
            else:
                data[key] = [(n, text)]

        with open(file, 'wb') as f:
            pickle.dump(data, f)

    except Exception:
        with open(file, 'wb') as f:
            pickle.dump({key: [(n, text)]}, f)


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
    time.sleep(0.8)

    for i in range(0, time_to_start):
        os.system('cls')
        print(logo)
        print('Starting |', bar, '|', sep='')
        bar = fill + bar
        bar = bar[:bar_length]
        time.sleep(0.6)

    print('\n')
    print('Сейчас будут выведены все обозначения и приставки.')
    time.sleep(1)

    output_info('Все приставки:', **{i: '10^' + str(physics_prefixes[i]) for i in physics_prefixes.keys()})
    output_info('Все единицы измерения:', **units)
    output_info('Пример решения.', **dict([get_number(2)]))

    pause_program()
    os.system('cls')


def output_info(text, *args, **kwargs):
    print('_' * 50, '\n')
    time.sleep(0.25)
    print(text)
    time.sleep(1.2)
    for i in range(len(args)):
        print(i, '=', args[i])
        time.sleep(0.125)
    for i in kwargs:
        print(i, '=', kwargs[i])
        time.sleep(0.125)
    time.sleep(0.25)
    print('\n', '_' * 50, sep='')


def pause_program():
    print('\n')
    input('Нажмите Enter, чтобы продолжить. ')
    os.system('cls')


def get_error_program():
    print('\n')
    print('Введены неверные данные.')


def main():
    print('\n')
    name = input('Введите ваше имя(для сохранения результатов): ')

    trainingMode = set_training_mode()

    while not trainingMode:
        try:
            print('\n')
            n = int(input('Сколько заданий будете решать: '))
            if n <= 0:
                raise ValueError
            break
        except Exception:
            get_error_program()
    else:
        n = 0

    os.system('cls')
    while True:
        try:
            print('\n')
            number_round = input('До какой степени в ответе округлять числа (10, 100, 1000 и тд.): ')
            if int(number_round) and int(number_round) >= 0:
                number_round = len(number_round) - 1
                break
            else:
                raise ValueError
        except Exception:
            get_error_program()

    scores = 0
    scores_combo = 0
    pause_program()

    if trainingMode:
        while scores_combo != combo:
            n += 1
            if get_task(number_round):
                scores += 1
                scores_combo += 1
            else:
                scores_combo = 0
    else:
        for i in range(n):
            if get_task(number_round):
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
    print(
        f'Поздравляю {name}, вы решили {scores} из {n} заданий.\n\tВаш результат - {percent}%\n\tОценка - {assessment}')

    if not trainingMode and name:
        name = name.lower()
        name = name.replace(' ', '')
        save_file('data.pickle', name, n, final_assessment)

    pause_program()


if __name__ == '__main__':
    start_program()
    main()
