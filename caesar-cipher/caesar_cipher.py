
def get_message():
    message = ''
    while message == '':
        message = input('Enter your message: ')
        if message == '':
            print('Please enter a non-blank message.')
    return message

def get_key(DICTIONARY):
    key = 0
    while key <= 0 or key > len(DICTIONARY):
        key = int(input('Enter a key (1-26): '))
        if key <= 0 or key > len(DICTIONARY):
            print('Invalid key, please try again.')
    return key

def get_mode():
    modes = ['encrypt', 'decrypt']
    mode = ''
    while mode == '' or mode not in modes:
        mode = input('Enter a mode for this message (encrypt|decrypt): ').lower()
        if mode == '' or mode not in modes:
            print('Invalid mode, please try again.')
    return mode.lower()

def translate_message(message, mode, key, DICTIONARY):
    message = message.upper()
    translated = ''

    for symbol in message:
        if symbol in DICTIONARY:
            num = DICTIONARY.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            
            if num >= len(DICTIONARY):
                num = num - len(DICTIONARY)
            elif num < 0:
                num = num + len(DICTIONARY)
            
            translated = translated + DICTIONARY[num]
        else:
            translated = translated + symbol
    return translated


DICTIONARY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = get_message()
    key = get_key(DICTIONARY)
    mode = get_mode()

    translated = translate_message(message, mode, key, DICTIONARY)
    output = str(mode[0].upper() + mode[1:]) + 'ed message: ' + translated
    print(output)

if __name__ == '__main__':
    main()