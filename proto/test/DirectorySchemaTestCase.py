from unittest2 import TestCase
from proto import DirectorySchema
from stubBuilder import sBuilder

class DirectorySchemaTestCase(TestCase):
	
	def test_creation_should_fail(self):
		with self.assertRaises(AssertionError):
			DirectorySchema(None, None, None)

	def test_creation_success(self):
		stub = sBuilder()
		ds = DirectorySchema("root", stub, stub)
		self.assertEqual("root", ds.root)
		self.assertEqual(stub, ds.fileBuilder)
		self.assertEqual(stub, ds.directoryBuilder)
		
	def test_add_single_dir_to_root(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		ds.addDirectory("root/test")
		self.assertEqual(2, ds.dirCount)
		
	def test_add_duplicated_dir_to_root(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		ds.addDirectory("root/test")
		self.assertEqual(2, ds.dirCount)
		with self.assertRaises(AssertionError):
			ds.addDirectory("root/test")
		self.assertEqual(2, ds.dirCount)
	
	def test_add_dir_with_non_existing_parent(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		with self.assertRaises(AssertionError):
			ds.addDirectory("test_parent/test")
		self.assertEqual(1, ds.dirCount)
		
	def test_add_dir_duplicating_root_name(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		with self.assertRaises(AssertionError):
			ds.addDirectory("root")
	
	def test_build_various_directories(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		expected = ["root"]
		for i in xrange(3):
			ds.addDirectory("root/test" + str(i))
			expected.append("root/test" + str(i))
		for i in xrange(3):
			for j in xrange(3):
				ds.addDirectory("root/test" + str(i) + "/" + "test" + str(j))
				expected.append("root/test" + str(i) + "/" + "test" + str(j))
		ds.buildRepresentation()
		print sorted(expected)
		print sorted(stub.directories)
		self.assertEqual(sorted(expected), sorted(stub.directories))		

	def test_build_various_directories_and_files(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		expected = ["root"]
		expected_files = []
		for i in xrange(3):
			ds.addDirectory("root/test" + str(i))
			ds.addFile("root/test_file" + str(i))
			expected_files.append("root/test_file" + str(i))
			expected.append("root/test" + str(i))
		for i in xrange(3):
			for j in xrange(3):
				ds.addDirectory("root/test" + str(i) + "/" + "test" + str(j))
				ds.addFile("root/test" + str(i) + "/" + "test_file" + str(j))
				expected.append("root/test" + str(i) + "/" + "test" + str(j))
				expected_files.append("root/test" + str(i) + "/" + "test_file" + str(j))
		ds.buildRepresentation()
		self.assertEqual(sorted(expected), sorted(stub.directories))
		self.assertEqual(sorted(expected_files), sorted(stub.files))	
			
	@staticmethod
	def create_ds_and_builder():
		stub = sBuilder()
		ds = DirectorySchema("root", stub, stub)
		return stub, ds
		
if __name__=="__main__":
	unittest2.main()
