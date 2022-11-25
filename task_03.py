# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

days_in_year =   {1 : '31'
                , 2 :'28'
                , 3 :'31'
                , 4:'30'
                , 5 :'31'
                , 6 :'30'
                , 7 :'31'
                , 8 :'31'
                , 9 :'30'
                ,10 :'31'
                ,11 :'30'
                ,12 :'31'
                  }  
print(days_in_year)
user_input = input("Введите номер месяца: ")
month = int(user_input)
#print(days_in_year.get(month, 'такого месяца не бывает'))
if month in days_in_year :
  print('Вы ввели', month)
else :
  print('Вы ввели несуществующий месяц')

# Отлично
# Вот еще варианты
# Решение 1
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month in [4, 6, 9, 11]:
    print(30)
elif month == 2:
    print(28)
else:
    print('Введен неправильный номер месяца!')

# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))
