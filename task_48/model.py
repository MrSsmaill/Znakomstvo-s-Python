def inrut_data():
    with open('Phonebook.txt', "r", encoding="utf-8") as data:
        a = data.read().split()