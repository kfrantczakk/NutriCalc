from engine import calc_bmi, calc_bmr, calc_macros
from languages import translations, available_languages

#Language
print("1. Polski / 2. English / 3.Deutsch")

choice = input("Enter your choice: ")

if choice in available_languages:
    lang_code = available_languages[choice][0]
    text = translations[lang_code]
else:
    print("Invalid choice. Default language is English.")
    text = translations['en']

print(f"\n*** {text['app_name']} ***")

#PAL
pal_map = {'1': 1.2, '2': 1.4, '3': 1.6, '4': 1.8}

#BaseDATA
weight = float(input(text['input_weight']))
height = float(input(text['input_height']))
age = int(input(text['input_age']))
gender = input(text['input_gender']).upper()

#ActivityDATA
pal_choice = input(text['input_pal'])
pal = pal_map.get(pal_choice, 1.2)

#GOAL
goal = input(text['input_goal'])
change = 0.0

if goal in ['1', '3']:
    change_input = input(text['input_change'])
    change = float(change_input.replace(',', '.'))
    change = max(0.5, min(1.0, change))

#CALC
bmi = calc_bmi(weight, height)
bmr_val = calc_bmr(weight, height, age, gender)


results = calc_macros(bmr_val, pal, weight, goal, change)

#RESULTS
print("\n" + "="*40)
print(f"{text['bmi']} {bmi}")
print(f"{text['kcal']} {results['kcal']} kcal")
print(f"{text['macro']} ({results['p']}g, {results['c']}g, {results['f']}g)")
print("="*40)