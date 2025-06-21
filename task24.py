email = input("e-mailni kiriting : ")

natija = email[0] != '@' and email.endswith('.com')
print(natija)