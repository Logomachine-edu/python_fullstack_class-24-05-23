string = input("Введите название компании:")
len_string = len(string) // 2
new_string = string[len_string:] + string[:len_string]
print("Новое название компании:", new_string)
