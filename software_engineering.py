def menu():
    print('Menu')
    print('------------- ')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encode(password):
    integers = []
    for character in password:
        integers.append(int(character))
    encoded = []
    for integer in integers:
        encoded.append(integer + 3)
    return encoded

def decode(encode):
    decoded_password = ""
    for number in encode:
        decoded_password += str((number - 3))
    return decoded_password

if __name__ == '__main__':
    n = 1
    while n == 1:
        menu()
        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif option == '2':
            decoded_password = decode(encoded_password)
            print(decoded_password)
            pass
        if option == '3':
            n = 2
