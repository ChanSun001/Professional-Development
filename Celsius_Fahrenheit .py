class TempConverter:
    """Plug in a value x eg. TempConverter(x)
    and call the display_example_instructions below eg. TempConverter(2).display_example_instructions
    """
    input_temp = 0

    def __init__(self, input_temp):
        self.input_temp = input_temp

    def display_example_instructions(self):
        """
        This displays an example for what to input and what it would return.
        """
        print("Only accepts numerical digits eg. (2, 35.6)")
        print("Is this your input?", self.input_temp)
        print("if yes, choose celsius to fahrenheit? or fahrenheit to celsius?")
        print("eg. TempConverter(2).celsius_to_fahrenheit or TempConverter(2).fahrenheit_to_celsius")

    def celsius_to_fahrenheit(self):
        """
        This function is a converter for celsius to fahrenheit.
        """
        fahrenheit = self.input_temp * (9 / 5) + 32
        rounded_fahrenheit = round(fahrenheit, 2)
        print("When Celsius is", self.input_temp, "C", "The Fahrenheit is", rounded_fahrenheit, "F")

    def fahrenheit_to_celsius(self):
        """
        This function is a converter for fahrenheit to celsius.
        """
        celsius = (self.input_temp - 32) * (5/9)
        rounded_celsius = round(celsius, 2)
        print("When Fahrenheit is", self.input_temp, "F", "The Celsius is", rounded_celsius, "C")


TempConverter(2).display_example_instructions()
TempConverter(2).celsius_to_fahrenheit()
