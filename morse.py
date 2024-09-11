MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': ' '}


# dec_enc=input('do you want encode or decode?').lower()

def encode(massage):
    msg_list = [char for char in massage]
    encoded_msg=[MORSE_CODE_DICT[item] for item in msg_list if item in MORSE_CODE_DICT]
    final_decoded_msg = ' '.join(str(item) for item in encoded_msg)
    return final_decoded_msg

def decode(massage):
    msg_list = massage.split()
    decoded_msg = [list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(item)]
                   for item in msg_list
                   if item in MORSE_CODE_DICT.values()]
    final_decoded_msg = ' '.join(str(item) for item in decoded_msg)
    ff2=final_decoded_msg.replace(' ', '')
    return ff2


# dec_enc=input('do you want encode or decode?(NO for ending program)').lower()


cont =True
while cont:
    dec_enc = input('do you want encode or decode?(no for ending program): ').lower()
    if dec_enc == 'encode' or 'decode':
        if dec_enc == 'decode':
            massage = input(f'please inter your massage to decode; \ntype here: ').upper()
            try:
                masg=decode(massage)
                print(masg)
            except KeyError:
                raise 'Not in morse deictionary'

        if dec_enc == 'encode':
            massage = input(f'please inter your massage to encode; \ntype here: ').upper()
            try:
                masg=encode(massage)
                print(masg)
            except KeyError:
                raise 'Not in morse deictionary'
    if dec_enc == 'no':
        cont = False
    else:
        print('Enter a valid masage')

print('Good bye')