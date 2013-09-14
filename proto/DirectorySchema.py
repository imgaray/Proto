
class DirectorySchema(object):
	"""Represents a directory schema based on a project representation. It
	will be in charge of building de directory tree and adding the files"""
	
	def __init__(self, root, fileBuilder, directoryBuilder):
		self.directoryMap = {}
		self._root = Directory(root, None, directoryBuilder, fileBuilder)
		self.directoryBuilder = directoryBuilder
		self.fileBuilder = fileBuilder
		self.directoryMap[root] = Directory(root)
	
	@property
	def root(self):
		return this._root	
	
	def addDirectoryToRoot(self, directory):
		""" adds a directory to the root directory.
		args: directory(string), the name of the directory"""
		self.addDirectoryTo(directory, self.root.name)
	
	def addDirectoryTo(self, directory, parent):
		""" adds a directory to the root directory.
		args: directory(string), the name of the directory
			parent(string), the name of the parent directory"""
		assert(parent not in self.directoryMap)
		assert(directory not in self.directoryMap)
		self.directoryMap[directory] = Directory(directory, self.directoryMap[parent], self.directoryBuilder, self.fileBuilder)
			
	def addFileTo(self, filename, directory):
		"""adds a file to a specific directory.
		args: filename(string), the name of the filename
			directory(string), the name of the directory where the file 
			would be inserted"""
		assert(directory not in self.directoryMap)
		assert(not self.directoryMap[directory].hasFile(filename))
		self.directoryMap[directory].addFile(filename)
	
	def buildRepresentation(self, logicSchema):
		""" builds the structure of the shhiiieeeet"""
		tocreate = [self.root]
		while len(toCreate) > 0:
			currentDirectory = toCreate.pop()
			for child in currentDirectory.children:
				toCreate.append(child)
			currentDirectory.build()
			
			
			
	
