# ColorQuest

The Python project is a color guessing game that generates random RGB values and prompts users to rate colors on a scale from 0 to 10, with the program adjusting bet amounts and updating money accordingly.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 4/10](#Rating)

# About

The project is a Python-based color guessing game that generates random RGB values for colors and prompts users to rate them on a scale from 0 to 10. If the user cannot see the color, they can input -1. The program adjusts the bet amount and updates the user's money, utilizing concepts like random number generation and list manipulation.

# Features

The Python-based color guessing game features random RGB color generation, a user rating system, and a visibility option for users with color vision deficiencies. Users rate the generated colors on a scale from 0 to 10, with higher ratings indicating more visually appealing colors. The game also includes a betting system, where the bet amount may change based on user actions or color ratings. Additionally, the game allows users to manage their money by updating their funds based on their interactions. The game uses random number generation for RGB values and list manipulation for storing colors and ratings. Overall, this color guessing game combines randomness, user input, and financial management for an engaging experience.

# Imports

random

# Rating

The code generates random RGB colors, asks the user to rate them, and stores the color and rating in a 2D list. It handles incorrect user inputs by asking the user to input a valid rating and prompts the user to confirm exit. The code uses ANSI escape codes to display colored text in the terminal, providing a visual representation of the generated RGB colors. However, there are several issues with the code, including redundancy in the color comparison loop, an inefficient loop, incorrect use of global variables, confusing bet logic, inadequate comments, unclear exit handling, and hardcoded limits.
To improve the code, the code should simplify color comparison, remove the unnecessary loop, encapsulate variables, refactor the bet logic, add comments to explain the purpose of each function, loop, and conditional block, improve error handling, and allow customization of the rating system to accommodate different scales or ranges based on user requirements.
In summary, the code has several pros and cons, including functionality, error handling, and color representation. However, improvements include simplifying color comparison, removing unnecessary loops, encapsulating variables, simplifying the bet logic, adding comments, improving error handling, and creating a flexible rating system.
