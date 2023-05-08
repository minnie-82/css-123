import random

# step 1: consider two large prime numbers i.e. p & q

# p,q = map(int,input("Enter two large prime numbers: ").split())
p,q = 353,37

# consider any two random numbers a & b

a,b = random.randint(50,1000), random.randint(50,1000)

# step 2
R = (q**a) % p

# step 3
S = (q**b) % p

# step 4 calculate secret key for user 1
Rk = S**a % p

# step 5 calculate secret key for user 2
Sk = R**b % p

if Sk==Rk:
    print("Unlocked!")
else:
    print("Invalid key!")