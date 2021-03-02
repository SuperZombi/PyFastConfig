# PyFastConfig
Fast creation and reading of files on Python with configurations.

<a href="README_rus.md"><img src="https://emojio.ru/images/twitter-64/1f1f7-1f1fa.png" width="30" height="30"></img>Читать на Русском</a>

### Install <a href="https://pypi.org/project/PyFastConfig/">Pypi</a>:
```
pip install PyFastConfig
```

</br>

Usage example:

<ul>
  <li><a href="#save">Save file</a></li>
  <li><a href="#load">Load file</a></li>
</ul>

```Python
import PyFastConfig as fc
```
<br/>

## Save
```Python
#Declare any values
min_t = 25
max_t = 35
arr = [45, 'hello', 81.5]
```
Quick save:
```Python
array = [min_t, max_t, arr]
fc.save(array)

# or just:
# fc.save([any values])
```
Result file (Config.txt):
```
min_t = int(25)
max_t = int(35)
arr = list([45, 'hello', 81.5])
```

### Optional options:

<table>
  <thead>
  <tr>       <th align="center">Name</th>       <th align="center">Accepts values</th>       <th align="center">Default</th></tr>
  </thead>
  
  <tr><td>   <code>array</code></td>            <td>Dataset</td>                             <td>Required</td></tr>
  <tr><td>   <code>file</code></td>             <td>File name</td>                           <td>"config.txt"</td></tr>
  <tr><td>   <code>mode</code></td>             <td>Write modes:<br/>"w" - rewrite<br/>"a" - append</td>        <td>"w"</td></tr>
  <tr><td>   <code>save_types</code></td>       <td>True/False</td>                          <td>True</td></tr>
  <tr><td>   <code>save_names</code></td>       <td>True/False</td>                          <td>True</td></tr>
</table>

```Python
fc.save(array, file="config.txt", mode="w", save_types=True, save_names=True)
```

<br/>
<br/>

## Load
Quick load:
```Python
#import values (only if run_mode is not False)
#With copy namespace
exec(fc.load("config.txt"))
```
### Optional options:

<table>
  <thead>
  <tr>       <th align="center">Name</th>       <th align="center">Explanation</th>       <th align="center">Default</th></tr>
  </thead>
  
  <tr><td>   <code>file</code></td>             <td>File name</td>                           <td>Required</td></tr>
  <tr><td>   <code>run_mode</code></td>            <td>Allows you to run (copy namespace) values<br/>from the library and continue working<br/>with them in the executable.</td>                             <td>True</td></tr>
  <tr><td>   <code>return_only_names</code></td>             <td>True/False</td>                           <td>False</td></tr>
  <tr><td>   <code>return_only_values</code></td>             <td>True/False</td>        <td>False</td></tr>

</table>

```Python
fc.load(file, run_mode=True, return_only_names=False, return_only_values=False)
```

If you changed the parameters for saving additional information (save_types and save_names) in the SAVE function, you must disable run_mode when reading such a file.

```Python
#Returns an array (use if you have disabled any of the following options: save_types or save_names)
print(fc.load("config.txt", run_mode=False))
```

<br/>

### Errors:

If you are reading a file in a function and you can't get objects: please try this:
```
names = fc.load("config.txt", return_only_names=True)
fc.load("config.txt")
for i in range(len(names)):
  globals()[names[i]] = eval("fc."+names[i])
```

Or this if you know the name of the variable in advance:
```
fc.load("config.txt")
name = fc.name
```
