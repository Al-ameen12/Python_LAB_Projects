class WeekDayError(Exception):
    pass

	

class Weeker:
    #
    # Write code here.
    #
    __days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
       

    def __init__(self, day):
        # checking if {day} is part of the of the week, if not it raises an error
        if day not in Weeker.__days_of_week:
            raise WeekDayError
        self.__day = day
        
    
    def __str__(self):
        #
        # Write code here.
        #
        # this part returns the day as string
        return self.__day

    def add_days(self, n):
        #
        # Write code here.
        #
        
        current_index = Weeker.__days_of_week.index(self.__day)
        new_index = (current_index + n) % 7
        self.__day = Weeker.__days_of_week[new_index]

    def subtract_days(self, n):
        #
        # Write code here.
        #
        current_index = Weeker.__days_of_week.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = Weeker.__days_of_week[new_index]


# Testing the code
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    