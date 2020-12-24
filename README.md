# PyFastConfig
Fast creation and reading of files on Python with configurations.
Usage example:

```Python
import PyFastConfig as fc
```

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
```
Result file (Config.txt):
```
min_t = int(25)
max_t = int(35)
arr = list([45, 'hello', 81.5])
```

### Optional options:

file: File name can be specified <br/>
mode: "w" - write, "a" - append <br/>
save_types: default - True <br/>
save_names: default - True <br/>

```Python
fc.save(array, file="config.txt", mode="w", save_types=True, save_names=True)
```

<br/>
<br/>

## Load
Quick load:
```Python
#With copy namespace
comands = fc.load("config.txt")
#import values (only if run_mode is not False)
for i in range(len(comands)):
  exec(comands[i])
```
### Optional options:
run_mode: default - True <br/> Allows you to run (copy namespace) values from the library and continue working with them in the executable. <br/><br/>
return_only_names: default - False <br/>
return_only_values: default - False <br/>

```Python
fc.load(file, run_mode=True, return_only_names=False, return_only_values=False)
```

If you changed the parameters for saving additional information (save_types and save_names) in the SAVE function, you must disable run_mode when reading such a file.

```Python
#Returns an array (use if you have disabled any of the following options: save_types or save_names)
print(fc.load("config.txt", run_mode=False))
```
