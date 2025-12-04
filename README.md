# Project Title

## Description
- Red-Black Tree
- It is a Movie Database that allows the user to search for movies using various paramaters or add them to a list and give them their own rating
- I use a film rating database, my brother uses one, and he has some friends that use one so people that like films and like rating films might use this, especially if it was very fleshed out

---

## Team Members
- **Name** – Petros Blankenstein

---

## Installation & Setup

### Prerequisites
- Python 3.13+

### Setup Instructions
1. Clone the repository

### How to Run the Application
- Run ```main.py```

---

## Usage Guide
- There are two files (```title.basics.tsv.gz``` and ```title.ratings.tsv.gz```, these files are not included because they were too big and GitHub didn't like that) from iMDb's non-commercial data sets, these two sets are read in by ```movie_exporter.py```, parsed, and put into the correct format in ```movie_list.txt``` (This is all already done for you).
- ```main.py``` reads in ```movie_list.txt``` when you run it which has more than 300,000 film entries and puts them into a Red-Black Tree, sorted by title alphabetically. It also creates a second Red-Black Tree that sorts them all by release year.
- You have 15 options to select from. 
- You can create your own Red-Black Tree with movies you have watched and give them a rating out of 10 and write a little note about them or you can create a list of movies you want to watch and have a note on why you want to watch them. You can view these at any time in either list form or tree form.
- You can view the full Red-Black Tree with all 300,000 entries as a tree or alphabetical list (this takes a few seconds to print them all out and is completely useless because the terminal doesn't save that many lines). 
- You can search for a specific movie, search for movies that contain keywords, or search for all movies released within a year range.
- You can export your watchlists or import them as well from txt files

---

## Screenshots / Demos
> Include **at least 3 screenshots**.

### Screenshot 1
- Shows the results of a keyword search with the search term "Monty Python".

### Screenshot 2
- Shows the results of a year range search of all films in the database between 1900 and 1902.

### Screenshot 3
- Shows a Red-Black Tree representation of the watchlist imported from ```watchlist_example.txt```.

---

## Tree Implementation Details
- Overview: 
Self-balancing binary search tree that maintains logarithmic height through a color and structural rules; each node stores its value, color (RED or BLACK), parent, and its right and left children. Null nodes are represented by the 'nil' node which is always BLACK. The root node is always BLACK, all non nil nodes must have children, these can be nil nodes. A RED node cannot have RED children. Every path from the root to to the bottom of the tree must have the same amount of BLACK nodes. These rules keep the tree self balanced
- Key Operations:
Insert(value) - Standard binary search tree insertion. O(log n) time complexity and O(1) space complexity. New nodes start as RED, fix-up loop adjusts colors and performs rotations to restore RBT properties:
  Case 1: parent & uncle are red - recolor
  Case 2: triangle shape - rotate
  Case 3: line shape - rotate + recolor
Then the root is recolored to BLACK.

Search(value) - Typical binary search tree lookup, descends left and right depending on the value you are searching for. O(log n) time complexity and O(1) space complexity.

Remove(node) - Checks all Red-Black Tree cases:
If the node has one non-nil child, then replace with child.
If the node has two children, then replace with the in-order successor
After transplanting, if a BLACK node was removed, run full delete fix-up:
  Sibling is red - rotation + recolor
  Sibling has black children - recolor
  Sibling has at least one red child - rotation(s) + recolor
O(log n) time complexity and O(1) space complexity.

Rotations - Used by both insert and removal functions to fix up the tree. Left rotations pivot around the nodes right child and vice versa. O(1) time and space complexity.

find_min(node) - Runs down the left child of a node until it reaches the smallest node from that node. O(log n) time complexity and O(1) space complexity.

transplant(node1, node2) - Replaces node1 with node2 in the tree. O(1) time and space complexity.

print_tree() - Prints a sideways visual representation of the tree. O(n) time complexity and O(log n) space complexity.


- Any interesting or unusual implementation choices:
Uses an explicit nil node rather than representing it with "None" as some implementations do.
Node has grandparent() and sibling() methods to get the grandparents and siblings more cleanly.

---

## Evolution of the Interface
- What changed from your initial design? - I added the grandparent() and sibling() functions to make my life easier instead of writing out node.parent.parent or going through and figuring out what child the node is and getting the other child of its parent. Print_tree() was added last so I could actually visualize and make sure everything was functioning correctly. I also added some things exclusively to the MovieDatabase version such as in order traverse to get every item in the tree in order.
- Why did those changes occur? - For better readability, easier writability, visualization, or to add a specific feature to the application.
- What did you learn during the process? - Red-Black Trees are really cool and very useful. It's unbelievable how fast you can search through 300,000 items.

---

## Challenges & Solutions
- Technical or algorithmic difficulties - It's a complex algorithm but I really enjoyed learning about it and implementing it and especially creating the application.
- Bugs or design issues you encountered - Had a few bugs with things I wrote wrong in the insertion or removal fixups which caused the tree to not self-balance the way it should.
- How you solved or worked around them - I looked to some tutorials and figured out what I was doing wrong and then fixed it.

---

## Future Enhancements
- Features you would add with more time - I would add more features to the application like when you search for one movie, you get the first one it finds in the tree so movies with the same title you might not get the one that you are actually looking for and then you can't actually add it to your list. You should be able to pick which one you want. Movies in the database could be marked with a * if you've watched them or something to show you want to watch them.
- Improvements to the interface or performance - The year range searching algorithm in the application could be optimized to be O(log n).
- Additional tools or visualizations - I would love to be able to export the Red-Black Trees as a full visualization. It would be really cool to look at a tree with 300,000 nodes. I'll probably figure that out at some point just for the fun of it.