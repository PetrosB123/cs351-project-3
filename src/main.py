from MovieDatabase import MovieNode, MovieTree, main_menu
from RedBlackTree import RedBlackTree

db = MovieTree()

with open("movie_list.txt", "r", encoding="utf-8", errors="ignore") as f:
    
    for line in f:
        title, year, rating, genre, user_notes = line.strip().split(",")
        year = int(year)
        rating = float(rating)
        db.insert(title, year, rating, genre, user_notes)

main_menu(db)