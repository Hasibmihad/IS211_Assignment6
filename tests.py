import conversions
import unittest
import conversions_refactored
"""
result = conversions.convertCelsiusToFahrenheit(300.00)
assert result == 572.00, f"Expected 572.00°F but got {result}°F"


result = conversions.convertCelsiusToKelvin(300.00)
assert result == 573.15, f"Expected -40.00°F but got {result}°F" """


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


    # Miles to Yards conversion
    miles_to_yards_samples=(
    (2.0,3520.0),
    (0.5, 880.0),
    (0.25 ,440.0),
    ( 1.0 ,1760.0),
    ( 3.75,6600.0),
    )

    yards_to_miles_samples = (
    (1760.0, 1.0),
    (440.0, 0.25),
    (880.0, 0.5),
    (3520.0, 2.0),
    (4400.0, 2.5), )

    miles_to_meters_samples = (
    (2.0, 3218.68),
    (0.5, 804.67),
    (0.25, 402.33),
    (1.0, 1609.34),
    (3.75, 6035.02),
)

    meters_to_miles_samples = (
    (1609.34, 1.0),
    (402.34, 0.25),
    (804.68, 0.5),
    (3218.68, 2.0),
    (6036.98, 3.75),
    )

    yards_to_meters_samples = (
    (109.73, 100.34),
    (328.08, 300.0),
    (546.81, 500.0),
    (164.04, 150.0),
    (437.4, 399.96),
    )


    meters_to_yards_samples = (
    (250.0, 273.4),
    (750.0, 820.21),
    (937.5, 1025.26),
    (400, 437.45),
    (100.0,109.36)
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


    def testConvertSameValue(self):
        """convert() should return same value if converting from one unit to itself"""
        testdata = (
            ('kelvin', 'kelvin', 773.15),
            ('yards', 'yards', 880),
            ('celsius', 'celsius', -150),
            ('fahrenheit', 'fahrenheit', 572),
            ('miles', 'miles', 30)      
        )

        for from1,to1,value in testdata:
            result=conversions_refactored.convert(from1, to1, value)
            print (from1,to1,value)

    def testConvertIncompatibleUnits(self):
    
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert,
                          'Miles', 'Kelvin', 100
                          )
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert,
                          'Celcius', 'yards', 666
                          )
        
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert,
                          'Celcius', 'meter', 666
                          )

        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert,
                          'Celcius', 'yards', 666
                          )

    

