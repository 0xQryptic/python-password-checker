# Python Password Strength Checker

## Description

This Python script provides a command-line interface to check the strength of a given password based on several common criteria. It offers feedback on each criterion and calculates an overall strength score, categorizing the password as "Weak," "Medium," or "Strong." The script allows users to check multiple passwords in a single session.

This project was developed as a Python learning exercise, focusing on fundamental programming concepts, function definition and refactoring, iterative development, and user interaction.

## Features

* Prompts the user for password input.
* Allows checking multiple passwords sequentially until the user types 'quit'.
* **Individual Criteria Checks:**
    * Minimum length (default is 8 characters).
    * Presence of at least one uppercase letter (A-Z).
    * Presence of at least one lowercase letter (a-z).
    * Presence of at least one digit (0-9).
    * Presence of at least one special character (from the set: `!@#$%^&*()_-+=<>?`).
* Provides "Passed" or "Failed" feedback for each individual check.
* Calculates an overall strength score out of 5 based on the criteria met.
* Categorizes the overall password strength as "Weak," "Medium," or "Strong."
* The code is organized into separate functions for each validation check for better readability and modularity.

## How to Use

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository or download the `password_checker.py` script.
3.  Navigate to the script's directory in your terminal.
4.  Run the script using the command:
    ```bash
    python password_checker.py
    ```
5.  Follow the prompts:
    * Enter a password when asked.
    * Review the feedback and the overall strength score.
    * When prompted for the next password, you can enter another password or type `quit` to exit the script.

## Code Structure Overview

The script is structured with:
* A set of functions, each responsible for a specific validation check:
    * `check_uppercase(password)`
    * `check_lowercase(password)`
    * `check_digit(password)`
    * `check_length(password, min_length=8)`
    * `check_special_char(password)`
* A main `while` loop that handles user input, calls the check functions, and manages the scoring and feedback process for each password.

## Technologies Used

* Python 3
* Standard Python built-in functions and string methods.

---
