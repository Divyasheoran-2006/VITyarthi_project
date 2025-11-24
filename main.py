from numpy import array

rates = array([
    [1,     0.012, 0.011, 0.0097,0.018, 0.016, 1.78, 0.087, 0.016, 0.011, 0.044],  
    [83,    1,     0.93,  0.81,  1.56,  1.36, 147.5, 7.22,  1.34,  0.91,  3.67 ],
    [90,    1.07,  1,     0.87,  1.68,  1.47, 158,   7.75,  1.43,  0.96,  3.86 ],
    [103,   1.23,  1.15,  1,     1.93,  1.70, 182,   8.92,  1.64,  1.11,  4.47 ],
    [56,    0.64,  0.59,  0.52,  1,     0.88, 94.3,  4.62,  0.85,  0.58,  2.33 ],
    [62,    0.74,  0.68,  0.59,  1.13,  1,    107.2, 5.15,  0.95,  0.65,  2.59 ],
    [0.56,  0.0068,0.0063,0.0055,0.0106,0.0093,1,    0.048, 0.0088,0.006, 0.024],
    [11.45, 0.138, 0.129, 0.112, 0.216, 0.194,20.9,  1,     0.185, 0.124, 0.50 ],
    [62,    0.75,  0.70,  0.61,  1.18,  1.03, 110,   5.40,  1,     0.69,  2.75 ],  
    [91,    1.10,  1.04,  0.90,  1.73,  1.53, 164,   8.0,   1.45,  1,     4.00 ],  
    [22.5,  0.27,  0.25,  0.22,  0.42,  0.37, 40.7,  2.0,   0.36,  0.25,  1    ]   
])

currencies = [
    "INR", "USD", "EUR", "GBP", "AUD", "CAD", 
    "JPY", "CNY", "SGD", "CHF", "AED"
]

def conversion(amount, From, to):
    a = currencies.index(From)
    b = currencies.index(to)
    c = amount * rates[a][b]
    return c

print("Available Currencies: INR, USD, EUR, GBP, AUD, CAD, JPY, CNY, SGD, CHF, AED")

From = input("CONVERT FROM: ").upper()
to   = input("CONVERT TO: ").upper()

amt = float(input("Enter amount: "))

if amt >= 0:
    r = conversion(amt, From, to)
    print(f"{amt} {From} = {r} {to}")
else:
    print("Amount cannot be negative.")