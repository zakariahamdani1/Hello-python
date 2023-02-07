s = input('Enter your string: ')
S = s.split()
A = []
for i in range(len(S)):
    U = S[i][0].upper()
    A.append(U + S[i][1:])

Final = " ".join(A)
print(Final)
    


    

