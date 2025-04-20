# Weeker - Day of Week Handler

## Description
**Weeker** is a simple Python class that allows you to create and manipulate days of the week. It accepts only valid weekday names (`Mon` to `Sun`) and provides methods to move forward or backward by any number of days.

## About
This project was completed as part of a Python programming lab from Cisco Networking Academy.

## Features
- Add or subtract any number of days
- Only valid weekdays accepted
- Custom exception for invalid days

## Usage



try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
except WeekDayError:
    print("Invalid weekday!")