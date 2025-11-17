def menu():
    option = input("enter '1' to view all movies, enter '2' to add a new movie, enter '3' to")
    if option == 1:
        movies = {"Black Phone 2": "10:50", "Children Of The Corn": "11:20", "The First Omen": "11:50", "The Conjuring": "12:20", "Until Dawn": "12:50"}
        print(movies)
    elif option == 2:
        print("would you like to add a new movie")
        new_movie = input("type 'y' for yes or 'n' for no")
        if new_movie == "y":
            movie_name = input("what movie would you like to add")
            movies.append(movie_name)
            print(movies)
        elif new_movie == "n":
            print("your movie list has stayed the same")
menu()