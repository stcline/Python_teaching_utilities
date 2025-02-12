def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def menu():
    print("\n=== Temperature Converter ===")
    print("[1] Convert Celsius to Fahrenheit")
    print("[2] Convert Fahrenheit to Celsius")
    print("[3] Quit")

def main():
    running = True
    while running:
        menu()
        option = input("Select an option: ")
        if option == '1':
            temp = float(input("Enter Celsius temperature: "))
            print(f"{temp}°C equals {celsius_to_fahrenheit(temp):.2f}°F")
        elif option == '2':
            temp = float(input("Enter Fahrenheit temperature: "))
            print(f"{temp}°F equals {fahrenheit_to_celsius(temp):.2f}°C")
        elif option == '3':
            print("Thank you for using the converter!")
            running = False
        else:
            print("Invalid input, please choose a valid option.")

main()
