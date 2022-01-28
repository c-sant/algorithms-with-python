from conversion.roman import roman_to_int, int_to_roman
from conversion.temperature import *


def test_roman_conv() -> bool:
    # numbers are expected to be the same when converted into roman and back
    # to int

    t_roman = [int_to_roman(i) for i in range(1, 2001)]
    t_int = [roman_to_int(i) for i in t_roman]

    return t_int == list(range(1, 2001))


def test_to_celsius() -> bool:
    f_case = fahrenheit_to_celsius(32) == 0
    k_case = kelvin_to_celsius(273.15) == 0

    return f_case and k_case


def test_to_fahrenheit() -> bool:
    c_case = celsius_to_fahrenheit(0) == 32
    k_case = kelvin_to_fahrenheit(273.15) == 32

    return c_case and k_case


def test_to_kelvin() -> bool:
    c_case = celsius_to_kelvin(0) == 273.15
    f_case = fahrenheit_to_kelvin(32) == 273.15

    return c_case and f_case


if __name__ == '__main__':
    print(
        f"Roman Conversions: {'OK' if test_roman_conv() else 'FAILED'}\n"
        f"Conversions to Celsius: {'OK' if test_to_celsius() else 'FAILED'}\n"
        f"Conversions to Fahrenheit: {'OK' if test_to_fahrenheit() else 'FAILED'}\n"
        f"Conversions to Kelvin: {'OK' if test_to_kelvin() else 'FAILED'}"
    )
