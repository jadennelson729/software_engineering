def menu():
    print('Menu')
    print('------------- ')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encode():
    integers = []
    for character in password:
        integers.append(int(character))
    encoded = []
    for integer in integers:
        encoded.append(integer + 3)


n = 1
if __name__ == '__main__':
    while n == 1:
        menu()
        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter your password to encode: ')
            encode()
            print('Your password has been encoded and stored!')
            print()
        elif option == '2':
            pass
        if option == '3':
            n = 2
