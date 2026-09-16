import random
import string
X=int(input("Enter password length: ")) #password length
Y= string.ascii_letters+string.digits+string.punctuation #password characters
if X <= 0:
    print("Password length must be greater than 0")
    exit()
else:
    password=''.join(random.choice(Y) for _ in range(X))
    print("Your password is: ", password)