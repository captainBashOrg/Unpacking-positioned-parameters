print('Распаковка позиционных параметров')

def print_params(a = 1, b = 'строка', c = True):
    print(f"a= {a}, b={b}, c={c}")



#Начало основной программы

values_list = [1, 3.1415, ["Слон", "мышь"]  ]
values_dict = { 'a': 1, 'b':2, "c":5}

values_list_2 = ["Слонские уши", "мышьев нос"]
#

#print(values_list) #print(values_dict)

print_params() # in default
print_params(values_list) # Списог встаёт на место а, остальные по=дефолту
print_params(*values_list) # Список распакован, на место с встаёт список ["Слон", "мышь"] из values_list
# print_params(**values_list)  а вот так нельзя ;)
print("") #Разделитель
print_params(  values_dict)  # a= {'a': 1, 'b': 2, 'c': 5}, b=строка, c=True
print_params( *values_dict)  # a= a, b=b, c=c Ключи?! NB прокачать глубже
print_params(**values_dict)  # логично. a= 1, b=2, c=5 Значения

print_params(*values_list_2, 42) # аргументы встают на место а и б, с -- по дефолтному





