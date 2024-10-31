class Movie:
    movie_count = 0

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.is_rented = False
        movie_count += 1

    def __str__(self) -> str:
        return f"{self.title}, {self.genre}"
    
    def toggle_rent_status(self):
        self.is_rented = not self.is_rented