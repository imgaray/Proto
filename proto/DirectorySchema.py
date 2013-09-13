import os

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
	
	@accepts(object, str)
	def addDirectoryToRoot(self, directory):
		self.addDirectoryTo(directory, self.root.name)
	
	@accepts(object, str, str)
	def addDirectoryTo(self, directory, parent):
		"""adds a directory to the schema, nesting it to the specific parent.
		A parent must be specified."""
		assert(self.directoryMap.contains(parent))
		assert(not self.directoryMap.contains(directory))
		self.directoryMap[directory] = Directory(directory, self.directoryMap[parent], self.directoryBuilder, self.fileBuilder)
			
	@accepts(object, str, str)
	def addFileTo(self, filename, directory):
		"""adds a file to a specific directory."""
		assert(self.directoryMap.contains(directory))
		assert(not self.directoryMap[directory].hasFile(filename))
		self.directoryMap[directory].addFile(filename)

	@accepts(object, LogicSchema)
	def buildRepresentation(self, logicSchema):
		""" builds the structure of the shhiiieeeet"""
		tocreate = [self.root]
		while len(toCreate) > 0:
			currentDirectory = toCreate.pop()
			for child in currentDirectory.children:
				toCreate.append(child)
			currentDirectory.build()
			
			
			
	
