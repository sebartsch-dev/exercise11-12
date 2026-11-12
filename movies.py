def read_movies(filename):
    ratings={}
    titles={}
    list_of_everything=[]
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            list_words=line.strip().split(",")
            titles[int(list_words[0])]=list_words[1]
            ratings[int(list_words[0])]=list_words[4]
    return titles, ratings


def get_movie_title(movie_id, titles):
    if movie_id in titles:
        return titles.get(movie_id)
    else:
        return "Movie not found"
    


def get_highly_rated_movies(min_rating, titles, ratings):
    high_rated_titles=[]
    for i in range(1, len(ratings)+1):
        if float(ratings[i])>=float(min_rating):
            high_rated_titles.append(titles[i])
    return high_rated_titles


def main():
    titles, ratings = read_movies("movies.txt")

    print(get_movie_title(1, titles))
    print(get_movie_title(100, titles))

    print(get_highly_rated_movies(8.4, titles, ratings))


main()