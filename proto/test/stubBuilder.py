class sBuilder(object):
	def __init__(self):
		self.filesbuilt = []
		self.directoriesbuilt = []
	
	def buildFile(self, filepath):
		self.filesbuilt.append(filepath)
	
	def buildDirectory(self, dirpath):
		self.directoriesbuilt.append(dirpath)
		
	@property
	def files(self):
		return self.filesbuilt

	@property
	def directories(self):
		return self.directoriesbuilt
