import numpy as np

def game_core_v2(number):
    '''���砫� ��⠭�������� �� random �᫮, � ��⮬ 㬥��蠥� ��� 㢥��稢��� ��� � ����ᨬ��� �� ⮣�, ����� ��� ��� ����� �㦭���.
       �㭪�� �ਭ����� ���������� �᫮ � �����頥� �᫮ ����⮪'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
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