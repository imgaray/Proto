class File(object):
	def __init__(self, filename, directory, fileBuilder):
		self.filename = filename
		self.directory = directory
		self.fileBuilder = fileBuilder
	
	def build(self):
		fileBuilder.buildFile(self.directory.fullPath + "/" + self.filename)
		
	
		
