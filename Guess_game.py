import random

Random_Number = random.randint(1,100)
b = 0
c = 0
d = 5
while b != Random_Number:
        
    b = int(input(f'Guss a number(1 to 100) you have {d} chance: '))
    d -= 1
    c += 1
    
    if b < Random_Number and c != 5:
        print('Go upperr')
    elif b > Random_Number and c != 5:
        print('Go lower')
    elif b == Random_Number:
        print('Nice Done! :)')
        break
    if c == 5:
        print(f'The correct answer is {Random_Number}. you lose. try again!')
        break
    

    
    
        
