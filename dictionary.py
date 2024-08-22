
# Example for using Python dictionary data structure

addressbook = {}  # (key, value)

# addressbook[key] = value 
option = 0
while True:
    print('What would you like to do!')
    print('1 - Adding new entry')
    print('2 - Search an entry')
    print('3 - Edit an entry')
    print('4 - Delete any existing entry')
    print('5 - Exit the system')
    
    option = input('Enter your option! Choose from 1 - 5')
    if option == '1':
        name = input('Enter your name!')
        phone = input('Enter your contact number!')
        addressbook[name] = phone
    elif option == '2':
        name = input('Enter your name!')
        if (name in addressbook):
            print('Contact number is: ', addressbook[name])
        else:
            print('This contact does not exist in addressbook')
    elif option == '4':
        name = input('Enter your name!')
        del addressbook[name]
        print('Contact is deleted!')
    elif option == '5':
        break
    else:
        print('Invalid option')
        