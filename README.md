Currency Converter

This is a simple currency converter program created using Python.
The main idea of this project is to take an amount in one currency and convert it into another.
It is built using only the basic programming concepts taught in class.

1. Project Overview

This program allows the user to:
-Enter an amount of money to convert
-Choose the currency to convert from
-Choose the currency to convert to
-Instantly see the converted result

2. Features
-Supports 11 currencies: INR, USD, EUR, GBP, AUD, CAD, JPY, CNY, SGD, CHF, AED
-Uses a NumPy matrix for all conversions
-If the user enters a wrong currency code, the program stops and shows an error
-Negative or invalid amounts are not allowed

3. Technologies Used
-Python 
-Basic programming concepts:
	-functions 
	-loops 
	-conditionals 
	-arrays

4. How It Works
-The user selects the two currencies for conversion
-The program picks the correct exchange rate using NumPy indexing
-The entered amount is multiplied by the exchange rate
-The converted value is displayed on the terminal

5. How to Run This Program

Follow these steps:

1. Install Python
2. Install NumPy
3. Save the Program
4. Run the Program
	Open terminal/cmd where the file is saved and type:
		python currency_converter.py

	1. The program will start and ask you:
	2. Which currency you want to convert from
	3. Which currency you want to convert to
	4. The amount you want to convert

Available Currencies: INR, EUR, USD, GBP, AUD, CAD, JPY, CNY, SGD, CHF, AED
CONVERT FROM: USD
CONVERT TO: INR
Enter amount: 1
1 USD = 83 INR

6. Limitations
-Currency exchange rates are fixed and not updated automatically
-No graphical user interface
-Only 11 currencies are supported

7. Future Improvements
-Add real-time exchange rates using an API
-Include more currency