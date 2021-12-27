def celsius_to_fahrenheit(t: float) -> float:
    """
    Converts Celsius to Fahrenheit.
    """
    return 32 + t * 9 / 5

def celsius_to_kelvin(t: float) -> float:
    """
    Converts Celsius to Kelvin.
    """
    return t + 273.15

def fahrenheit_to_celsius(t: float) -> float:
    """
    Converts Fahrenheit to Celsius.
    """
    return (t - 32) * 5 / 9

def fahrenheit_to_kelvin(t: float) -> float:
    """
    Converts Fahrenheit to Kelvin.
    """
    return ((t - 32) * 5 / 9) + 273.15

def kelvin_to_celsius(t: float) -> float:
    """
    Converts Kelvin to Celsius.
    """
    return t - 273.15

def kelvin_to_fahrenheit(t: float) -> float:
    """
    Converts Kelvin to Fahrenheit.
    """
    return 32 + (t - 273.15) * 9 / 5
