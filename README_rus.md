# PyFastConfig
Быстрое создание и чтение файлов на Python с конфигурациями.

<a href="README.md"><img src="https://emojio.ru/images/twitter-64/1f1fa-1f1f8.png" width="30" height="30"></img>Read in English</a>

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
```
</br>

# SAVE
```Python
#Сохранить массив в файл
fc.save(min_t, max_t, arr)
```

### Перегрузки: </br>

<table>
  <thead>
  <tr>       <th align="center">Имя</th>       <th align="center">Значение</th>       <th align="center">По умолчанию</th></tr>
  </thead>
  
  <tr><td>   <code>*args</code></td>           <td>Переменные</td>                                                       <td>Обязательно</td></tr>
  <tr><td>   <code>file</code></td>            <td>Имя файла</td>                                                        <td>"config.txt"</td></tr>
  <tr><td>   <code>mode</code></td>            <td>Режимы записи:<br/>"w" - переписать<br/>"a" - дописать в конец</td>   <td>"w"</td></tr>
  <tr><td>   <code>save_types</code></td>      <td>Сохранять типы переменных<br/>(True/False)</td>                       <td>True</td></tr>
  <tr><td>   <code>save_names</code></td>      <td>Сохранять имена переменных<br/>(True/False)</td>                      <td>True</td></tr>
</table>

```Python
fc.save(*args, file="config.txt", mode="w", save_types=True, save_names=True)
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
Чтение внутри функции:
```Python
def func():
    exec(fc.load("config.txt", function_mode=True))
```

### Перегрузки: </br>

<table>
  <thead>
  <tr>       <th align="center">Имя</th>             <th align="center">Значение</th>                                      <th align="center">По умолчанию</th></tr>
  </thead>
  
  <tr><td>   <code>file</code></td>                  <td>Имя файла</td>                                                    <td>Обязательно</td></tr>
  <tr><td>   <code>run_mode</code></td>              <td>Режим инициализации:<br/>Присвоить считанным переменным их значения<br/>(Если выключить, то вернет просто массив)<br/>(True/False)</td>   <td>True</td></tr>
  <tr><td>   <code>function_mode</code></td>    <td>Тоже самое, что и <code>run_mode</code>, но выполняется внутри функции.</td>   <td>False</td></tr>
  <tr><td>   <code>return_only_names</code></td>     <td>Возращает только имена переменных<br/>(True/False)</td>           <td>False</td></tr>
  <tr><td>   <code>save_names</code></td>            <td>Возращает только значения переменных<br/>(True/False)</td>        <td>False</td></tr>
</table>


```Python
fc.load(file, run_mode=True, function_mode=False, return_only_names=False, return_only_values=False)
```
