import gzip
import csv

BASICS_FILE = "title.basics.tsv.gz"
RATINGS_FILE = "title.ratings.tsv.gz"
OUTPUT_FILE = "movie_list.txt"

ratings = {}

with gzip.open(RATINGS_FILE, "rb") as f:
    for line in f:
        try:
            decoded = line.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if decoded.startswith("tconst"):
            continue
        parts = decoded.strip().split("\t")
        if len(parts) < 2:
            continue
        ratings[parts[0]] = parts[1]

with gzip.open(BASICS_FILE, "rb") as f, open(OUTPUT_FILE, "w", encoding="utf-8") as out_f:
    for line in f:
        try:
            decoded = line.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if decoded.startswith("tconst"):
            continue
        parts = decoded.strip().split("\t")
        if len(parts) < 5:
            continue
        tconst, titleType, title, year, genres = parts[0], parts[1], parts[2], parts[5], parts[8]
        if titleType != "movie":
            continue
        if year == "\\N":
            continue
        rating = ratings.get(tconst, "")
        if rating == "":
            continue
        title = title.replace(",", "")
        genres = genres.replace("\\N", "").replace(",", " ")
        out_f.write(f"{title},{year},{rating},{genres},\n")

print(f"Export complete! File saved as {OUTPUT_FILE}")
