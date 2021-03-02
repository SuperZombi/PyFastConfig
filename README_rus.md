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

```Python
fc.save(array, file="config.txt", mode="w", save_types=True, save_names=True)
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

<table>
  <thead>
  <tr>       <th align="center">Имя</th>             <th align="center">Значение</th>                                      <th align="center">По умолчанию</th></tr>
  </thead>
  
  <tr><td>   <code>file</code></td>                  <td>Имя файла</td>                                                    <td>Обязательно</td></tr>
  <tr><td>   <code>run_mode</code></td>              <td>Режим инициализации:<br/>Присвоить считанным переменным их значения<br/>(Если выключить, то вернет просто массив)<br/>(True/False)</td>   <td>True</td></tr>
  <tr><td>   <code>return_only_names</code></td>     <td>Возращает только имена переменных<br/>(True/False)</td>           <td>False</td></tr>
  <tr><td>   <code>save_names</code></td>            <td>Возращает только значения переменных<br/>(True/False)</td>        <td>False</td></tr>
</table>


```Python
fc.load(file, run_mode=True, return_only_names=False, return_only_values=False)
```

<br/>

### Ошибки:

Если вы читаете файл в функции и не можете получить объекты - попробуйте это:
```
names = fc.load("config.txt", return_only_names=True)
fc.load("config.txt")
for i in range(len(names)):
  globals()[names[i]] = eval("fc."+names[i])
```

Или это, если вы заранее знаете имя переменной:
```
fc.load("config.txt")
name = fc.name
```
