import random

for i in range(1,6):
    for j in range(i):
        ran = random.randint(0, 9)
        if(ran % 2 == 0):
            ran = "p"
        print(f"{ran} ", end="")
    print(" ")
        