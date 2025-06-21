file = input("Fileni kiriting : ")

natija = file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt')
print(natija)