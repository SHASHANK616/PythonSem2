# p6 1. Scan n values in range 0-3 and print the number of times each value has occurred

n = int(input("Enter the value of n: "))
counts = {0: 0, 1: 0, 2: 0, 3: 0}
for i in range(n):
    value = int(input("Enter a value between 0 and 3: "))
    counts[value] += 1
print("Counts of each value:")
for value, count in counts.items():
    print(f"{value}: {count}")


#******************************************************************************************

# P6 2. Create a tuple to store n numeric values and find average of all values.

x = int(input("Enter the upper limit: "))

tupp = ()
for i in range(x):
    value = float(input("Enter a numeric values: "))
    tupp = tupp + (value,)
total = sum(tupp)

average = total/x

print("The average of the" ,x, "values is:", average)


#******************************************************************************************

#P6 3. WAP to input a list of scores for N students in a list data type. 
# Find the score of the runner-upand print the output.Sample Input
# N = 5Scores= 2 3 6 6 5Sample output5Note: Given list is [2, 3, 6, 6, 5].
# The maximum score is 6, second maximum is 5.
# Hence, we print 5 as the runner-up score

lst=[]
n=int(input("Enter the the upper limit:"))
print("Enter the marks of each student:")
for x in range(0,n):
    k=input()
    lst.append(k)
# k.sort()
m=sorted(lst,reverse=True)
print("Second maximum:",m[1])
     




#******************************************************************************************

# P6 4. Create a dictionary of n persons where key is name and value is city.
# a) Display all names
# b) Display all city names
# c) Display student name and city of all students.
# d) Count number of students in each city.

persons = {
    'Shashank': 'Madhubani',
    'Lucky': 'Haridwar',
    'Aridaman': 'Lucknow',
    'Gauransh': 'Delhi'
}

# Displaying all names
names = persons.keys()
print(names)


# Displaying all city names
cities = persons.values()
print(cities)

# Displaying student name and city of all students
for name, city in persons.items():
    print(name, city)

# Counting number of students in each city
from collections import defaultdict

city_count = defaultdict(int)

for city in persons.values():
    city_count[city] += 1

print(city_count)


#******************************************************************************************

# P6 5. Store details of n movies in a dictionary by taking input from the user.
# Each movie must storedetails like name, year, director name, production cost, collection made (learning) 
# & performthe following :-
# a) print all movie details
# b) display name of movies released before 2015
# c) print movies that made a profit.
# d) print movies directed by a particular director

n = int(input("Enter the number of movies: "))
movies = {}

for i in range(n):
    print(f"\nEnter the details of movie {i+1}:")
    name = input("Enter the name of the movie: ")
    year = int(input("Enter the year of release: "))
    director = input("Enter the name of the director: ")
    production_cost = int(input("Enter the production cost: "))
    collection = int(input("Enter the collection made: "))
    
    movies[name] = {
        'year': year,
        'director': director,
        'production_cost': production_cost,
        'collection': collection
    }

# a) Print all movie details
print("\nAll movie details:")
for name, details in movies.items():
    print(f"\nMovie: {name}")
    print(f"Year of release: {details['year']}")
    print(f"Director: {details['director']}")
    print(f"Production cost: {details['production_cost']}")
    print(f"Collection made: {details['collection']}")

# b) Displaying name of movies released before 2015
print("\nMovies released before 2015:")
for name, details in movies.items():
    if details['year'] < 2015:
        print(name)

# c) Movies that made a profit
print("\nMovies that made a profit:")
for name, details in movies.items():
    if details['collection'] > details['production_cost']:
        print(name)

# d) Movies directed by a particular director
director_name = input("\nEnter the name of the director to get movies directed by them: ")
print(f"Movies directed by {director_name}:")
for name, details in movies.items():
    if details['director'] == director_name:
        print(name)