#cobvert funct call

    def testConvertCelsiusToKelvin(self):
        for celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {celsius} degrees Celsius to {kelvin} Kelvin Conversion') 
            result = conversions_refactored.convert("celsius","kelvin",celsius)
            self.assertEqual(kelvin, round(result, 2))
     


    #tests the Celsius to Fahrenheit conversion
    def testConvertCelsiusToFahrenheit(self):
         for celsius, fahrenheit, kelvin in self.knownvalues:
                print(f'Validating {celsius} degrees Celsius to {fahrenheit} degrees Fahrenheit Conversion') 
                result = conversions_refactored.convert("celsius","fahrenheit",celsius)
                self.assertEqual(fahrenheit, round(result, 2))



    #tests the Fahrenheit to Celsius conversion
    def testConvertFahrenheitToCelsius(self):
         for celsius, fahrenheit, kelvin in self.knownvalues:
                print(f'Validating {fahrenheit} degrees Fahrenheit to {celsius} degrees Celsius Conversion') 
                result = conversions_refactored.convert("fahrenheit","celsius",fahrenheit)
                self.assertEqual(celsius, round(result, 2))


    #test the Fahrenheit to Kelvin conversion
    def testConvertFahrenheitToKelvin(self):
        for celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {fahrenheit} degrees Fahrenheit converts to {kelvin} Kelvin Conversion') 
            result = conversions_refactored.convert("fahrenheit","kelvin",fahrenheit)
            self.assertEqual(kelvin, round(result, 2))

    #tests the Kelvin to Celsius conversion
    def testConvertKelvinToCelsius(self):
        for  celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {kelvin} Kelvin converts to {celsius} degrees Celsius Conversion') 
            result = conversions_refactored.convert("kelvin","celsius",kelvin)
            self.assertEqual(celsius, round(result, 2))


    #tests the Kelvin to Fahrenheit conversion
    def testConvertKelvinToFahrenheit(self):
        for celsius, fahrenheit, kelvin in self.knownvalues:
            print(f'Validating {kelvin} Kelvin converts to {fahrenheit} degrees Fahrenheit Conversion') 
            result = conversions_refactored.convert("kelvin","fahrenheit",kelvin)
            self.assertEqual(fahrenheit, round(result, 2))






    def testConvertYardsToMiles(self):
        for yards,miles in self.yards_to_miles_samples:
            print(f'Validating {yards} yards= {miles} miles ') 
            result = conversions_refactored.convert('yards', 'miles', yards)
            self.assertEqual(miles, round(result, 2) )

    def testConvertMilesToYards(self):
       for miles,yards in self.miles_to_yards_samples:
            print(f'Validating {miles} miles = {yards} yards') 
            
            result = conversions_refactored.convert('miles', 'yards', miles)
            self.assertEqual(yards,round(result, 2))

    def testConvertMetersToMiles(self):
       for meters,miles in self.meters_to_miles_samples:
            print(f'Validating {meters} meters= {miles} miles') 
            result = conversions_refactored.convert('meters', 'miles', meters)
            self.assertEqual(miles, round(result, 2))

    def testConvertMilesToMeters(self):
     for miles,meters in self.miles_to_meters_samples:
            print(f"Validating {miles} miles= '{meters} meters") 
            result = conversions_refactored.convert('miles', 'meters', miles)
            self.assertEqual(meters, round(result, 2))

    def testConvertMetersToYards(self):
        for meters,yards in self.meters_to_yards_samples:
            print(f'Validating {meters} meters= {yards} yards') 
            result = conversions_refactored.convert('meters', 'yards', meters)
            self.assertEqual(yards, round(result, 2))

    def testConvertYardsToMeters(self):
        for yards,meters in self.yards_to_meters_samples:
            print(f'Validating {yards} yards= {meters} meters ') 
            result = conversions_refactored.convert('yards', 'meters', yards)
            self.assertEqual(meters, round(result, 2)) 
        



kv=KnownValues()
print("<-------------------Testing On Known Value --------------------->")
print ("\n")
print("<-------------------Testing Kelvin to --------------------->")
print ("\n")
kv.testConversionKelvinToFahrenheit()
kv.testConversionKelvinToCelsius()
print ("\n")

print("<-------------------Testing Celsius to --------------------->")
print ("\n")
kv.testConversionCelsiusToFahrenheit
kv.testConversionCelsiusToKelvin()
print ("\n")
print("<-------------------Testing Farhenheit to --------------------->")
print ("\n")
kv.testConversionFahrenheitToCelsius()
kv.testConversionFahrenheitToKelvin()
print ("\n")

print("<-------------------Testing Same Unit Convert --------------------->")
print ("\n")
kv.testConvertSameValue()
print ("\n")

print("<-------------------Testing Refactored Temp Unit Convert --------------------->")
print ("\n")
kv.testConvertCelsiusToFahrenheit()
print ("\n")
kv.testConvertCelsiusToKelvin()
print ("\n")
kv.testConvertFahrenheitToCelsius()
print ("\n")
kv.testConvertFahrenheitToKelvin()
print ("\n")

kv.testConvertKelvinToCelsius()
print ("\n")

kv.testConvertKelvinToFahrenheit()
print ("\n")


print("<-------------------Testing Distance Unit Convert --------------------->")
print ("\n")
kv.testConvertYardsToMeters()
print ("\n")
kv.testConvertYardsToMiles()
print ("\n")

kv.testConvertMetersToMiles()
print ("\n")
kv.testConvertMetersToYards()
print ("\n")


kv.testConvertMilesToMeters()
print ("\n")
kv.testConvertMilesToYards()
print ("\n")

print("<-------------------Invalid Unit Convert --------------------->")
print ("\n")
kv.testConvertIncompatibleUnits()
