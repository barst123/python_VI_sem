#Działania na podstawowym środowisku Pythona
#print("Hello World")
#help(print)
#Moduły i przestrzenie nazw
from os import getcwd
current_path=getcwd
import czas
print(czas.aktualny_czas)
import time
time.sleep(20)
print(czas.aktualny_czas)
import imp
imp.reload(czas)
print(czas.aktualny_czas)