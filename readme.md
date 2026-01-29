#NutriCalc v1.1
-

NutriCalc is dietary calculator built with Python.

It provides calculations for Body Mass Index (BMI), Total Daily Energy Expenditure (TDEE) and macronutrient distribution based on user-specific goals and activity levels.

#KeyFeatures
-
- **Multilingual Support**: Fully localized for **English**, **Polish** and **Deutsch**.
- **Dynamic PAL**: User can choose from 4 activity levels (1.2-1.8) with descriptive guidance.
- **Goal Selection**: Supports **Cutting**, **Maintenance** and **Bulking**
- **Specific Weight Goals**: Ability to set a target weight change (0.5kg to 1.0kg per week) for automated calorie adjustment.
- **Macro Distribution**

#ProjectArchitecture
-

The code is divided into three main modules for better maintainability:
- `main.py`: Interface and user input flow.
- `engine.py`: Mathematical logic and nutritional formulas.
- `languages.py`: Internationalization

#FutureRoadmap:
-
-[ ] **Expanded Localization**: Support for more languages.
-[ ] **Data Export**: Save results to a `.txt` or `.pdf` file.
-[ ] **Web App**

#QuickStart
- 
1. Clone `git clone https://github.com/kfrantczakk/NutriCalc.git`
2. Run `python main.py`
