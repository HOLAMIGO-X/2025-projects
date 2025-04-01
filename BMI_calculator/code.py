def get_customer_details():
    """Function to gather customer details including age, weight, height, and any additional info."""
    print("Please provide the following details:")
    
    # Getting customer's age
    age = int(input("Enter your age (years): "))
    
    # Getting customer's weight and ensuring it's a positive value
    weight = float(input("Enter your weight (kg): "))
    while weight <= 0:
        print("Please enter a valid weight (positive number).")
        weight = float(input("Enter your weight (kg): "))
    
    # Getting customer's height and ensuring it's a positive value
    height = float(input("Enter your height (meters): "))
    while height <= 0:
        print("Please enter a valid height (positive number).")
        height = float(input("Enter your height (meters): "))
    
    # Additional customer inquiry: Getting contact info or other optional data
    contact_info = input("Enter your contact information (optional): ")
    
    # Returning customer details
    return age, weight, height, contact_info

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (meters)."""
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """Determine the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def display_customer_report(age, weight, height, contact_info, bmi, category):
    """Display the customer's BMI report and additional information."""
    print("\n--- BMI Report ---")
    print(f"Age: {age} years")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} meters")
    if contact_info:
        print(f"Contact Info: {contact_info}")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")

# Main function to drive the program
def main():
    """Main function that ties everything together for BMI calculation and customer details collection."""
    # Get customer details
    age, weight, height, contact_info = get_customer_details()
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Determine BMI category
    category = get_bmi_category(bmi)
    
    # Display the complete report
    display_customer_report(age, weight, height, contact_info, bmi, category)

if __name__ == "__main__":
    # Run the program
    main()
