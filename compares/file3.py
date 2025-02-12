def celsius_to_fahrenheit(celsius):
    return round((celsius * (9 / 5)) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * (5 / 9), 2)

def menu():
    print("\nTemperature Conversion Program")
    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")
    print("0 - Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C is equal to {f}°F.")
        
        elif choice == "2":
            f = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F is equal to {c}°C.")
        
        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid selection! Please try again.")

main()
