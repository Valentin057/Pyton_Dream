# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random

import random as rd
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

song_count = my_favorite_songs.index(my_favorite_songs[-1])
# print(song_count)
song_name_test = [] 
n = 0
total_time = 0
total_min = 0
total_sec = 0
while n < 3: 
    song_index = rd.randint(0,song_count) #  print(song_index)
    song_name = my_favorite_songs[song_index][0]
    time_song = my_favorite_songs[song_index][1]
    time_min = int(time_song)
    time_sec = round((time_song - int(time_song)) * 100)
    if song_name in song_name_test : 
        #n = n-1
        continue
    else :   
      print(f" Композиция = {song_name} продожительность:  мин - {str(time_min)} сек - {str(time_sec)}" ,)
      total_min = int(total_min + time_min) 
      total_sec = int(total_sec + time_sec) 
      song_name_test.append(song_name) 
      n = n + 1

print(total_min,total_sec)
sec = 0
n = 0
while total_sec > 60:
  total_sec = total_sec - 60 
  n = n + 1    
  print(total_min,total_sec)
  next
total_min = total_min + n

print(" выбранные композиции: '" + "', '".join(song_name_test) +"'")
print(f" Общая продолжительность трех композиций - {total_min} мин {total_sec} сек ")  
print(f" Три песни звучат - {total_min}.{total_sec}")

# Понял идею с перехлестыванием по секундам)
# Ну как по мне довольно много переменных
# Все ок. Но скину свой вариант
# Решение 2
time = 0
for song in sample(my_favorite_songs, 3):
    print(song[0])
    time += song[1]

print(f'Три песни звучат {round(time, 2)}')
