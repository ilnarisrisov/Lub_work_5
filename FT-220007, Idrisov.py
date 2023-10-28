language = input('Введите "1", если хотите зашифровать код на русском языке'
                     ', введите "2", если хотите зашифровать на латинском: ')
sentence = str(input('\nВведите предложение: '))
shift = int(input('\nВведите сдвиг шифра Цезаря: '))


def Ceasar_s_cipher_RU(sentence, shift):

    encrypted_sentence = ''

    i = 0
    while i < len(sentence):
        letter = sentence[i]
        if letter.isalpha():
            if letter.isupper():
                encrypted_sentence += chr((ord(letter) - 1040 + shift) % 33 + 1040)

            else:
                encrypted_sentence += chr((ord(letter) - 1072 + shift) % 33 + 1072)

        else:
            encrypted_sentence += letter

        i += 1
    return encrypted_sentence


def Ceasar_s_cipher_EN(sentence, shift):

    encrypted_sentence = ''

    for letter in sentence:
        if letter.isalpha():
            ascii_offset = ord('a') if letter.islower() else ord('A')
            encrypted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_letter = letter
        encrypted_sentence += encrypted_letter
    return encrypted_sentence

if language == '1':

    encrypted_sentence = Ceasar_s_cipher_RU(sentence, shift)
    print('\nЗашифрованный текст: ' + str(encrypted_sentence))

elif language == '2':

    encrypted_sentence = Ceasar_s_cipher_EN(sentence, shift)
    print('\nЗашифрованный текст: ' + str(encrypted_sentence))

else:
    print('\nВведено неверное число для выбора языка')

