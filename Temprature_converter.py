def red(text):
    return f"\033[91m{text}\033[0m"
def green(text):
    return f"\033[92m{text}\033[0m"
def blue(text):
    return f"\033[94m{text}\033[0m"
print("Enter value only in integer!\n")
Value = float(input("Enter your temprature value: "))


print("\nwhat is this value in ")
print("1.", red("Celcius"))
print("2.", green("Fahrenheit"))
print("3.", blue("Kelvin"))
unit = int(input("Enter choices from(1-3): "))
if unit == 1:
    Celcius = Value
elif unit == 2:
    Celcius = (Value - 32) *5 / 9
elif unit == 3:
    Celcius = Value - 273.15
else:
    print("Invalid Unit")
    exit()
print("\nwhat do you want to convert this value in ")
print("1.", red("Celcius"))
print("2.", green("Fahrenheit"))  
print("3.", blue("Kelvin"))
choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    print("Result: ", Celcius, red("C"))
elif choice == 2:
    print("Result: ",(Celcius * 9 /5) + 32, green("F") )
elif choice == 3:
    print("Result: ", Celcius + 273.15, blue("K") )
else:
    print("Invalid Choice.\n Please choose from 1 to 3")
    exit()