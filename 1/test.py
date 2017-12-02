import converter


def test_hex_to_base64():
    assert converter.hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d') == \
        'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


def test_base64_to_hex():
    assert converter.hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d') == \
        'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


def test_base64_char_to_int():
    assert converter.base64_char_to_int('A') == 0
    assert converter.base64_char_to_int('a') == 26


def test_hex_char_to_int():
    assert converter.hex_char_to_int('a') == 10
    assert converter.hex_char_to_int('A') == 10


def test_hex_to_bin_string():
    assert converter.hex_to_bin_string('F') == '1111'
    assert converter.hex_to_bin_string('F0') == '11110000'
    assert converter.hex_to_bin_string('FE') == '11111110'
    assert converter.hex_to_bin_string('FF') == '11111111'


def test_int_to_bin_string():
    assert converter.int_to_bin_string(15) == '1111'
    assert converter.int_to_bin_string(240) == '11110000'
    assert converter.int_to_bin_string(254) == '11111110'
    assert converter.int_to_bin_string(255) == '11111111'


def test_bin_str_to_int():
    assert converter.bin_str_to_int('0') == 0
    assert converter.bin_str_to_int('1') == 1
    assert converter.bin_str_to_int('0000') == 0
    assert converter.bin_str_to_int('1010') == 10


def test_bin_string_to_base64():
    assert converter.bin_string_to_base64('010000') == 'Q'
    assert converter.bin_string_to_base64('000100') == 'E'
    assert converter.bin_string_to_base64('010011010110000101101110') == 'TWFu'


def test_bin_string_to_hex():
    assert converter.bin_string_to_base64('10') == 'C'
    assert converter.bin_string_to_base64('0010') == 'C'
    assert converter.bin_string_to_base64('10010') == 'S'
    assert converter.bin_string_to_base64('010010') == 'S'
    assert converter.bin_string_to_base64('111111') == '/'
    assert converter.bin_string_to_base64('1111111') == 'B/'


def test_int_to_base64_char():
    assert converter.int_to_base64_char(4) == 'E'
    assert converter.int_to_base64_char(16) == 'Q'


def test_int_to_hex_char():
    assert converter.int_to_hex_char(4) == '4'
    assert converter.int_to_hex_char(15) == 'F'


