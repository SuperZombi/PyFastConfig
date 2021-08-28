import inspect

def save(*array, file="config.txt", mode="w", save_types=True, save_names=True):
	F = ""
	for i in array:
		if save_names:
			name = [name for name, value in inspect.currentframe().f_back.f_locals.items() if i is value]
			F += str(name[0]) + " = "
		if save_types:
			_type = type(i).__name__
			F += str(_type) + "("
			if isinstance(_type, str):
				F += "'"
			F += str(i)
			if isinstance(_type, str):
				F += "'"
			F += ")\n"
		if not save_types:
			F += str(i) + "\n"

	with open(file, mode) as _file:
		_file.write(F)
	_file.close()


def load(file, run_mode=True, function_mode=False, return_only_names=False, return_only_values=False):
	with open(file, 'r') as _file:
		lines = [x.strip('\n') for x in _file.readlines()]
	_file.close()

	if return_only_names:
		names = []
		for i in lines:
			string = i.split(' = ')
			names.append(string[0])
		return names

	if return_only_values:
		values = []
		for i in lines:
			string = i.split(' = ')
			values.append(string[1])
		return values

	if function_mode:
		comand = ""
		for i in lines:
			string = i.split(' = ')
			globals()[string[0]] = eval(string[1])
			comand += f'globals()["{str(string[0])}"] = fc.{str(string[0])}'
			comand += "\n"
		return comand

	if run_mode:
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
