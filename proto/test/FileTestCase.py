import proto
import unittest2
import stubDirectory as sd
import stubBuilder as sb

class FileTestCase(unittest2.TestCase):
		
	def test_create_file(self):
		testfile = proto.File("test", sd.sDirectory(), sb.sBuilder())
		self.assertEqual(testfile.name, "test")
		
	@unittest2.expectedFailure	
	def test_create_file_fail(self):
		testfile = proto.File(None, None, None)

	def test_build_file(self):
		stub = sb.sBuilder()
		testfile = proto.File("test", sd.sDirectory(), stub)
		testfile.build()
		self.assertEqual("test/test", stub.files[0])
		

if __name__ == '__main__':
    unittest2.main()		
