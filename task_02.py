# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

citys = ["Москва", "Углич", "Торжок", "Ижевск"]
residents = [["Москва",12_000_000],["Углич",45_000],["Торжок",120_000],["Ижевск",500_000]]
tot_people = 0
for i in range(len(residents)) :
  tot_people = tot_people + residents[i][1]
print("Население города {0} составляет {1:_} человек".format(residents[1][0], residents[1][1]))
print(f"Итого размер населения составляет {tot_people:_} человек")
