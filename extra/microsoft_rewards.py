import os
from random_words import RandomWords
import string
import random
rw = RandomWords()

userprofile = str(os.environ['USERPROFILE'])

x = 5 # Number of times to search
a = 0


try:
    while(a<x):
        search_term = rw.random_word(random.choice(string.ascii_lowercase))
        os.system("start microsoft-edge:"+search_term)
        a += 1
        os.system("TIMEOUT /t 5")
        if(a>=x):
            os.system("taskkill /F /IM MicrosoftEdge.exe /T")# Fix Tab caching
            exit()
except Exception as e:
    print("Broke with " + e)
    os.system("pause")
