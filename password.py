import string
import random


def create_pwd(pass_len):
    resourse = string.punctuation + string.ascii_letters + string.digits
    lst = []
    for i in range(pass_len):
        lst.append(random.choice(resourse))
    return "".join(lst)


"""print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
print(string.digits)
print(string.whitespace)
print(string.hexdigits)"""

pass_len = int(input("Tan heden orontoi nuuts ug uusgeh we ?\n"))
print(type(pass_len))

created_pass = create_pwd(pass_len)
print(created_pass)
# Example #
dr = []
print(string.punctuation)
dr = string.punctuation
print(dr)
print(dr)
