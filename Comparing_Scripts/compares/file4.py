def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def menu():
    options = """
Temperature Conversion Options:
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Exit Program
"""
    print(options)

def main():
    while True:
        menu()
        try:
            choice = int(input("Select an option (1-3): "))
            
            if choice == 1:
                c_temp = float(input("Enter Celsius temperature: "))
                f_temp = celsius_to_fahrenheit(c_temp)
                print(f"Result: {c_temp:.2f}°C -> {f_temp:.2f}°F")
            
            elif choice == 2:
                f_temp = float(input("Enter Fahrenheit temperature: "))
                c_temp = fahrenheit_to_celsius(f_temp)
                print(f"Result: {f_temp:.2f}°F -> {c_temp:.2f}°C")
            
            elif choice == 3:
                print("Exiting program...")
                break
            
            else:
                print("Invalid selection! Please enter a number between 1 and 3.")
        
        except ValueError:
            print("Error: Please enter a valid number.")

main()
