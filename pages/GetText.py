#! /usr/bin/python

class ReadText():
	def __init__(self, page):
		self.page = page
		self.file = open(f"./text/{page}.txt", 'r')
		self.lines = self.file.readlines()

	def read(self, line_nb):
		line = self.lines[line_nb]
		line = line.replace("\\n", "\n \n")
		return line

	def update(self):
		self.file.close()
		self.file = open(f"./text/{self.page}.txt", 'r')
		self.lines = self.file.readlines()

if __name__ == '__main__':
	rt = ReadText("main")
	print(rt.read(1))