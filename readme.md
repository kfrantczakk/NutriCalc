#NutriCalc v1.0
-

NutriCalc is dietary calculator built with Python.

It provides calculations for Body Mass Index (BMI), Total Daily Energy Expenditure (TDEE) and macronutrient distribution based on user-specific goals and activity levels.

#KeyFeatures
-
- **Multilingual Support**: Fully localized for **English** and **Polish**.
- **Standardized PAL**: Uses a fixed Physical Activity Level (PAL) of **1.4** (most common baseline) for consistent TDEE results
- **Goal Selection**: Supports **Cutting**, **Maintenance** and **Bulking**
- **Macro Distribution**

#ProjectArchitecture
-

The code is divided into three main modules for better maintainability:
- `main.py`: Interface and user input flow.
- `engine.py`: Mathematical logic and nutritional formulas.
- `languages.py`: Internationalization

#FutureRoadmap:
-
-[ ] **Dynamic Activity Levels**: User-selectable PAL factors (1.3 - 2.2).
-[ ] **Specific Weight Goals**: Option to set target weight gain/loss per week
-[ ] **Expanded Localization**: Support for German, Spanish and French.
-[ ] **Data Export**: Save results to a `.txt` or `.pdf` file.

#QuickStart
- 
1. Clone `git clone https://github.com/kfrantczakk/NutriCalc.git`
2. Run `python main.py`
