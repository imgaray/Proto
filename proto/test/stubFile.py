class sFile(object):
	def __init__(self, filename, directory, fileBuilder):
		assert(filename is not None and directory is not None and fileBuilder is not None)
		self.filename = filename
		self.directory = directory
		self.fileBuilder = fileBuilder
	
	def build(self):
		self.fileBuilder.buildFile(self.directory.fullPath + "/" + self.filename)
		
	@property
	def name(self):
		return self.filename
	
	@property
	def dirpath(self):
		return self.directory
		
