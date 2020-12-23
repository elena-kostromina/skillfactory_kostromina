import numpy as np

def game_core_v3(number):
    '''Сначала берем середину диапазона 0-100, а потом сдвигаем границы 
       в зависимости от того, больше или меньше нужного числа середина диапазона .
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 50
    predict_min = 0
    predict_max = 100
    while number != predict:
        count+=1
        if number > predict: 
            predict_min = predict
        elif number < predict: 
            predict_max = predict
        predict = (predict_min + predict_max) // 2
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(100))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)



score_game(game_core_v3)