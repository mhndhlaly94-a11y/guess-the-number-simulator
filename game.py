import random
H = random.randint(1,100)
S = 0
print("I choose a number between 1 and 100")
while True :
    M = int(input("Enter a number: "))
    S = S + 1
    if M == H :
        print("Correct")
        print(f"Attempts ({S})")
        break
    elif M > H :
        print("Down")
    else:
        print("Up")
# FUTURE GOOGLE AI ENGINEER IN THE MAKING.
# M.A