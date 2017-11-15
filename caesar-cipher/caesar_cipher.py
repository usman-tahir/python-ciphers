
message = input('Enter your message: ')

key = 0
while key <= 0 or key > 26:
    key = int(input('Enter a key (1-26): '))
    if key <= 0 or key > 26:
        print('Invalid key, please try again.')

modes = ['encrypt', 'decrypt']
mode = ''

while mode == '' or mode not in modes:
    mode = input('Enter a mode for this message (encrypt|decrypt): ').lower()
    if mode == '' or mode not in modes:
        print('Invalid mode, please try again.')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = message.upper()
translated = ''

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol

print(translated)