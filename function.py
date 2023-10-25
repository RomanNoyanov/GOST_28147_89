def bin_to_digit(mas_n):
    """ПЕРЕВОД СПИСОКА ИЗ ЭЛЕМЕНТОВ ПО 4 БИТА В ДЕСЯТИЧНЫЙ ФОРМАТ ([0000,0001...] -> [0,1...])"""
    s = []
    for i in mas_n:
        s.append(str((int(i, 2))))  # Бинарное число в десятичном формате
    return s


def digit_to_bin(swap_digit):
    """ПЕРЕВОД СПИСКА ДЕСЯТИЧНЫХ ЧИСЕЛ В ДВОИЧНЫЙ ФОРМАТ ([0,1...] -> [0000,0001...])"""
    s = []
    for i in swap_digit:
        s.append(bin(i))  # Десятичное число в бинарный вид
    return s


def bin_to_str(mas_n):
    """СПИСОК ИЗ ЭЛЕМЕНТОВ ПО 4 БИТА В СТРОКУ ([0000,0001] -> 00000001)"""
    result = ""
    for i in mas_n:
        if "0b" in i:
            result += (4 - len(i[2:])) * "0" + i[2:]
        else:
            result += str(i)
    return result


def strbin_to_list(strbin):
    """ПЕРЕВОД ДВОИЧНОЙ СТРОКИ В СПИСОК [0000,0001,...]"""
    if "b" in strbin:  # Проверка на наличние "0b" у строки
        strbin = strbin[2:]
    return [strbin[i:i + 4] for i in range(0, len(strbin), 4)]


def view_bin_4_bit_str(strbin):
    """ РАЗДЕЛЕНИЕ СТРОКИ ИЗ БИНАРНЫХ ЧИСЛ ПО 4 БИТА (00000001 ->0000 0001)"""
    if "b" in strbin:  # Проверка на наличние "0b" у строки
        strbin = strbin[2:]
    number = (' '.join(strbin[i:i + 4] for i in range(0, len(strbin), 4)))
    return number


def normal_view_bin_list(mas):
    """ПЕРЕВОД В ЧИТАБЕЛЬНЫЙ ВИД ([0b0,0b1...] -> [0000, 0001])"""
    return strbin_to_list(bin_to_str(mas))


def sum_bin(n1, key):
    """СУММА ДВУХ БИНАРНЫХ ЧИСЕЛ (N1+Key) mod2^32"""
    strbin_n1 = bin_to_str(n1)
    strbin_n2 = bin_to_str(key)
    s = str(int(strbin_n1, 2) + int(strbin_n2, 2))
    print(bin(int(s)))
    result = bin(int(s))
    if len(result[2:]) < 32:
        result = (32 - len(result[2:])) * "0" + result[2:]
    else:
        result = bin(int(s))[-32:]
    return result


def sum_xor_bin(mas_n1, mas_n2):
    """СУММА ДВУХ БИНАРНЫХ ЧИСЕЛ (N1+N2) mod2"""
    strbin_n1 = bin_to_str(mas_n1)
    strbin_n2 = bin_to_str(mas_n2)
    s = str(int(strbin_n1, 2) ^ int(strbin_n2, 2))
    result = bin(int(s))

    if len(result[2:]) < 32:
        result = (32 - len(result[2:])) * "0" + result[2:]

    return result


def shift(strbin, n):
    """ЦИКЛИЧНЫЙ СДВИГ БИНАРНОЙ СТРОКИ НА n ЭЛЕМЕНТОВ"""
    swap = strbin[n:] + strbin[:n]
    return swap


def print_separator():
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
