import numpy as np
count = 0                            # —Å—á–µ—Ç—á–∏–∫ –ø–æ–ø—ã—Ç–æ–∫
number = np.random.randint(1,101)    # –∑–∞–≥–∞–¥–∞–ª–∏ —á–∏—Å–ª–æ
print ("–ó–∞–≥–∞–¥–∞–Ω–æ —á–∏—Å–ª–æ –æ—Ç 1 –¥–æ 100")

while True:                        # –±–µ—Å–∫–æ–Ω–µ—á–Ω—ã–π —Ü–∏–∫–ª
    predict = int(input())         # –ø—Ä–µ–¥–ø–æ–ª–∞–≥–∞–µ–º–æ–µ —á–∏—Å–ª–æ
    count += 1                     # –ø–ª—é—Å—É–µ–º –ø–æ–ø—ã—Ç–∫—É
    if number == predict: break    # –≤—ã—Ö–æ–¥ –∏–∑ —Ü–∏–∫–ª–∞, –µ—Å–ª–∏ —É–≥–∞–¥–∞–ª–∏
    elif number > predict: print (f"–£–≥–∞–¥—ã–≤–∞–µ–º–æ–µ —á–∏—Å–ª–æ –±–æ–ª—å—à–µ {predict} ")
    elif number < predict: print (f"–£–≥–∞–¥—ã–≤–∞–µ–º–æ–µ —á–∏—Å–ª–æ –º–µ–Ω—å—à–µ {predict} ")
        
print (f"–í—ã —É–≥–∞–¥–∞–ª–∏ —á–∏—Å–ª–æ {number} –∑–∞ {count} –ø–æ–ø—ã—Ç–æ–∫.")
//hello

import numpy as np

def game_core_v1(number):
    '''è‡Æ·‚Æ „£†§Î¢†•¨ ≠† random, ≠®™†™ ≠• ®·ØÆ´Ïß„Ô ®≠‰Æ‡¨†Ê®Ó Æ °Æ´ÏË• ®´® ¨•≠ÏË•.
       î„≠™Ê®Ô Ø‡®≠®¨†•‚ ß†£†§†≠≠Æ• Á®·´Æ ® ¢Æß¢‡†È†•‚ Á®·´Æ ØÆØÎ‚Æ™'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # Ø‡•§ØÆ´†£†•¨Æ• Á®·´Æ
        if number == predict: 
            return(count) # ¢ÎÂÆ§ ®ß Ê®™´†, •·´® „£†§†´®
        
        
def score_game(game_core):
    '''á†Ø„·™†•¨ ®£‡„ 1000 ‡†ß, Á‚Æ°Î „ß≠†‚Ï, ™†™ °Î·‚‡Æ ®£‡† „£†§Î¢†•‚ Á®·´Æ'''
    count_ls = []
    np.random.seed(1)  # ‰®™·®‡„•¨ RANDOM SEED, Á‚Æ°Î ¢†Ë Ì™·Ø•‡®¨•≠‚ °Î´ ¢Æ·Ø‡Æ®ß¢Æ§®¨!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ç†Ë †´£Æ‡®‚¨ „£†§Î¢†•‚ Á®·´Æ ¢ ·‡•§≠•¨ ß† {score} ØÆØÎ‚Æ™")
    return(score)



score_game(game_core_v1)