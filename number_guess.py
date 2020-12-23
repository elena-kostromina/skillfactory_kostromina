import numpy as np

def game_core_v3(number):
    '''���砫� ��६ �।��� ��������� 0-100, � ��⮬ ᤢ����� �࠭��� 
       � ����ᨬ��� �� ⮣�, ����� ��� ����� �㦭��� �᫠ �।��� ��������� .
       �㭪�� �ਭ����� ���������� �᫮ � �����頥� �᫮ ����⮪'''
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
    return(count) # ��室 �� 横��, �᫨ 㣠����
        
        
def score_game(game_core):
    '''����᪠�� ���� 1000 ࠧ, �⮡� 㧭���, ��� ����� ��� 㣠�뢠�� �᫮'''
    count_ls = []
    np.random.seed(1)  # 䨪��㥬 RANDOM SEED, �⮡� ��� �ᯥਬ��� �� ���ந������!
    random_array = np.random.randint(1,101, size=(100))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"��� ������ 㣠�뢠�� �᫮ � �।��� �� {score} ����⮪")
    return(score)



score_game(game_core_v3)