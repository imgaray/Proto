from File import File

class Directory(object):
	def __init__(self, dirname, parent, directoryBuilder, fileBuilder):
		assert(dirname is not None and directoryBuilder is not None and fileBuilder is not None)
		self.dirname = dirname
		self.directoryBuilder = directoryBuilder
		self.fileBuilder = fileBuilder
		self.parent = parent
		self.filemap = {}
	
	def build(self):
		self.directoryBuilder.buildDirectory(self.fullPath)
		for filename in self.filemap:
			self.filemap[filename].build()
	
	def hasFile(self, filename):
		return filename in self.filemap
				
	def addFile(self, filename):
		if not self.hasFile(filename):
			self.filemap[filename] = File(filename, self, self.fileBuilder)
		
	@property	
	def fullPath(self):
		if self.parent == None:
			return self.name
		return self.parent.fullPath + "/" + self.name
	
	@property	
	def filesCount(self):
		return len(self.filemap)

	@property
	def name(self):
		return self.dirname
