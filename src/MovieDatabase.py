from RedBlackTree import RedBlackTree, Node
from typing import Optional, cast, Any
import os


class MovieNode(Node):
    def __init__(self, parent, leftChild, rightChild, title: str, nil, year: int, rating: float, genre: str, user_notes: str = "") -> None:
        self.color: str = "RED"
        self.parent: MovieNode = parent
        self.leftChild: MovieNode = leftChild
        self.rightChild: MovieNode = rightChild
        self.nil = nil

        self.value: str = title
        self.year: int = year
        self.rating: float = rating
        self.genre: str = genre
        self.user_notes: str = user_notes

    def movie_info(self) -> None:
        if self.user_notes == "":
            print(f"Title: {self.value}, Year: {self.year}, Rating: {self.rating}, Genre: {self.genre}")
        else:
            print(f"Title: {self.value}, Year: {self.year}, Rating: {self.rating}, Genre: {self.genre}, User Notes: {self.user_notes}")


class YearTree(RedBlackTree):
    def __init__(self) -> None:
        self.nil: MovieNode = MovieNode(None, None, None, "", None, 0, 0, "")
        self.nil.leftChild = self.nil
        self.nil.rightChild = self.nil
        self.nil.parent = self.nil
        self.nil.color = "BLACK"
        self.nil.nil = self.nil
        self.root: MovieNode = self.nil
    
    def insert(self, title: str, year: int, rating: float, genre: str, user_notes: str = "") -> None:
        newNode = MovieNode(self.nil, self.nil, self.nil, title, self.nil, year, rating, genre)
        if self.root == self.nil:
            self.root = newNode
        else:
            node = self.root
            parent = self.root
            while node != self.nil:
                parent = node
                if year < node.year:
                    node = node.leftChild
                else:
                    node = node.rightChild
            newNode.parent = parent
            if newNode.year < parent.year:
                parent.leftChild = newNode
            else:
                parent.rightChild = newNode

        # Insertion fixups
        while newNode.parent.color == "RED":
            if newNode.parent == newNode.grandparent().leftChild:
                nodeX = newNode.grandparent().rightChild
                if nodeX.color == "RED":
                    newNode.parent.color = "BLACK"
                    nodeX.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    newNode = newNode.grandparent()
                else: 
                    if newNode == newNode.parent.rightChild:
                        newNode = newNode.parent
                        self.left_rotate(newNode)
                    newNode.parent.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    self.right_rotate(newNode.grandparent())
            else:
                nodeX = newNode.grandparent().leftChild
                if nodeX.color == "RED":
                    newNode.parent.color = "BLACK"
                    nodeX.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    newNode = newNode.grandparent()
                else: 
                    if newNode == newNode.parent.leftChild:
                        newNode = newNode.parent
                        self.right_rotate(newNode)
                    newNode.parent.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    self.left_rotate(newNode.grandparent())
            if newNode == self.root:
                break
        self.root.color = "BLACK"

    # Searching by year range
    def search(self, year_start: int, year_end: int) -> None:
        def list_out(node: MovieNode, nil):
            if node == nil:
                return
            list_out(node.leftChild, nil)
            if node.year <= year_end and node.year >= year_start:
                node.movie_info()
            list_out(node.rightChild, nil)
        list_out(self.root, self.nil)
            


class MovieTree(RedBlackTree):
    def __init__(self) -> None:
        self.nil: MovieNode = MovieNode(None, None, None, "", None, 0, 0, "")
        self.nil.leftChild = self.nil
        self.nil.rightChild = self.nil
        self.nil.parent = self.nil
        self.nil.color = "BLACK"
        self.nil.nil = self.nil
        self.root: MovieNode = self.nil
        self.year_tree = YearTree()

    def insert(self, title: str, year: int, rating: float, genre: str, user_notes: str = "") -> None:
        newNode = MovieNode(self.nil, self.nil, self.nil, title, self.nil, year, rating, genre, user_notes)
        self.year_tree.insert(title, year, rating, genre)
        if self.root == self.nil:
            self.root = newNode
        else:
            node: MovieNode = self.root
            parent = self.root
            while node != self.nil:
                parent = node
                if title < node.value:
                    node = node.leftChild
                else:
                    node = node.rightChild
            newNode.parent = parent
            if newNode.value < parent.value:
                parent.leftChild = newNode
            else:
                parent.rightChild = newNode

        # Insertion fixups
        while newNode.parent.color == "RED":
            if newNode.parent == newNode.grandparent().leftChild:
                nodeX = newNode.grandparent().rightChild
                if nodeX.color == "RED":
                    newNode.parent.color = "BLACK"
                    nodeX.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    newNode = newNode.grandparent()
                else: 
                    if newNode == newNode.parent.rightChild:
                        newNode = newNode.parent
                        self.left_rotate(newNode)
                    newNode.parent.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    self.right_rotate(newNode.grandparent())
            else:
                nodeX = newNode.grandparent().leftChild
                if nodeX.color == "RED":
                    newNode.parent.color = "BLACK"
                    nodeX.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    newNode = newNode.grandparent()
                else: 
                    if newNode == newNode.parent.leftChild:
                        newNode = newNode.parent
                        self.right_rotate(newNode)
                    newNode.parent.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    self.left_rotate(newNode.grandparent())
            if newNode == self.root:
                break
        self.root.color = "BLACK"

    def search(self, title: str) -> MovieNode:
        node = self.root
        while node != self.nil and title != node.value:
            if title < node.value:
                node = node.leftChild
            else:
                node = node.rightChild
        return node
    
    # Print out every movie alphabetically
    def list_out(self, node: MovieNode):
        if node == self.nil:
            return
        self.list_out(node.leftChild)
        node.movie_info()
        self.list_out(node.rightChild)

    # Add every movie to a list alphabetically
    def export(self) -> list[MovieNode]:
        node = self.root
        nodes = []
        def in_order_traverse(node):
            if node == self.nil:
                return
            in_order_traverse(node.leftChild)
            nodes.append(node)
            in_order_traverse(node.rightChild)
        in_order_traverse(node)
        return nodes
    
    # Find every movie with a keyword, alphabetically and return it as a list
    def search_keyword(self, keyword) -> list[MovieNode]:
        movie_list = []
        def search(node: MovieNode):
            if node == self.nil:
                return
            search(node.leftChild)
            if keyword.strip().lower() in node.value.strip().lower():
                movie_list.append(node)
            search(node.rightChild)
        search(self.root)
        return movie_list



