def vigenere_cipher(plaintext, key):
    key = key.upper().replace('Ç', 'C')  # converte para maiúsculas e substitui 'Ç' por 'C'
    ciphertext = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')  # determina o deslocamento
            if char.isupper():
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)  # cifra o caractere maiúsculo
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)  # cifra o caractere minúsculo
            i += 1
        else:
            ciphertext += char  # mantém os caracteres não alfabéticos
    return ciphertext

plaintext = "Acredite em si mesmo e todo o resto se encaixara. Tenha fe em seus proprios talentos, habilidades e potencialidades, e voce sera capaz de alcançar coisas que antes pareciam impossiveis."
key = 'objetivos'
ciphertext = vigenere_cipher(plaintext, key)
print(ciphertext)