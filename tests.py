import conversions

"""
result = conversions.convertCelsiusToFahrenheit(300.00)
assert result == 572.00, f"Expected 572.00°F but got {result}°F"


result = conversions.convertCelsiusToKelvin(300.00)
assert result == 573.15, f"Expected -40.00°F but got {result}°F" """

import unittest
class KnownValues(unittest.TestCase):
    knownvalues = (     #celcius,Farhenhiet,kalvin 
                        (500.00, 932.00, 773.15),
                        (400.00, 752.00, 673.15),
                        (300.00, 572.00, 573.15),
                        (200.00, 392.00, 473.15),
                        (100.00, 212.00, 373.15),
                        ( 0.00,  32.00, 273.15),
                        (-100.00, -148.00, 173.15),
                        (-200.00, -328.00,  73.15),
                        (-150.00, -238.00, 123.15),
                        (-220.00, -364.00,  53.15),
                        (-270.00, -454.00,   3.15)
                       )



    #tests the Celsius to Fahrenheit conversion using 
    def testConversionCelsiusToKelvin(self):
        for celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {celsius} degrees Celsius to {kelvin} Kelvin Conversion') 
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, round(result, 2))
     


    #tests the Celsius to Fahrenheit conversion
    def testConversionCelsiusToFahrenheit(self):
         for celsius, fahrenheit, kelvin in self.knownvalues:
                print(f'Validating {celsius} degrees Celsius to {fahrenheit} degrees Fahrenheit Conversion') 
                result = conversions.convertCelsiusToFahrenheit(celsius)
                self.assertEqual(fahrenheit, round(result, 2))



    #tests the Fahrenheit to Celsius conversion
    def testConversionFahrenheitToCelsius(self):
         for celsius, fahrenheit, kelvin in self.knownvalues:
                print(f'Validating {fahrenheit} degrees Fahrenheit to {celsius} degrees Celsius Conversion') 
                result = conversions.convertFahrenheitToCelsius(fahrenheit)
                self.assertEqual(celsius, round(result, 2))


    #test the Fahrenheit to Kelvin conversion
    def testConversionFahrenheitToKelvin(self):
        for celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {fahrenheit} degrees Fahrenheit converts to {kelvin} Kelvin Conversion') 
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, round(result, 2))

    #tests the Kelvin to Celsius conversion
    def testConversionKelvinToCelsius(self):
        for celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {kelvin} Kelvin converts to {celsius} degrees Celsius Conversion') 
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, round(result, 2))


    #tests the Kelvin to Fahrenheit conversion
    def testConversionKelvinToFahrenheit(self):
        for celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {kelvin} Kelvin converts to {fahrenheit} degrees Fahrenheit Conversion') 
            result = conversions.convertKelvintoFahrenheit(kelvin)
            self.assertEqual(fahrenheit, round(result, 2))



kv=KnownValues()
kv.testConversionKelvinToFahrenheit()