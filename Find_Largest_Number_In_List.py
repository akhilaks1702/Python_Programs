class LargestNumber:

    def __init__(self, numbers):
        self.numbers = numbers

    def largest_number(self):
        big = self.numbers[0]
        for number in self.numbers:
            if number > big:
                big = number
        print(f"Largest number in the list: {big}")

numbers = [ 2, 65, 7, 9 ]
number_list = LargestNumber(numbers)
number_list.largest_number()






