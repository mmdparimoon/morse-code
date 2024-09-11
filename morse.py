#Dicrionary
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

# decode encode funct
def encode(massage):
    msg_list = [char for char in massage]
    not_in_dic = []
    for item in msg_list:
        if not item in MORSE_CODE_DICT:
            not_in_dic.append(item)
    encoded_msg = [MORSE_CODE_DICT[item] for item in msg_list if item in MORSE_CODE_DICT]
    final_decoded_msg = ' '.join(str(item) for item in encoded_msg)
    if len(not_in_dic) >= 1:
        return final_decoded_msg, f'{not_in_dic} are not in dictionary'
    else:
        return final_decoded_msg


def decode(massage):
    msg_list = massage.split()
    not_in_dic = []
    for item in msg_list:
        if not item in MORSE_CODE_DICT.values():
            not_in_dic.append(item)
    decoded_msg = [list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(item)]
                   for item in msg_list
                   if item in MORSE_CODE_DICT.values()]
    final_decoded_msg = ' '.join(str(item) for item in decoded_msg)
    ff2 = final_decoded_msg.replace(' ', '')
    if len(not_in_dic) >= 1:
        return ff2, f'{not_in_dic} are not in dictionary'
    else:
        return ff2

# core
cont =True
while cont:
    dec_enc = input('do you want encode or decode?(no for ending program): ').lower()
    if not dec_enc == 'no':
        if dec_enc == 'decode':
            massage = input(f'please inter your massage to decode; \ntype here: ').upper()
            masg = decode(massage)
            print(masg)
        elif dec_enc == 'encode':
            massage = input(f'please inter your massage to encode; \ntype here: ').upper()
            print(encode(massage))
        else:
            print('Enter a valid massage')
    if dec_enc == 'no':
        cont = False

print('\n Good bye')