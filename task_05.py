# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000
total_salary = salary * 12
total_expenses = 0
#print(f"{total_expenses}:_") 
for i in range(12) :
  if i == 0 :
    pass
  else :  
    expenses = expenses + (expenses * 3/100)
#  1 способ записи
  total_expenses += expenses
print(f" доходы - {round(salary * 12,2):_} расходы -{round(total_expenses,2):_}")    
print(f"Необходимо взять в долг {round(total_expenses - total_salary,2):_}")  

#  2 способ записи
for i in range(12) :
  expenses = expenses + (expenses * 3/100) if i > 0 else 0  
  total_expenses += expenses
print(f" доходы - {round(salary * 12,2):_} расходы -{round(total_expenses,2):_}")    
print(f"Необходимо взять в долг {round(total_expenses - total_salary,2):_}") 
