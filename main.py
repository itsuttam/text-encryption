text = input('Enter any text: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
translation_table = str.maketrans(alphabet, shifted_alphabet)
encrypted_text = text.translate(translation_table)
print('Encrypted text:', encrypted_text)