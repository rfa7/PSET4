print("Start")
#import sys
#sys.path.insert(0, 'F:\Dev\Py')
global random
global password
import random
def password(lenght):
    passw = ""
    characters = "abcdefghijklmnoprstuwxyz" + "0123456789"
    for i in range(lenght):
        passw += random.choice(characters)
    print('Twoje haslo to: ')
    print('------------------')
    return passw
    

print(password(int(input('podaj ilosc znkow hasla: '))))
print('------------------')
print('End')
