import inspect

def save(array, file="config.txt", mode="w", save_types=True, save_names=True):
	F = ""
	for i in range(len(array)):
		if save_names == True:
			name = [name for name, value in inspect.currentframe().f_back.f_locals.items() if array[i] is value]
			F += str(name[0]) + " = "
		if save_types == True:
			_type = type(array[i]).__name__
			F += str(_type) + "(" + str(array[i]) + ")\n"
		if save_types == False:
			F += str(array[i]) + "\n"

	with open(file, mode) as _file:
		_file.write(F)
	_file.close()


def load(file, run_mode=True, return_only_names=False, return_only_values=False):
	with open(file, 'r') as _file:
		lines = [x.strip('\n') for x in _file.readlines()]
	_file.close()

	if return_only_names == True:
		names = []
		for i in range(len(lines)):
			string = lines[i].split(' = ')
			names.append(string[0])
		return names

	if return_only_values == True:
		values = []
		for i in range(len(lines)):
			string = lines[i].split(' = ')
			values.append(string[1])
		return values

	if run_mode == True:
		comand = "from PyFastConfig import "
		for i in range(len(lines)):
			string = lines[i].split(' = ')
			globals()[string[0]] = eval(string[1])
			comand += str(string[0])
			if i+1 == len(lines):
				None
			else:
				comand += ", "
		return comand

	return lines