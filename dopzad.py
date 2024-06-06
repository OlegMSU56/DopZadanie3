def calculate_structure_sum(data_structure):
     x = 0 # здесь будем собирать данные типа int
     y = 0 # здесь будем собирать данные типа str
     s = x + y  # здесь будем собирать данные типа str и int
     for i in data_structure:
         if type(i) == str:
            y += len(i)
            s = x + y # здесь будем собирать данные типа str и int
         if type(i) == int:
            x += i
     for j in data_structure(i):
         if type(j) == list or type(j) == tuple:
            if type(i) == str:
                    y += len(i)
            if type(i) == int:
                    x += i
            if type(j) == dict:
                if type(i) == str:
                    y += len(i)
                if type(i) == int:
                    x += i
     return s



result = calculate_structure_sum([
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
])
print(result)



