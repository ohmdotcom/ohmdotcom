f = {}      #пустой словарь
null = None  #интерпретация объектов JSON в python
true = True
false = False

with open("package.json") as f:   #открываем файл как "f" 
    line = f.readline()  # задаём переменную "line", в которой считываем строки в "f"
    line.splitlines()   #Разделяем построчно, по умолчанию пробел
   # print(line)
    for line in f.readline():
      #       print(line)
        key, *value = line.split(sep=", ") # пара ключ- значение и разделитель "," для пар.
      #  f.update({key:value})
       # text = f.read()
    print(line)
    #f[key, ":"] = value
    #for value in f:
    #print(key, ":", value)


