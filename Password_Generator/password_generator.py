
import random
import string 
print("=" * 35)
print("      PASSSWORD GENERATOR")
length = int(input("enter password length:"))
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password += random.choice(characters)
print("\n generated password:",password)
if length>=12:
        print("password strength:strong")
elif length>=8:
        print("password strength:medium")
else:
        print("password strength:weak")
again=input("\n Generate another password?(yes/no):")
print("Thank you for using password generator!")            
