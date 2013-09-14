class sDirectory(object):
	def __init__(self, addon = ""):
		self.dirname = "test" + addon
		
	@property	
	def fullPath(self):
		return self.dirname
