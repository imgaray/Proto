from File import File

class Directory(object):
	def __init__(self, dirname, parent, directoryBuilder, fileBuilder):
		assert(dirname is not None and directoryBuilder is not None and fileBuilder is not None)
		self.dirname = dirname
		self.directoryBuilder = directoryBuilder
		self.fileBuilder = fileBuilder
		self.parent = parent
		self.filemap = {}
		self.dirmap = {}
	
	def build(self):
		self.directoryBuilder.buildDirectory(self.fullPath)
		for filename in self.filemap:
			self.filemap[filename].build()
		for dirname in self.dirmap:
			self.dirmap[dirname].build()
	
	def hasDir(self, dirname):
		return dirname in self.dirmap
	
	def hasFile(self, filename):
		return filename in self.filemap
				
	def addFile(self, filename):
		aux = filename.split("/")
		assert(len(aux) > 0)
		if len(aux) > 1:
			assert(self.name == aux[0])
			aux.pop(0)
			if (len(aux) > 1):
				assert(self.hasDir(aux[0]))
				self.dirmap[aux[0]].addFile("/".join(aux))
			else:
				self.addFile(aux[0])
		else:
			assert(not self.hasFile(filename) and not self.hasDir(filename))
			self.filemap[filename] = File(filename, self, self.fileBuilder)
	
	def addDir(self, dirname):
		aux = dirname.split("/")
		assert(len(aux) > 0)
		if len(aux) > 1:
			assert(self.name == aux[0])
			aux.pop(0)
			if (len(aux) > 1):
				assert(self.hasDir(aux[0]))
				self.dirmap[aux[0]].addDir("/".join(aux))
			else:
				self.addDir(aux[0])
		else:
			assert(not self.hasDir(dirname) and not self.hasFile(dirname))
			self.dirmap[dirname] = Directory(dirname, self, self.directoryBuilder, self.fileBuilder)
	
	@property
	def children(self):
		return [self.dirmap[dname] for dname in self.dirmap]
		
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
