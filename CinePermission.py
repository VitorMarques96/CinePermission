movie1 = 'Rocky'
movie2 = 'The Hangover'
movie3 = 'Saw'

name = input('Tell me your name: ')

print(f'{name}, Tell me the movie do you want to watch: ')
movie = input(f'{movie1} [1], {movie2} [2], {movie3} [3]: ')
if movie == '1':
    minimum_age = '12'
    movie_name = movie1
elif movie == '2':    
    minimum_age = '14'
    movie_name = movie2
elif movie == '3':
    minimum_age = '16'
    movie_name = movie3
else:
    print(f"'I'm sorry, {name}, i can't understand wich movie you want, try again!")


age = input(f'{name}, tell me your age: ')
if age < minimum_age:
    permission = input(f'{name}, Do you have permission to watch {movie_name} alone? [Y] or [N]: ')
    if permission == 'Y':
        print(f'Can you go to the cine, {name}. have fun watching {movie_name}!')
    elif permission == 'N':
        print(f'The minimum age to watch {movie_name} is {minimum_age}, {name}.')
        print(f"I'm sorry, but you can't watch {movie_name} without permission!")
    else:
        print(f"I'm sorry, {name}, but i can't understand your answear, please try again!")
else:
    print(f'The minimum age to watch {movie_name} is {minimum_age}, {name}. have fun watching {movie_name}!')