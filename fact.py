import math

n=input("Input check number:")
try:
    n = int(eval(n))
except:
    print("Your input isn't a number")
    exit()

k = n
sent = str(n) + "="

m = 2  # start division with 2
while n > 1: # keep dividing till the number is greater than 1
    if m > k / 2 + 1:
        break
    i = 0
    while n % m == 0:
        n = n / m   # modify n by dividing it with current divisor
        i += 1
    
    if i > 1: # add only if m divides n at least once
        sent = sent + " " + str(m) + "^" + str(i) + " *"
    elif i == 1:
        sent = sent + " " + str(m) + " *"

    m = m + 1

if sent == str(n)+ "=":
    sent = sent + " 1 * " + str(n)
else:
    sent = sent[:-1]

print(sent)

k = input("Press any key")
if k != "":
    exit()