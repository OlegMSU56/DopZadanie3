def calculate_structure_sum(data_structure):
    symma = 0
    if isinstance(data_structure, int):  # проверяем содержит ли параметр функции тип данных int
        return data_structure
    if isinstance(data_structure, str):  # проверяем содержит ли параметр функции тип данных str
        return len(data_structure)
    if isinstance(data_structure, (list, tuple, set)):  # проверяем содержит ли параметр функции тип данных list, tuple, set
        for i in data_structure:
            symma += calculate_structure_sum(i)  # добавляем i-й элемент к сумме при условиях описанных в строке 3 и 5, если не подходит, функция переходит в строку 9 или возвращается в строку 7
    if isinstance(data_structure, dict):  # проверяем содержит ли параметр функции тип данных dict
        for key, value in data_structure.items():
            symma += calculate_structure_sum(key)  # добавляем значения ключа к сумме при условиях описанных в строке 3 и 5
            symma += calculate_structure_sum(value)  # добавляем значения величины к сумме при условиях описанных в строке 3 и 5
    return symma




data_structure=[
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)



