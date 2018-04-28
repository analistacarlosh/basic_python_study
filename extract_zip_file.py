# coding: utf-8

import os
import zipfile
import sys

def main(path):
	if not os.path.exists(path):
		print("File {filePath} no exist".format(filePath=path))
		sys.exit(-1)
	else:
		zfile = zipfile.ZipFile(path)
		zfile.extractall()
		print("Arquivos extracteds")

if __name__ == "__main__":
	main(sys.argv[1])