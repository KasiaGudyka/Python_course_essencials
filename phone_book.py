# Creating and browsing a phone book

n = int(input('How namy contacts would you like to save?: '))
name_numbers = [input('Insert a name and a phone number (i.e. Kasia 888777666): ').split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}

choice = input('\nAre you looking for a number? (y/n)')

while choice != 'y' and choice != 'n': 
  choice = input('Sorry, I didn\'t catch that. Enter again: ')

while choice == 'y':
    try:
        name = input('Who\'s number are you looking for? ')
        if name in phone_book:
            print('A number to %s is %s' % (name, phone_book[name]))
            choice = input('\nAre you looking for another number? (y/n)')
        else:
            print('Not found')
            choice = input('\nAre you looking for another number? (y/n)')
    except:
        break
