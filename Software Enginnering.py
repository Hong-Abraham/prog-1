def encoder(message):
    result = ''
    for digit in message:
        new = str((int(digit) + 3) % 10)
        result += new
    return result


def decoder(message):
    result = ''
    for digit in message:
        new = str((int(digit)- 3) % 10)
        result += new
    return result


def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        choice = input('\nPleas enter an option: ')
        if choice == 1:
            value = input("Please enter your password to encode: ")
            print('Password has been encoded and stored!')
        if choice == 2: