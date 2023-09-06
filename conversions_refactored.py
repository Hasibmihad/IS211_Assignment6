class ConversionNotPossible(Exception):
    pass
def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    # this is an dictionary, with key (from,to) = which function should return after playing with value 
    conversion_functions = {
        ("celsius", "kelvin"): lambda x: x + 273.15,
        ("celsius", "fahrenheit"): lambda x: (x * 9/5) + 32,
        ("kelvin", "celsius"): lambda x: x - 273.15,
        ("kelvin", "fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
        ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,
        ("fahrenheit", "kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("miles", "yards"): lambda x: x * 1760.0,
        ("yards", "miles"): lambda x: x / 1760.0,
        ("miles", "meters"): lambda x: x * 1609.34,
        ("meters", "miles"): lambda x: x / 1609.34,
        ("yards", "meters"): lambda x: x * 0.9144,
        ("meters", "yards"): lambda x: x / 0.9144
    }

  
    if fromUnit == toUnit:
        return value  # No conversion needed, return the same value

    #find the appropriate conversion function  by KEY (from,to)
    conversion_function = conversion_functions.get((fromUnit, toUnit))


    # Check if the conversion is not possible
    if conversion_function is None:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible")

    try:
        result = conversion_function(value)
        return round(result, 2)
    except Exception as e:
        raise ConversionNotPossible(f"Error during conversion: {e}")
