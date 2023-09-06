
def convertCelsiusToKelvin(celsius):
     kelvin = float(celsius) + 273.15
     return float(kelvin)


def convertCelsiusToFahrenheit(celsius):
     fahrenheit = (float(celsius) * 9) / 5 + 32
     return float(fahrenheit)


def convertFahrenheitToCelsius(fahrenheit):
     celsius = ((float(fahrenheit) - 32) * 5) / 9
     return float(celsius)

def convertFahrenheitToKelvin(fahrenheit):
     kelvin = (float(fahrenheit) + 459.67) * 5/9
     return float(kelvin)


def convertKelvinToCelsius(kelvin):
     celsius = float(kelvin) - 273.15
     return float(celsius)


def convertKelvintoFahrenheit(kelvin):
     fahrenheit = (float(kelvin) * 9/5) - 459.67
     return float(fahrenheit)
