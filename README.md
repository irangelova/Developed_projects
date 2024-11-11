## **Developed projects during the Python courses and in my free time** 📈

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
