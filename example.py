import PyFastConfig as fc

min_t = 25
max_t = 35
arr = [45, 'hello', 81.5]
fc.save(min_t, max_t, arr], file="my_file_name.txt")

exec(fc.load("my_file_name.txt"))

print(min_t)
print(max_t)
print(arr)



def func():
      exec(fc.load("my_file_name.txt", function_mode=True))
      
      print(min_t)
      print(max_t)
