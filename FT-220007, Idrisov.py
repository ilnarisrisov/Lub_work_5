sentence = str(input('\nВведите предложение, написанное латинскими буквами: '))
shift = int(input('\nВведите сдвиг шифра Цезаря: '))

if shift > 0 and shift < 27:


    def Ceasar_s_cipher(sentence, shift):

        encrypted_sentence = ''
        for char in sentence:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                    encrypted_char = char
            encrypted_sentence += encrypted_char
        return encrypted_sentence


    encrypted_sentence = Ceasar_s_cipher(sentence, shift)
    print('\nЗашифрованный текст: ' + encrypted_sentence)

else:
    print('\nВыбран слишком большой сдвиг шифра')