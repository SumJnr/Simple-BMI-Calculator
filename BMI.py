def calculate_bmi(weight, height_cm):
    try:
        # Convert height to meters
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main Program Execution
print("--- Simple BMI Calculator ---")
w = float(input("Enter weight in kg: "))
h = float(input("Enter height in cm: "))

result = calculate_bmi(w, h)
if result:
    print(f"Your BMI is: {result}")
    print(f"Health Category: {get_category(result)}")
else:
    print("Invalid input. Height cannot be zero.")

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def calculate_bmr(weight, height_cm, age, gender):
    # Mifflin-St Jeor Equation
    if gender.lower() == 'male':
        return round(10 * weight + 6.25 * height_cm - 5 * age + 5, 2)
    else:
        return round(10 * weight + 6.25 * height_cm - 5 * age - 161, 2)

def calculate_tdee(bmr, activity_level):
    # Activity multipliers
    multipliers = {
        "1": 1.2,    # Sedentary
        "2": 1.375,  # Lightly active
        "3": 1.55,   # Moderately active
        "4": 1.725,  # Very active
        "5": 1.9     # Extra active
    }
    return round(bmr * multipliers.get(activity_level, 1.2), 2)

def main():
    print("--- Advanced Health & BMI Calculator ---")
    
    # Inputs
    w = float(input("Weight (kg): "))
    h = float(input("Height (cm): "))
    a = int(input("Age: "))
    g = input("Gender (male/female): ")
    
    print("\nSelect Activity Level:")
    print("1. Sedentary | 2. Light | 3. Moderate | 4. High | 5. Extreme")
    act = input("Choice (1-5): ")

    # Calculations
    bmi = calculate_bmi(w, h)
    bmr = calculate_bmr(w, h, a, g)
    tdee = calculate_tdee(bmr, act)

    # Output
    print("-" * 30)
    print(f"RESULTS:")
    print(f"BMI: {bmi}")
    print(f"BMR: {bmr} calories/day (Base metabolism)")
    print(f"TDEE: {tdee} calories/day (To maintain weight)")
    print("-" * 30)

if __name__ == "__main__":
    main()