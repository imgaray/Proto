class Directory(object):
	def __init__(self, dirname, parent, directoryBuilder, fileBuilder):
		self._dirname = dirname
		self.directoryBuilder = directoryBuilder
		self.fileBuilder = fileBuilder
		self.parent = parent
		self.filemap = {}
	
	def build(self):
		self.directoryBuilder.buildDirectory(self.fullPath)
		for filename in self.filemap:
			filemap[filename].build()
	
	def hasFile(self, filename):
		return filename in self.filemap
				
	def addFile(self, filename):
		if not self.hasFile(filename):
			self.filemap[filename] = File(filename, self, self.fileBuilder)
		
	@property	
	def fullPath(self):
		if self.parent == none:
			return self.name
		return self.parent.fullPath + "/" + self.filename
