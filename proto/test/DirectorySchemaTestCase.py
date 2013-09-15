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
		ds.addDirectoryToRoot("test")
		self.assertEqual(2, ds.dirCount)
		
	def test_add_duplicated_dir_to_root(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		ds.addDirectoryToRoot("test")
		self.assertEqual(2, ds.dirCount)
		with self.assertRaises(AssertionError):
			ds.addDirectoryToRoot("test")
		self.assertEqual(2, ds.dirCount)
	
	def test_add_dir_with_non_existing_parent(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		with self.assertRaises(AssertionError):
			ds.addDirectoryTo("test", "test_parent")
		self.assertEqual(1, ds.dirCount)
		
	def test_add_dir_duplicating_name(self):
		stub, ds = DirectorySchemaTestCase.create_ds_and_builder()
		with self.assertRaises(AssertionError):
			ds.addDirectoryTo("test", "test")
		self.assertEqual(1, ds.dirCount)
	
	
	@staticmethod
	def create_ds_and_builder():
		stub = sBuilder()
		ds = DirectorySchema("root", stub, stub)
		return stub, ds
		
if __name__=="__main__":
	unittest2.main()
