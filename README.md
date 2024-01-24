# DateArithmetic Project

This project implements a Date class in Python and utilizes it to process celebrity information from an input file, calculating and displaying relevant details such as the day of the week for date of birth (DOB), date of death (DOD), and the number of days alive. The program also handles error checking for invalid date entries.

## Files

1. **Date.py**: Contains the implementation of the `Date` class, which includes methods for date arithmetic, determining the day of the week, and other date-related operations.

2. **DateArithmetic.py**: The main program that reads celebrity information from an input file, processes the data using the `Date` class, and produces a formatted listing sorted by the number of days alive.

## Input File Format (p1.dat)

The input file should contain lines with the following format:

- `<FirstName>`: First name of the celebrity.
- `<LastName>`: Last name of the celebrity.
- `<DOB>`: Date of birth in the format MM/DD/YYYY.
- `<DOD>`: Date of death (if applicable) in the format MM/DD/YYYY. If the celebrity is alive, this field is left blank.

## Sample Run

A sample run is included in the project, showcasing the program's output sorted by the number of days alive. The program also identifies and discards entries with data entry errors, such as a date of birth after the date of death.

## How to Run

To run the program, execute the following command in the terminal:
```bash

### Note
The program uses the Date class methods to perform date calculations and formatting.
Data entry errors are flagged, and the corresponding entries are discarded from further calculations.
