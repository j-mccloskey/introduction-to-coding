movies = {}

movies['fight club'] = ['brad pitt', 'ed norton']
movies['die hard'] = ['bruce willis', 'alan rickman']
movies['step brothers'] = ['will ferrell', 'john c reilly']

movie_title = raw_input('Enter movie to search for: ').lower()

if movie_title in movies:
    print 'The main actors are: %s' % ' & '.join(movies[movie_title])
else:
    print "Sorry that's not in our list!"
