import csv

print('x')

movies = [["Top Gun", "Risky Business", "Minority Report"],
["Titanic", "The Revenant", "Incption"], ["Training Day", "Man Fire", "Flight"]]

with open ('movies.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for movie_list in movies:
        spamwriter.writerow(movie_list)

         
