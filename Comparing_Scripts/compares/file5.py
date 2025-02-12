def celsius_to_fahrenheit(c):
    # Formula for converting Celsius to Fahrenheit
    f = (c * 9 / 5) + 32
    return f

def fahrenheit_to_celsius(f):
    # Formula for converting Fahrenheit to Celsius
    c = (f - 32) * (5 / 9)
    return c

def menu():
    # Display the menu options for the user
    print("\n--- Temperature Conversion ---")
    print("[1] Celsius to Fahrenheit")
    print("[2] Fahrenheit to Celsius")
    print("[3] Exit")

def main():
    while True:
        menu()
        user_input = input("> Enter your choice: ")
        
        if user_input == "1":
            c_temp = float(input("> Enter temperature in Celsius: "))
            f_temp = celsius_to_fahrenheit(c_temp)
            print(f"> {c_temp:.1f}°C is equivalent to {f_temp:.1f}°F.")
        
        elif user_input == "2":
            f_temp = float(input("> Enter temperature in Fahrenheit: "))
            c_temp = fahrenheit_to_celsius(f_temp)
            print(f"> {f_temp:.1f}°F is equivalent to {c_temp:.1f}°C.")
        
        elif user_input == "3":
            print("> Exiting program. Goodbye!")
            break
        
        else:
            print("> Invalid input! Please select a valid option.")

main()
