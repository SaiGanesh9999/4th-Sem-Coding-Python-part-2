class Year:
    def _init_(self, year):
        self.year = year

    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

year = int(input("Enter the year to check: "))
year_obj = Year(year_input)
if year_obj.is_leap_year():
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
