import unittest2
from unittest2 import TestCase
from proto import Directory
from stubBuilder import sBuilder

class DirectoryTestCase(TestCase):
		
	def create_nested(self, level_of_depth):
		stub = sBuilder()
		targ = None
		aux = None
		for i in xrange(level_of_depth):
			aux = Directory("test" + str(i), aux, stub, stub)
		targ = Directory("leaf", aux, stub, stub)
		return aux, targ
	
	def create_nested_leaf(self, level_of_depth):
		return self.create_nested(level_of_depth)[1]

	def test_create_root_dir(self):
		stub = sBuilder()
		direct = Directory("test", None, stub, stub)
		self.assertEqual("test", direct.fullPath)
		self.assertEqual(0, direct.filesCount)
	
	def test_create_child_dir(self):
		stub = sBuilder()
		root = Directory("root", None, stub, stub)
		direct = Directory("test", root, stub, stub)
		self.assertEqual("root/test", direct.fullPath)
		self.assertEqual(0, direct.filesCount)
		self.assertEqual("root", direct.parent.name)
			
	def test_build_simple(self):
		direct = self.create_nested_leaf(2)
		direct.build()
		expected = "test0/test1/leaf"
		self.assertEqual(1, len(direct.directoryBuilder.directories))
		self.assertEqual(expected, direct.directoryBuilder.directories[0])
		
	def test_build_with_file(self):
		direct = self.create_nested_leaf(2)
		expected = []
		expecteddir = [direct.fullPath]
		for x in xrange(4):
			direct.addFile("test_file" + str(x))
			expected.append(direct.fullPath + "/" + "test_file" + str(x))
		direct.build()
		self.assertEqual(len(expected), len(direct.directoryBuilder.files))
		self.assertEqual(sorted(expected), sorted(direct.directoryBuilder.files))
		self.assertEqual(len(expecteddir), len(direct.directoryBuilder.directories))
		self.assertEqual(expecteddir, direct.directoryBuilder.directories)
		
	def test_add_single_file(self):
		direct = self.create_nested_leaf(2)
		direct.addFile("myfile")
		self.assertTrue(direct.hasFile("myfile"))
		
	def test_add_duplicated_file(self):
		direct = self.create_nested_leaf(2)
		direct.addFile("myfile")
		with self.assertRaises(AssertionError):
			direct.addFile("myfile")
		self.assertEqual(1, direct.filesCount)
		
		
		
if __name__ == '__main__':
    unittest2.main()
