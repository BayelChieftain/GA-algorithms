book = dict()

book['apple'] = 1.1
book['milk'] = 2.01
book['orange'] = 3.4

print(book['milk'])
print(book)

name = input('Введите ваше имя!: ')
phonenumber = input('Введите ваш номер телефона!: ')
allContact = dict()
def contact(name, phonenumber):
    if allContact.get(name):
        print('Ваше имя уже есть!')
    else:
        allContact[name] = phonenumber
        print(allContact)

contact(name, phonenumber)