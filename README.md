## **Developed projects during the Python courses and in my free time** 📈

In this repository I would like to share the projects I developed during the Python courses I took place in and in my free time

### 1. Game of rock🪨, paper📄, scissors✂️

🚀 The goal of the project was to develop a two-player game of rock, paper, schissors where a player plays against the computer. Each player choose simultaneously one of three possible options - rock, paper or scissors. The outcome of the game is then defined according to following rules:
- Paper beats rock (the paper covers the rock)
- Rock beats scissors (the scissors get broken by the rock)
- Scissors beat paper (the paper gets cut by the scissors)

The winner is the player whose choice beats the choice of the opponent. In case both players chose the same option (e.g., "paper"), the game outcome is "draw".

⚙️ The solution consists of several steps:
- Player inputs their choice (rock, paper or scissors). If player input invalid text an error is raised
- With the library "random" and the "randint" method the computer makes a random choice
- After each round the result (win, loss or draw) is evaluated and printed according to the following table: <!--![image](https://github.com/user-attachments/assets/be36617d-7c00-48fc-92b0-de5537077f7a) -->
- After printing the outcome of the round the player is asked wheter they want to play another one
- If the player wants to continue the game they input "yes". Otherwise they input "no" and statistics of the game (number of won, lost and draw rounds) are printed
  
  ![Screenshot 2024-09-28 235741](https://github.com/user-attachments/assets/8599fd35-1c01-4399-ba6f-06efb6f8a6e4)
  
⏯️ Live demo of the code:

 [<img alt="Play Button" src="https://github.com/user-attachments/assets/458c9ed7-0521-4f88-9eef-cbd555bb7511" width="100" height="50"/>](https://replit.com/@ivetar/RockPaperScissorsbyIveta)

### 2. Interactive data type operations ➕➖✖️➗

🚀 The goal of the project was to develop a program letting users choose a data type and present the result ofoperations with it. User can choose on of following data types:
- Strings
- Numbers
- Booleans
- Additional data types lists, tuples, dictionaries

⚙️ The solution consists of several steps:
1. If choice is string, completed operations are string variable declaration, extraction of substring, conversion of a string in uppercase, replacement of word in a string. After the opertaions are completed the results are printed.
2. If choice is number, user is asked to enter two float numbers. The operations addition, subtraction, multiplication, and division are performed and the results are printed.
3. If choice is boolean, two boolean variables are declared. Afterwards logical operations AND, OR and NOT are performed and the results are printed.
4. If choice is additional data types:
  - A list with mixed data types is created. New element is appended to the list and the fourt element of the list is accessed and printed.
  - A tuple with mixed data types is created. The length of the tuple is printed and error handling from modification of the tuple is printed.
  - A dictionary with key-value pairs is created. The value for one of the keys is accessed and printed. Afterwards new key-value pair is added to the dictionary and the update is printed.

Screenshot of the programm working:

  ![Screenshot_program2](https://github.com/user-attachments/assets/e7b34985-2276-40cf-8fce-0e549a671da4)
