class Movie:
    def __init__(self):
        self.movies = []
    def add_movie(self,title, genre, director,year): 
        id = len(self.movies)+1
        one_movie = {"title":title, "genre":genre,"director":director,"year":year, "id":id}
        add = self.movies.append(one_movie)
        print(add)

    def remove_movie(self,title):
        for element in self.movies:
            if(element.title == title):
                self.movies.remove(element)
        print("Movie is deleted succefully")
    def  movies_director(self, director):
        filteredList = []
        for element in self.movies:
            if(element.director == director):
                filteredList.append(element)
        print("The movies by {director}")  
    def display(self):
        print(self.movies)        

