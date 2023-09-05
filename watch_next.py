import spacy
nlp = spacy.load('en_core_web_md')

def movie(description):

    movies = open('movies.txt', 'r')
    # create a list that will store the movie list from the txt file into title and description
    split_list = []

    # split movies into title and description to be stored in list:
    for i in movies:
        split_list.append(i.split(':'))

    # get number of movies in text file
    count = len(split_list)
    # now create a list to store the similarity values
    similarity_list = []

    model_sentence = nlp(description)

    # iterate through the movies in the text file
    for i in range(0, count):
        # check similarity between movie descriptions with most recently watched movie (Planet Hulk description)
        similarity_list.append(nlp(split_list[i][1]).similarity(model_sentence))

    # get the max similarity value
    max_similarity = max(similarity_list)
    # then get index of highest similarity value
    max_similarity_index = similarity_list.index(max_similarity)

    # return most similar movie from start
    return split_list[max_similarity_index][0]

# movie description to compare text file with
planet_hulk_description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

# finally, call on function that provides the next movie description most similar with watched movie
print('Next movie recommendation for you: ' + movie(planet_hulk_description))