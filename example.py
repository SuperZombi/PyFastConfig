import PyFastConfig as fc

fc.save([min_t = 25, max_t = 35, arr = [45, 'hello', 81.5]], file="my_file_name.txt")

exec(fc.load("my_file_name.txt"))

print(min_t)
print(max_t)
print(arr)