def menu():
    print('Menu')
    print('------------- ')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encode(password):
    integers = [int(integer) for integer in password]
    encoded_integer = [(integer + 3) % 10 for integer in integers]
    encoded_password = "".join(str(integer) for integer in encoded_integer)
    return encoded_password


n = 1
if __name__ == '__main__':
    while n == 1:
        menu()
        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif option == '2':
            pass
        if option == '3':
            n = 2
