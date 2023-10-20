from function import *
from numb import key, m, round_number, message_len
from replacement import table_swap

n1 = []  # первые 8 бит текста
n2 = []  # вторые 8 бит текста

# Реверс входного сообщения в бинарном ввиде
for i in range(message_len - 1, -1, -1):
    if message_len <= 8:
        n1.append(bin(m[i]))
        n2.append(bin(m[i]))
    else:
        if i >= 8:
            n2.append(bin(m[i]))
        elif i < 8:
            n1.append(bin(m[i]))

# Из [0b0,0b1] приводим к формату [0000,0001....]
normal_view_bin_list(n1)
normal_view_bin_list(n2)

for i in range(1, round_number + 1):
    print("|_____", i, "РАУНД _____|")
    key_n = key[i - 1]
    print("n2:    ", view_bin_4_bit_str(bin_to_str(n2)))  # перевод строки в спиок(списка в строку)
    print("n1:    ", view_bin_4_bit_str(bin_to_str(n1)))  # перевод строки в спиок(списка в строку)
    print("key:   ", view_bin_4_bit_str(bin_to_str(key_n)))  # вывод строки в виде списка
    print_separator()
    sum_n1_key_strbin = sum_bin(n1, key_n)  # Сумма N1 и Key
    sum_n1_key_list = normal_view_bin_list(sum_n1_key_strbin)  # сумма в виде списка
    digit_sum_n1_key0 = bin_to_digit(sum_n1_key_list)  # сумма в десятичном формате
    after_swap_digit = table_swap(digit_sum_n1_key0)  # Табличная перестановка в десятичном формате
    after_swap_bin = digit_to_bin(after_swap_digit)  # Табличная перестановка в двоичном формате

    print("Сумма (N1 + Key): ", view_bin_4_bit_str(sum_n1_key_strbin))  # Сумма двух чисел в бинарном виде (N1 + KEY)
    print("Сумма в десятичном виде (N1 + Key):   ", digit_sum_n1_key0)
    print_separator()
    print("После перестановки в двоичном виде:   ", view_bin_4_bit_str(bin_to_str(after_swap_bin)))
    print("После перестановки по таблице:        ", after_swap_digit)

    bin_shift = shift(bin_to_str(after_swap_bin), 11)  # Циклический сдвиг на 11
    sum_n1_n2_strbin = sum_xor_bin(bin_shift, n2)  # Сумма двух чисел в бинарном виде (N1(bin_shift) + N2)
    # Сумма в виде списка
    sum_n1_n2_list = strbin_to_list(sum_n1_n2_strbin)
    sum_n1_n2_list = normal_view_bin_list(sum_n1_n2_list)
    print_separator()
    print("Сдвиг на 11:                             ", view_bin_4_bit_str(bin_shift))
    print("N2:                                      ", view_bin_4_bit_str(bin_to_str(n2)))
    print("Сумма (Сдвиг N1 + N2):                   ", view_bin_4_bit_str(sum_n1_n2_strbin))
    print("Сумма (Сдвиг N1 + N2) в десятичном виде: ", bin_to_digit(sum_n1_n2_list))

    # Подготовка к следующему раунду
    # Меняем месатми n1 и n2
    n2 = normal_view_bin_list(n1)
    n1 = sum_n1_n2_list
    print()
    print("<----- ПАРМЕТРЫ ДЛЯ СЛЕДУЮЩЕГО РАУНДА -----> ")
    print("N1:", view_bin_4_bit_str(bin_to_str(n1)))
    print("Десятичный формат N1:", bin_to_digit(n1))
    print("N2:", view_bin_4_bit_str(bin_to_str(n2)))
    print("Десятичный формат N2:", bin_to_digit(n2))
    print()
