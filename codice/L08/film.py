class Film:
    def __init__(self, title, director, year, genre, rating):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director}, Genre: {self.genre}, Rating: {self.rating}"
    
    def toListItem(self):
        return f"<li>{self.title}</li>"
    
    def toTableRow(self):
        return f"<tr><td>{self.title}</td><td>{self.year}</td><td>{self.director}</td><td>{self.genre}</td><td>{self.rating}</td></tr>"