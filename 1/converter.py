
HEX_CHARS = '0123456789ABCDEF'
BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
BIN_DIGITS_PER_HEX_CHAR = 4
BIN_DIGITS_PER_BASE64_CHAR = 6


def hex_to_base64(hex_str):
    return bin_string_to_base64(hex_to_bin_string(hex_str))


def base64_to_hex(hex_str):
    return bin_string_to_hex(base64_to_bin_string(hex_str))


def base64_char_to_int(base64_char):
    return BASE64_CHARS.index(base64_char)


def int_to_base64_char(int_num):
    return BASE64_CHARS[int_num]


def int_to_hex_char(int_num):
    return HEX_CHARS[int_num]


def hex_char_to_int(hex_char):
    return HEX_CHARS.index(hex_char.upper())


def hex_to_bin_string(hex_str):
    return _convert_to_bin_string(hex_str, hex_char_to_int, BIN_DIGITS_PER_HEX_CHAR)


def base64_to_bin_string(base64_str):
    return _convert_to_bin_string(base64_str, base64_char_to_int, BIN_DIGITS_PER_BASE64_CHAR)


def _convert_to_bin_string(string, unit_converter, digits):
    return ''.join([int_to_bin_string(unit_converter(char)).zfill(digits)
                    for char
                    in string])


def int_to_bin_string(int_num):
    buff = ''

    value = int_num

    while value > 0:
        buff = '%s%s' % (str(value % 2), buff)
        value /= 2

    return buff


def bin_str_to_int(bin_str):
    return sum([int(digit) * (2 ** index) for index, digit in enumerate(reversed(bin_str))])


def bin_string_to_base64(bin_string):
    return _convert_bin_string(bin_string, int_to_base64_char, BIN_DIGITS_PER_BASE64_CHAR)


def bin_string_to_hex(bin_string):
    return _convert_bin_string(bin_string, int_to_hex_char, BIN_DIGITS_PER_HEX_CHAR)


def _convert_bin_string(bin_string, converter, digits):
    result = ''
    chars = list(bin_string)

    while chars:
        result = '%s%s' % (converter(bin_str_to_int(chars[-digits:])), result)
        del chars[-digits:]
    return result



