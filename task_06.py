# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random as rd

my_favorite_songs = {
  'Waste a Moment': 3.03,
  'New Salvation': 4.02,
  'Staying\' Alive': 3.40,
  'Out of Touch': 3.03,
  'A Sorta Fairytale': 5.28,
  'Easy': 4.15,
  'Beautiful Day': 4.04,
  'Nowhere to Run': 2.58,
  'In This World': 4.02,
}
_taken_song = ''
_song_str = []
_key = []
_num = 0
_min = 0
_sek = 0
_total_m = 0
_total_s = 0
for k in my_favorite_songs.keys():
  _song_str.append(k)
#print(_song_str)
while _num < 3 :
  _key = rd.choice(_song_str)
  _min = int(my_favorite_songs[_key] // 1)
  _sek = round(my_favorite_songs[_key] % 1 * 100)
 # print(_key,_min, _sek )
  if _key not in  _taken_song :
    _taken_song +=  _key  if _key  == '' else ',' + _key
    _total_m += _min
    _total_s += int(_sek *100)//100 
    _num += 1
 #   print(_key,_min, _sek, '    ', _total_m, '     ',_total_s)
    while _total_s > 59 :
      _total_s -= 60
      _total_m += 1


print(f"Три песни ({_taken_song[1 :]}) звучат {_total_m} мин {_total_s} сек")
