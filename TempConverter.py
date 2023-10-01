def cel(x):
    return x * 9 / 5 + 32


def fah(x):
    return (x - 32) * 5 / 9


def kel(x):
    return x + 273.15


while True:
    print("Temperature converter")
    print("Celsius to Fahrenheit Type: 1")
    print("Fahrenheit to Celsius Type: 2")
    print("Celsius to Kelvin Type: 3")
    print("Exit the program Type: 4")

    user_input = input(": ")

    if user_input == "4":
         break
    elif user_input in ('1', '2','3'):
            num1 = float(input("Enter first number: "))

            if user_input == "1":
                print("Result:", cel(num1, ))
            elif user_input == "2":
                print("Result:", fah(num1, ))
            elif user_input == "3":
                print("Result:", kel(num1, ))

    else:
        print("Invalid input. Please enter a valid operation.")

