MENU_PROMPT = "\nEnter 'a' to add movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit :"
movies = []


def add_movie():
    title = input("Enter the movie title :")
    director = input("Enter the name of the director :")
    year = input("Enter the year of release :")

    movies.append({
        'title' : title,
        'director' : director,
        'year' : year

    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title : {movie['title']}")
    print(f"Director : {movie['director']}")
    print(f"Release_year : {movie['year']}")

def find_movies():
    search_title = input("Enter the movie title you are looking for :")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


def menu():
    selection = input(MENU_PROMPT)
    while(selection != 'q'):
        if(selection == 'a'):
            add_movie()
        elif(selection == 'l'):
            show_movies()
        elif(selection == 'f'):
            find_movies()
        else:
            print('Unknown command, please try again.')

        selection = input(MENU_PROMPT)


menu()
