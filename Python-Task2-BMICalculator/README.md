# BMI Calculator

## Project Overview
The BMI Calculator is a simple Python desktop application that calculates a person's Body Mass Index (BMI) using their weight and height. It displays the BMI value and its corresponding category.

## Objectives
- Understand basic Python programming.
- Perform mathematical calculations using Python.
- Develop a graphical user interface.
- Practice input validation and conditional statements.

## Features
- User-friendly graphical interface.
- Accepts weight in kilograms.
- Accepts height in centimetres.
- Calculates BMI automatically.
- Displays BMI to two decimal places.
- Shows the BMI category.
- Includes a reset button.
- Handles empty and invalid inputs.

## Technologies Used
- Python 3
- Tkinter
- Messagebox

## Project Structure
```text
Python-Task2-BMICalculator/
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
```

## BMI Formula
```text
BMI = Weight (kg) / Height (m)²
```
Height is converted from centimetres into metres before calculation.

## BMI Categories
| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5–24.9 | Normal Weight |
| 25–29.9 | Overweight |
| 30 or above | Obesity |

## Installation
1. Install Python 3.
2. Ensure Tkinter is available in your Python installation.
3. No third-party packages are required.

## How to Run
From this project folder, run:
```bash
python3 main.py
```

## Example
**Input:** Weight: 60 kg; Height: 165 cm  
**Output:** BMI: 22.04 — Normal Weight

## Learning Outcomes
- Understanding Python functions.
- Performing mathematical operations.
- Using conditional statements.
- Developing a GUI using Tkinter.
- Handling user inputs and errors.

## Disclaimer
BMI is a screening measure and does not independently determine a person's health condition.

## Author
GitHub: [@ashwina2026](https://github.com/ashwina2026)

## Internship
Oasis Infobyte – Python Programming Internship

## Conclusion
This project demonstrates how Python can be used to create a simple graphical application that performs calculations and displays meaningful results.
