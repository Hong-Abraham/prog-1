def encoder(message):
    result = ''
    for digit in message:
        new = str((int(digit) + 3) % 10)
        result += new
    return result


def decoder(message)