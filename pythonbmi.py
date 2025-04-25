def calculate_bmi(weight_kg, height_m):
    """Calculates BMI given weight in kilograms and height in meters."""
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """Interprets BMI value and returns the corresponding category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
