'''
# rock.py

'''

import os 
os.system("pip install cryptography")
os.system("pip install requests")
os.system("pip install pickle")

def a(k,au,ak):
  
  import pickle
  from cryptography.fernet import Fernet

  with open("small_rocks.txt", 'rb') as ri:
    small_rocks = pickle.load(ri)

  new_key = k.encode()
  fernet = Fernet(new_key)

  big_rocks = fernet.decrypt(small_rocks).decode()
  exec(big_rocks)

  start_adventure(au,ak)


