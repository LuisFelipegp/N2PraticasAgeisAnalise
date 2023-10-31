def encryptThis(message):
    words = message.split()  # Divide a mensagem em palavras
    encrypted_words = []

    for word in words:
        if len(word) == 0:
            encrypted_words.append('')
        else:
            first_char = str(ord(word[0]))  # Converte o primeiro caractere para seu código ASCII
            if len(word) > 1:
                
                encrypted_word = first_char + word[-1] + word[2:-1] + word[1]
            else:
                encrypted_word = first_char
            encrypted_words.append(encrypted_word)

    return ' '.join(encrypted_words)  # Reconstroi a mensagem com as palavras criptografadas

# Teste para palavra de cinco letras
def test_encryptThis_five_letters():
    assert encryptThis("Hello") == '72olle'

# Teste para palavra de quatro letras
def test_encryptThis_four_letters():
    assert encryptThis("good") == '103doo'

# Teste para mensagem com duas palavras
def test_encryptThis_two_words():
    assert encryptThis("hello world") == '104olle 119drlo'

# Teste para mensagem vazia
def test_encryptThis_empty_message():
    assert encryptThis("") == ''

# Teste para palavra de uma letra
def test_encryptThis_one_letter():
    assert encryptThis("A") == '65'

# Executa os testes
if __name__ == '__main__':
    test_encryptThis_five_letters()
    test_encryptThis_four_letters()
    test_encryptThis_two_words()
    test_encryptThis_empty_message()
    test_encryptThis_one_letter()
    print("Testes realizados com sucesso!")
