import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")

while True:                        # бесконечный цикл
    predict = int(input())         # предполагаемое число
    count += 1                     # плюсуем попытку
    if number == predict: break    # выход из цикла, если угадали
    elif number > predict: print (f"Угадываемое число больше {predict} ")
    elif number < predict: print (f"Угадываемое число меньше {predict} ")
        
print (f"Вы угадали число {number} за {count} попыток.")
//hello

import numpy as np

def game_core_v1(number):
    '''���� 㣠�뢠�� �� random, ����� �� �ᯮ���� ���ଠ�� � ����� ��� �����.
       �㭪�� �ਭ����� ���������� �᫮ � �����頥� �᫮ ����⮪'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # �।���������� �᫮
        if number == predict: 
            return(count) # ��室 �� 横��, �᫨ 㣠����
        
        
def score_game(game_core):
    '''����᪠�� ���� 1000 ࠧ, �⮡� 㧭���, ��� ����� ��� 㣠�뢠�� �᫮'''
    count_ls = []
    np.random.seed(1)  # 䨪��㥬 RANDOM SEED, �⮡� ��� �ᯥਬ��� �� ���ந������!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"��� ������ 㣠�뢠�� �᫮ � �।��� �� {score} ����⮪")
    return(score)



score_game(game_core_v1)