# sliding_puzzle_ai

On implémente dans ce projet **l'algorithme A\*** pour résoudre le problème du taquin, et ce en utilisant deux **fonctions heuristiques différentes**.
### Utilisation
**Language de programmation:** Python 3.0 
Il faut installer **matplotlib** en utilisant cette commande: 
```
pip install matplotlib
```

### Fonctionnement
Dans le fichier main.py, on peut modifier la configuration du jeu pour pouvoir lancer la simulation. Exemple:
```
s = Simulator([(3, 3),(3, 4),(4, 4)], [2, 3, 4, 5, 6])
```
* Le premier paramètre représente la taille de la grille. Dans cet exemple on a 3 grilles de tailles 3x3 , 3x4 et 4x4.
* Le second paramètre représente combien de mouvements aléatoires on effectue pour créer la grille initiale. Et ce car quelques grilles sont impossibles a résoudre, donc on a choisi de générer nos grilles en faisant des mouvements aléatoires sur une grille complétée (correcte), et cela pour etre sûr a 100% que notre jeu du taquin présente bel et bien une solution et peut etre résolu.

### L'algorithme A* 
On a utilisé deux différentes fonctions heuristiques: 
* **Hamming Distance** :  cette heuristique retourne le nombre de pieces se trouvant dans des emplacements incorrects.
* **Manhattan Distance** :  Manhattan Distance est la distance ou le nombre de mouvements séparant les pieces a leurs correctes emplacements.

pour implémenter l'algorithme on a utilisé une **priority queue** implémentée dans la heapq library.

### Result of running the simulator
* Une seule grille, différentes difficultés 
![](https://cdn.discordapp.com/attachments/558063744069140484/778044913304207381/unknown.png)

* plusieurs grilles de différentes tailles, Une seule difficulté 
![](https://cdn.discordapp.com/attachments/558063744069140484/778043781307564032/unknown.png)

* plusieurs grilles de différentes tailles, plusieurs difficultés
![](https://media.discordapp.net/attachments/558063744069140484/778051436650823690/unknown.png)

### conclusion
Tous ces graphes nous montrent bien que la fonction heuristique Manhattan Distance est bien plus performante que la Hamming Distance
