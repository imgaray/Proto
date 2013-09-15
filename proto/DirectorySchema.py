from Directory import Directory

class DirectorySchema(object):
	"""Represents a directory schema based on a project representation. It
	will be in charge of building de directory tree and adding the files"""
	
	def __init__(self, root, fileBuilder, directoryBuilder):
		assert( root is not None and fileBuilder is not None and directoryBuilder is not None)
		self._root = Directory(root, None, directoryBuilder, fileBuilder)
		self.directoryBuilder = directoryBuilder
		self.fileBuilder = fileBuilder
		self.dircount = 1
	
	@property
	def root(self):
		return self._root.name
		
	@property
	def dirCount(self):
		return self.dircount
			
	def addDirectory(self, directory):
		""" adds a directory to the directory schema.
		args: directory(string), the full path of the directory"""
		assert(directory is not None and directory != self.root)
		self._root.addDir(directory)
		self.dircount += 1
					
	def addFile(self, filepath):
		"""adds a file to a specific directory.
		args: filename(string), the name of the filename
			directory(string), the full path of the directory where the file 
			would be inserted"""
		assert(filepath is not None)
		self._root.addFile(filepath)
	
	def buildRepresentation(self):
		""" builds the structure of the shhiiieeeet"""
		self._root.build()
			
			
			
	
