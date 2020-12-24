# PyFastConfig
Быстрое создание и чтение файлов на Python с конфигурациями.

<a href="REAME.md">Read in English</a>

```Python
import PyFastConfig as fc

#Объявить переменные
min_t = 25
max_t = 35
arr = [45, 'hello', 81.5]
#Записать их для удобства в массив
array = [min_t, max_t, arr]
```
</br>

# SAVE
```Python
#Сохранить массив в файл
fc.save(array)
```

### Перегрузки: </br>
Имя - значение - по умолчанию </br>
------------------------------ </br>
```
array - массив данных (Обязательно),
file - имя файла ("config.txt"),
mode - режимы записи ("w"):
  "w" - переписать
  "a" - дописать в конец,
save_types - Сохранять типы переменных (True),
save_names - Сохранять имена переменных (True)
```
</br></br>

# LOAD
```Python
#Прочитать и импортировать значения (Лучший вариант)
exec(fc.load("config.txt"))

#Прочитать и показать только имена
print(fc.load("config.txt", return_only_names=True))

#Прочитать и показать только значения
print(fc.load("config.txt", return_only_values=True))

#Показать прочитаный массив
print(fc.load("config.txt", run_mode=False))
```

### Перегрузки: </br>
Имя - значение - по умолчанию </br>
------------------------------ </br>
```
file - имя файла (Обязательно),
run_mode - Режим инициализации (присвоить считаным переменным их значения) (Если выключить, то вернет просто массив) (True),
return_only_names - Возращает только имена переменных (False),
return_only_values - Возращает только значения переменных (False)
```
