# sliding_puzzle_ai
To see the french version [Français](README.fr.md)
On this project we implemented the **A\* Algorithm** to solve the Sliding game use two different **Heuristic functions**.
### Usage
**Programming language:** Python 3.0 
Make sure to install **matplotlib** using this command: 
```
pip install matplotlib
```

### How it works
In the main.py you can start the initial configuration for the game simulation.
For example: 
```
s = Simulator([(3, 3),(3, 4),(4, 4)], [2, 3, 4, 5, 6])
```
* The first parameter is a list of board sizes. In the example we have 3x3 , 3x4 et 4x4.
* The second parameter represent how much random move we perform to create the inital board. Since some Sliding puzzlea are impossible to solve, we choose to generate our initial boards by moving tiles starting from  a correct configuration to make sure that our puzzle is 100% solvable.

### A* algo 
We've used two different Heuristic functions 
* **Hamming Distance** :  This heuristics returns the number of tiles that are not in their final position.
* **Manhattan Distance** :  Manhattan Distance of a tile is the distance or the number of slides/tiles away it is from it’s goal state.

to implement the algo itself we used a **priority list** implemented in heapq library.

### Result of running the simulator
* Single board size, multiple difficulties 
![](https://cdn.discordapp.com/attachments/558063744069140484/778044913304207381/unknown.png)

* multiple board sizes, single difficulty 
![](https://cdn.discordapp.com/attachments/558063744069140484/778043781307564032/unknown.png)

* multiple board sizes, multiple difficulties
![](https://media.discordapp.net/attachments/558063744069140484/778051436650823690/unknown.png)

### conclusion
All those graphs shows that always Manhattan Distance Heuristic out perform the Hamming Distance Heuristic
