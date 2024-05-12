def autores():
    return '''Pedro Parra - Bruno César - Matheus Zambrana'''


def dec2any(numero, base):
    """
    > Converte um número decimal para qualquer base até 16
    > Parâmetro numero: número do tipo inteiro
    > Parâmetro base: base númerica do número
    > Return: retorna uma string
    """
    if base < 2 or base > 16:
        return "A base deve estar entre 2 e 16."

    if numero == 0:
        return f'O número {numero} na base 10 é igual a 0 na base {base}'


    dec_to_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] # Lista de caracteres suportadas
    quociente = int(numero)
    resto = 0
    numero_convertido = ''

    while quociente != 0:
        resto = quociente % base
        quociente = quociente // base
        numero_convertido += dec_to_hex[resto]

    numero_convertido = numero_convertido[::-1] # Inverter os restos para corrigir o resultado

    return f'O número {numero} na base Decimal é igual a {numero_convertido} na base {base}'


def any2dec(numero, base):
    """
    > Converte um número na base especificada para decimal
    > Parâmetro numero: número do tipo inteiro ou uma string contendo números e letras de A-F
    > Parâmetro base: base númerica do número
    > Return: retorna uma string
    """
    if base < 2 or base > 16:
        return "A base deve estar entre 2 e 16"

    if numero == 0:
        return f"O número {numero} na base {base} é igual a 0"

    lista_de_numeros = []
    meu_dicionario = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    if isinstance(numero, str):
        for letra in numero:
            if letra.isdigit():
                lista_de_numeros.append(int(letra))
            else:
                if letra.upper() not in meu_dicionario:
                    return 'Letra invalida. Apenas letras de A-F são permitidas.'

                lista_de_numeros.append(meu_dicionario[letra.upper()])
    else:
        lista_de_numeros.append(numero)

    numero_decimal = 0
    tamanho = len(lista_de_numeros)

    for index, x in enumerate(lista_de_numeros):
        digito = lista_de_numeros[tamanho - 1 - index]
        numero_decimal += digito * (base ** index)

    return f'O {numero} na base {base} é igual a {numero_decimal} na base Decimal'