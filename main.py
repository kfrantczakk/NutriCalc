from engine import calc_bmi, calc_bmr, calc_macros
from languages import translations, available_languages

print("1. Polski / 2. English")
choice = input("Enter your choice: ")

if choice in available_languages:
    lang_code = available_languages[choice][0]
    text = translations[lang_code]
else:
    print("Invalid choice. Default language is English.")
    text = translations['en']

print(f"\n*** {text['app_name']} ***")

#Data
weight = float(input(text['input_weight']))
height = float(input(text['input_height']))
age = int(input(text['input_age']))
gender = input(text['input_gender']).upper()

#Calc
bmi = calc_bmi(weight, height)
bmr_val = calc_bmr(weight, height, age, gender)
tdee = bmr_val * 1.4

goal = input(text['input_goal'])
results = calc_macros(tdee, weight, goal)

#Results
print("\n" + "="*40)
print(f"{text['bmi']} {bmi}")
print(f"{text['kcal']} {results['kcal']} kcal")
print(f"{text['macro']} {results['p']}g, {results['c']}g, {results['f']}g)")
print("="*40)
