Project Statement — Currency Converter

1. Problem Statement

People deal with different currencies in daily life, especially students, travelers, and online shoppers.
Checking exchange rates and converting amounts manually can be confusing and may lead to calculation mistakes.
To make this easier, I decided to create a small Python program that can convert one currency to another quickly.

2. Scope of the Project

This project is made only with the basic concepts taught in the course.
The main focus is on:

 -Using Python functions
 -Storing exchange rates in a NumPy array
 -Converting any amount using simple indexing
 -Taking user input and showing the result clearly

The project does not include advanced features like API calls, GUI, or database storage.
It is kept simple on purpose to match the basic Python + NumPy syllabus.

3. Target Users
The program can be useful for:
 -Students who want quick currency conversion
 -Beginners learning Python and NumPy
 -Anyone who needs a simple conversion tool

4. High-Level Features
 -Currency Selection
 	The user can choose the “from” and “to” currencies.
 	Supported currencies: INR, USD, EUR, GBP, AUD, CAD, JPY, CNY, SGD, CHF, AED.

 -NumPy-Based Rate Matrix
 	All the exchange rates are stored inside a NumPy 2D array.
 	This makes the conversion fast and easy.

 -Conversion Logic
 	The program multiplies the entered amount with the correct rate from the matrix:
 	converted_amount = amount * rate[from_index][to_index]

5. Summary

This project shows how Python and NumPy can be used to build a simple currency converter.
It is easy to understand, works without the internet, and helps in practicing basic programming concepts.
The project is suitable for a beginner-level Python course and demonstrates practical use of NumPy arrays.