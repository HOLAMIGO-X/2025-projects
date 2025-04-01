def get_customer_details():
    """Function to gather customer details including age, weight, height, gender, and activity level."""
    print("Please provide the following details:")
    
    # Getting customer's age
    age = int(input("Enter your age (years): "))
    
    # Getting customer's weight and ensuring it's a positive value
    weight = float(input("Enter your weight (kg): "))
    while weight <= 0:
        print("Please enter a valid weight (positive number).")
        weight = float(input("Enter your weight (kg): "))
    
    # Getting customer's height and ensuring it's a positive value
    height = float(input("Enter your height (cm): "))  # Height in cm for BMR calculation
    while height <= 0:
        print("Please enter a valid height (positive number).")
        height = float(input("Enter your height (cm): "))
    
    # Getting customer's gender
    gender = input("Enter your gender (M/F): ").strip().upper()
    while gender not in ['M', 'F']:
        print("Please enter a valid gender (M for Male, F for Female).")
        gender = input("Enter your gender (M/F): ").strip().upper()
    
    # Getting activity level (optional, for TDEE calculation)
    activity_level = input("Enter your activity level (Sedentary, Light, Moderate, Active, Very Active): ").strip().lower()
    while activity_level not in ['sedentary', 'light', 'moderate', 'active', 'very active']:
        print("Please enter a valid activity level (Sedentary, Light, Moderate, Active, Very Active).")
        activity_level = input("Enter your activity level (Sedentary, Light, Moderate, Active, Very Active): ").strip().lower()
    
    # Returning customer details
    return age, weight, height, gender, activity_level

def calculate_bmr(age, weight, height, gender):
    """Calculate BMR using the Mifflin-St Jeor equation."""
    if gender == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:  # For Female
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

def get_tdee(bmr, activity_level):
    """Calculate TDEE based on BMR and activity level."""
    activity_factors = {
        'sedentary': 1.2,    # little to no exercise
        'light': 1.375,      # light exercise (1-3 days/week)
        'moderate': 1.55,    # moderate exercise (3-5 days/week)
        'active': 1.725,     # intense exercise (6-7 days a week)
        'very active': 1.9   # very intense exercise (twice per day, extra heavy workouts)
    }
    
    tdee = bmr * activity_factors[activity_level]
    return tdee

def display_customer_report(age, weight, height, gender, activity_level, bmr, tdee):
    """Display the customer's BMR and TDEE report."""
    print("\n--- BMR and TDEE Report ---")
    print(f"Age: {age} years")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} cm")
    print(f"Gender: {'Male' if gender == 'M' else 'Female'}")
    print(f"Activity Level: {activity_level.capitalize()}")
    print(f"Your Basal Metabolic Rate (BMR) is: {bmr:.2f} kcal/day")
    print(f"Your Total Daily Energy Expenditure (TDEE) is: {tdee:.2f} kcal/day")

# Main function to drive the program
def main():
    """Main function that ties everything together for BMR and TDEE calculation and customer details collection."""
    # Get customer details
    age, weight, height, gender, activity_level = get_customer_details()
    
    # Calculate BMR
    bmr = calculate_bmr(age, weight, height, gender)
    
    # Calculate TDEE
    tdee = get_tdee(bmr, activity_level)
    
    # Display the complete report
    display_customer_report(age, weight, height, gender, activity_level, bmr, tdee)

if __name__ == "__main__":
    # Run the program
    main()

