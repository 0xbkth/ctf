# Coding90

## Description
```
We are given an IP address and a port to connect to, upon connecting we are asked to invert the path of some levels.
The summary tells us that we have to deal with inverted binary search trees
```

## Solution

After many tries trying to understand what the heck was the output. It appeared that it was a pre-order list that enabled us to build the BST.
From that I tried several ways to traverse the tree to find the one that the service was expected which is a depth traversal on the right.

I put together a python script that would get the list, build the BST and print the tree with the expected format and then sends it to the service. After the 50th question we get the flag

## Results
```
level: Level 50.: [266, 2, 140, 68, 83, 87, 88, 103, 92, 109, 252, 208, 199, 162, 159, 153, 171, 199, 200, 206, 247, 232, 211, 786, 585, 292, 283, 272, 406, 300, 395, 305, 367, 334, 405, 406, 531, 431, 413, 413, 416, 445, 444, 433, 445, 507, 452, 451, 454, 489, 483, 471, 462, 479, 506, 525, 521, 581, 573, 540, 575, 584, 643, 598, 592, 601, 610, 629, 716, 682, 681, 675, 649, 692, 692, 707, 779, 721, 726, 762, 736, 743, 774, 786, 814, 789, 812, 968, 964, 861, 851, 904, 900, 877, 962, 934, 923, 942, 989, 990]
[266, 2, 140, 68, 83, 87, 88, 103, 92, 109, 252, 208, 199, 162, 159, 153, 171, 199, 200, 206, 247, 232, 211, 786, 585, 292, 283, 272, 406, 300, 395, 305, 367, 334, 405, 406, 531, 431, 413, 413, 416, 445, 444, 433, 445, 507, 452, 451, 454, 489, 483, 471, 462, 479, 506, 525, 521, 581, 573, 540, 575, 584, 643, 598, 592, 601, 610, 629, 716, 682, 681, 675, 649, 692, 692, 707, 779, 721, 726, 762, 736, 743, 774, 786, 814, 789, 812, 968, 964, 861, 851, 904, 900, 877, 962, 934, 923, 942, 989, 990]
[*] sending [266, 786, 814, 968, 989, 990, 964, 861, 904, 962, 934, 942, 923, 900, 877, 851, 789, 812, 585, 643, 716, 779, 786, 721, 726, 762, 774, 736, 743, 682, 692, 707, 692, 681, 675, 649, 598, 601, 610, 629, 592, 292, 406, 531, 581, 584, 573, 575, 540, 431, 445, 507, 525, 521, 452, 454, 489, 506, 483, 471, 479, 462, 451, 444, 445, 433, 413, 416, 413, 300, 395, 405, 406, 305, 367, 334, 283, 272, 2, 140, 252, 208, 247, 232, 211, 199, 200, 206, 162, 171, 199, 159, 153, 68, 83, 87, 88, 103, 109, 92]
reponse: 
Yay, that's right!

IW{10000101010101TR33}
```