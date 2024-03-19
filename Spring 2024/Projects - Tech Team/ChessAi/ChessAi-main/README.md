# ChessAi
This is an Ai to play chess. This Ai was trained on a CNN architecture using this dataset: https://www.kaggle.com/datasets/ronakbadhe/chess-evaluations. It then uses the MinMax algorithm to select the best move.

This video was a big inspiration for the creation of this project: https://www.youtube.com/watch?v=ffzvhe97J4Q. I watched/read a lot of other materials during this project, but this one was the largest resource.

This model typically takes ~1 min to make a move at depth 3. In the future, I intend to optimize this by implementing the Alpha-Beta pruning algorithm in place of the MinMax algorthim, and implement move-ordering to save even more time. Perhaps in the future I will rewrite this code in C to make it even faster. 
