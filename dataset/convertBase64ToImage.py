import base64
import os
import sys


FOLDER = os.path.abspath("images")
IMAGE_FORMAT = "image{}.jpg"


def converter(base64_string:str, name:str)->None:
	open(name, "wb").write(base64.b64decode(base64_string))


def main()->int:

	try:
		os.mkdir(FOLDER)
	except FileExistsError:
		pass
		
	current_index = len(os.listdir(FOLDER))

	for index, line in enumerate(open(sys.argv[1]).read().split("\n")):
		if line:
			converter(line,
					  os.path.join(
						FOLDER,
						IMAGE_FORMAT.format(index+current_index)))


if __name__ == '__main__':
	main()