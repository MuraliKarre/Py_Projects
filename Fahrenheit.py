s = int(input("Enter the Fahrenheit value: "))


def convert(s):
    f = float(s)
    c = (f - 32) * 5 / 9
    return c


print("Converted value of Fahrenheit to Celsius: " + str(convert(s)))
