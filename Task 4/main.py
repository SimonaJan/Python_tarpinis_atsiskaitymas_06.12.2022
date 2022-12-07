# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
    
    def wasExpensive(self):
        print(bool(self.budget > 100000000))
        
    def __str__(self): 
        return f"movie title: {self.title}, movie director: {self.director}, movie budget: USD {self.budget}" 
        

movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 25000000)
movie2 = Movie('The Dark Knight', "Christopher Nolan", 185000000)

movie1.wasExpensive()
movie2.wasExpensive()

print(movie1)
print(movie2)