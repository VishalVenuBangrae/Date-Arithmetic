from datetime import date
import math


class Date:
    # Constructor
    def __init__(self, m, d, y):
        self.m = m
        self.d = d
        self.y = y

    def leap_year(self):
        return (self.y % 4 == 0) and not (self.y % 100 == 0 and self.y % 400 != 0)

    # To implement this class method, you can use Python's datetime package
    @classmethod
    def today(cls):
        date_today = str(date.today())
        year, month, day = date_today.split("-")
        month_new_0, month_new = month.split("0")
        return Date(month_new, day, year)

    # https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    # Gauss - disparate  variation
    # returns day of week as a String ("Sunday", "Monday", ...)
    def day_of_weekS(self):
        offset_dict = {1: 11, 2: 12, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9, 12: 10}
        year = self.y
        month = self.m
        for i in offset_dict.keys():
            if i == month:
                m = offset_dict[i]
        if m == 11 or m == 12:
            year -= 1
        c = year // 100
        y = year - (100 * c)
        w = (self.d + math.floor((2.6 * m) - 0.2) + y + math.floor(y // 4) + math.floor(c // 4) - (2 * c)) % 7
        str_day = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
        for i in str_day.keys():
            if i == w:
                day = str_day[i]
        return day

    # returns day of week as a number (0 for "Sunday", 1 for "Monday", ...)
    def day_of_weekN(self):
        offset_dict = {1: 11, 2: 12, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9, 12: 10}
        year = self.y
        month = self.m
        for i in offset_dict.keys():
            if i == month:
                m = offset_dict[i]
        if m == 11 or m == 12:
            year -= 1
        c = year // 100
        y = year - (100 * c)
        w = (self.d + math.floor((2.6 * m) - 0.2) + y + math.floor(y // 4) + math.floor(c // 4) - (2 * c)) % 7
        return w

    # Returns the Date object one day after self

    def tomorrow(self):
        today_d = self.d
        today_m = self.m
        today_y = self.y

        if today_m == 2:
            # February has special cases for the end of the month
            if today_d == 28:
                if self.leap_year():
                    # Leap year, go to March 29
                    tomorrow_d = 29
                    tomorrow_m = 2
                    tomorrow_y = today_y
                else:
                    # Non-leap year, go to March 1
                    tomorrow_d = 1
                    tomorrow_m = 3
                    tomorrow_y = today_y
            elif today_d == 29:
                # Leap year, go to March 1
                tomorrow_d = 1
                tomorrow_m = 3
                tomorrow_y = today_y
            else:
                # Not end of the month, just increment the day
                tomorrow_d = today_d + 1
                tomorrow_m = today_m
                tomorrow_y = today_y

        elif today_m in [1, 3, 5, 7, 8, 10]:
            if today_d == 31:
                tomorrow_d = 1
                tomorrow_m = today_m + 1
                tomorrow_y = today_y
            else:
                tomorrow_d = today_d + 1
                tomorrow_m = today_m
                tomorrow_y = today_y

        elif today_m in [4, 6, 9, 11]:
            if today_d == 30:
                tomorrow_d = 1
                tomorrow_m = today_m + 1
                tomorrow_y = today_y
            else:
                tomorrow_d = today_d + 1
                tomorrow_m = today_m
                tomorrow_y = today_y

        elif today_m == 12:
            if today_d == 31:
                tomorrow_d = 1
                tomorrow_m = 1
                tomorrow_y = today_y + 1
            else:
                tomorrow_d = today_d + 1
                tomorrow_m = today_m
                tomorrow_y = today_y
        return Date(tomorrow_m, tomorrow_d, tomorrow_y)

    # Returns the Date object obtained by adding ndays to self
    def add(self, ndays):
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]

        for i in range(ndays):
            feb = 29 if self.leap_year() else 28
            if self.d < feb:
                self.d += 1
            elif self.d == feb and self.m == 2:
                self.m += 1
                self.d = 1
            elif self.d == 30 and self.m in months_30:
                self.m += 1
                self.d = 1
            elif self.d == 31 and self.m in months_31:
                if self.m == 12:
                    self.y += 1
                    self.m = 1
                    self.d = 1
                    feb = 29 if self.leap_year() else 28
                else:
                    self.m += 1
                    self.d = 1
            else:
                self.d += 1

        return Date(self.m, self.d, self.y)

    # Returns True if self is after d
    def after(self, d):
        m = d.m
        y = d.y
        d = d.d
        return self.y > y or (self.y == y and (self.m > m or (self.m == m and self.d > d)))

    # Returns True if self is same as d
    def equals(self, d):
        m = d.m
        y = d.y
        d = d.d
        return self.y == y and self.m == m and self.d == d

    # Returns True if self is before d
    def before(self, d):
        m = d.m
        y = d.y
        d = d.d
        return self.y < y or (self.y == y and (self.m < m or (self.m == m and self.d < d)))

    # Returns the number of days between self and d
    def days_between(self, d):
        # Extracting date components for self
        self_year = int(self.y)
        self_month = int(self.m)
        self_day = int(self.d)

        # Extracting date components for d
        other_year = int(d.y)
        other_month = int(d.m)
        other_day = int(d.d)

        # Adjusting months for calculation
        if self_month in [1, 2]:
            self_month_adjusted = self_month + 12
            self_year_adjusted = self_year - 1
            self_days_count = ((365 * self_year_adjusted) + (self_year_adjusted // 4) +
                               (self_year_adjusted // 100) + (self_year_adjusted // 400) + self_day +
                               (((153 * self_month_adjusted) + 8) // 5))
        else:
            self_days_count = ((365 * self_year) + (self_year // 4) + (self_year // 100) +
                               (self_year // 400) + self_day + (((153 * self_month) + 8) // 5))

        # Adjusting months for calculation
        if other_month in [1, 2]:
            other_month_adjusted = other_month + 12
            other_year_adjusted = other_year - 1
            other_days_count = ((365 * other_year_adjusted) + (other_year_adjusted // 4) +
                                (other_year_adjusted // 100) + (other_year_adjusted // 400) + other_day +
                                (((153 * other_month_adjusted) + 8) // 5))
        else:
            other_days_count = ((365 * other_year) + (other_year // 4) + (other_year // 100) +
                                (other_year // 400) + other_day + (((153 * other_month) + 8) // 5))

        # Calculating the absolute difference in days
        days_difference = math.fabs(self_days_count - other_days_count)

        return days_difference

    # Please look at part 2 of assignment for string format
    def __str__(self):
        month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                      9: "September", 10: "October", 11: "November", 12: "December"}
        return f"{self.d} {month_dict[int(self.m)]}, {self.y}"


