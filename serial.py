class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Getting starting value"""
        self.start = start #Storing starting value
        self.new_value = start - 1 #Incrementing property

    def generate(self):
        """Adding 1 to incrementing property"""
        self.new_value += 1
        return self.new_value

    def reset(self):
        """Set value back to original starting value"""
        self.new_value = self.start - 1
