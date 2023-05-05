class Palindrome:
    def _init_(self, number):
        self.number = number

    def is_palindrome(self):
        original_number = self.number
        reversed_number = 0
        while self.number > 0:
            digit = self.number % 10
            reversed_number = reversed_number * 10 + digit
            self.number //= 10
        if original_number == reversed_number:
            return True
        else:
            return False

number_input = int(input("Enter the number to check: "))
palindrome_obj = Palindrome(number_input)
if palindrome_obj.is_palindrome():
    print(f"{number_input} is a palindrome.")
else:
    print(f"{number_input} is not a palindrome.")
