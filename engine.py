def calc_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m **2),2)

def calc_bmr(weight, height, age, gender):
    if gender in ['M', 'MALE']:
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calc_macros(total_kcal, weight, goal):
        if goal == '1':
            kcal = total_kcal - 300
        elif goal == '3':
            kcal = total_kcal + 300
        else:
            kcal = total_kcal

        protein = weight * 2
        fat = (kcal * 0.25) / 9
        carbs = (kcal - (protein * 4) - (fat * 9)) / 4

        return {'kcal': int(kcal), 'p': int(protein), 'f': int(fat), 'c': int(carbs)}