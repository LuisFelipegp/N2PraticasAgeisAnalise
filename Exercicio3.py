def digital_root(n):
    # Função para calcular a raiz digital de um número
    while n >= 10:
        # Transforma o número em uma lista de dígitos
        digit_list = [int(digit) for digit in str(n)]
        # Calcula a soma dos dígitos
        n = sum(digit_list)
    return n

# Teste para número de dois dígitos
def test_digital_root_two_digits():
    assert digital_root(16) == 7

# Teste para número de três dígitos
def test_digital_root_three_digits():
    assert digital_root(942) == 6

# Teste para número de seis dígitos
def test_digital_root_six_digits():
    assert digital_root(132189) == 6

# Teste para número de seis dígitos
def test_digital_root_seven_digits():
    assert digital_root(493193) == 2

# Teste para número de um dígito
def test_digital_root_single_digit():
    assert digital_root(7) == 7

# Executa os testes
if __name__ == '__main__':
    test_digital_root_two_digits()
    test_digital_root_three_digits()
    test_digital_root_six_digits()
    test_digital_root_seven_digits()
    test_digital_root_single_digit()
    print("Testes realizados com sucesso!")
