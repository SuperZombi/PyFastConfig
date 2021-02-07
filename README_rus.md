# PyFastConfig
Быстрое создание и чтение файлов на Python с конфигурациями.

<a href="README.md">Read in English</a>

### Установить <a href="https://pypi.org/project/PyFastConfig/">Pypi</a>:
```
pip install PyFastConfig
```

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

# или просто:
# fc.save([любые значения])
```

### Перегрузки: </br>

<table>
  <thead>
  <tr>       <th align="center">Имя</th>       <th align="center">Значение</th>       <th align="center">По умолчанию</th></tr>
  </thead>
  
  <tr><td>   <code>array</code></td>           <td>Массив данных</td>                                                    <td>Обязательно</td></tr>
  <tr><td>   <code>file</code></td>            <td>Имя файла</td>                                                        <td>"config.txt"</td></tr>
  <tr><td>   <code>mode</code></td>            <td>Режимы записи:<br/>"w" - переписать<br/>"a" - дописать в конец</td>   <td>"w"</td></tr>
  <tr><td>   <code>save_types</code></td>      <td>Сохранять типы переменных<br/>(True/False)</td>                       <td>True</td></tr>
  <tr><td>   <code>save_names</code></td>      <td>Сохранять имена переменных<br/>(True/False)</td>                      <td>True</td></tr>
</table>

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