def main_menu(db: MovieTree):
    watched_list = MovieTree()
    watchlist = MovieTree()
    while True:
        print("\nMovie Catalog Menu:")
        print("1. List all movies")
        print("2. Search movie by title")
        print("3. Search movie by keyword")
        print("4. Search movies by year")
        print("5. Mark a movie as watched")
        print("6. Add movie to your want to watch list")
        print("7. View your watched movies list")
        print("8. View your want to watch list")
        print("9. Export your lists")
        print("10. Import a watched list")
        print("11. Import a want to watch list")
        print("12. View watched list as red black tree")
        print("13. View want to watch list as red black tree")
        print("14. View full database as red black tree (BAD IDEA)")
        print("15. Exit")

        choice = input("Enter choice: ")
        match(choice):
            case "1":
                db.list_out(db.root)
            case "2":
                search_choice = input("What movie do you want to search for? (Input title): ").strip()
                print("\n")
                searched_movie = db.search(search_choice)
                if searched_movie == db.nil:
                    print(f"Could not find the movie '{search_choice}'")
                else:
                    searched_movie.movie_info()
            case "3":
                keyword = input("What keyword do you want to search for? ")
                print("\n")
                keyword_list = db.search_keyword(keyword)
                for movie in keyword_list:
                    movie.movie_info()
            case "4":
                while True:
                    try:
                        year_start = int(input("What year do you want to start from?: "))
                        year_end = int(input("What year do you want to end your search?: "))
                        print("\n")
                        break
                    except:
                        pass
                db.year_tree.search(year_start, year_end)
            case "5":
                watched_movie = input("What movie do you want to mark as watched?: ")
                print("\n")
                searched_movie = db.search(watched_movie)
                if searched_movie == db.nil:
                    print(f"Could not find the movie '{watched_movie}'")
                else:
                    while True:
                        user_rating = (input("What score (out of 10) do you rate this movie? (decimals are fine): "))
                        try: 
                            user_rating = float(user_rating)
                            break
                        except:
                            pass
                    user_notes = input("Write some notes or a review of the movie: ")
                    watched_list.insert(searched_movie.value, searched_movie.year, user_rating, searched_movie.genre, user_notes)
            case "6":
                want_to_watch_movie = input("What movie do you want to mark as want to watch?: ")
                print("\n")
                searched_movie = db.search(want_to_watch_movie)
                if searched_movie == db.nil:
                    print(f"Could not find the movie '{want_to_watch_movie}'")
                else:
                    user_notes = input("Why do you want to watch this movie?: ")
                    watchlist.insert(searched_movie.value, searched_movie.year, searched_movie.rating, searched_movie.genre, user_notes)
            case "7":
                watched_list.list_out(watched_list.root)
            case "8":
                watchlist.list_out(watchlist.root)
            case "9":
                counter = 1
                filename = "watched_list.txt"
                while os.path.exists(filename):
                    filename = f"watched_list ({counter}).txt"
                    counter += 1

                with open(filename, "x") as f:
                    export_list = watched_list.export()
                    for movie in export_list:
                        f.write(f"{movie.value},{movie.year},{movie.rating},{movie.genre},{movie.user_notes}\n")
                
                counter = 1
                filename = "watchlist.txt"
                while os.path.exists(filename):
                    filename = f"watchlist ({counter}).txt"
                    counter += 1

                with open(filename, "x") as f:
                    export_list = watchlist.export()
                    for movie in export_list:
                        f.write(f"{movie.value},{movie.year},{movie.rating},{movie.genre},{movie.user_notes}\n")
            case "10":
                fn = input("What is the filename of the list you want to Import? (format: list.txt): ")
                with open(fn, "r", encoding="utf-8", errors="ignore") as f:
        
                    for line in f:
                        title, year, rating, genre, user_notes = line.strip().split(",")
                        year = int(year)
                        rating = float(rating)
                        watched_list.insert(title, year, rating, genre, user_notes)
            case "11":
                fn = input("What is the filename of the list you want to Import? (format: list.txt): ")
                with open(fn, "r", encoding="utf-8", errors="ignore") as f:
        
                    for line in f:
                        title, year, rating, genre, user_notes = line.strip().split(",")
                        year = int(year)
                        rating = float(rating)
                        watchlist.insert(title, year, rating, genre, user_notes)
            case "12":
                watched_list.print_tree()
            case "13":
                watchlist.print_tree()
            case "14":
                db.print_tree()
            case "15W":
                if input("WARNING: THIS WILL WIPE ALL PROGRESS/CREATED LISTS. EXPORT BEFORE EXITING TO SAVE ANYTHING. ARE YOU SURE YOU WANT TO PROCEED?").strip().lower() in ["y", "yes"]:
                    exit()
        input("Press 'Enter' to continue: ")
