from unittest import TestCase, main

from utils import to_str


class MyUtilsTest(TestCase):
    """Test utils.to_str

    unittest method name must start with 'test'

    unittest doc: https://docs.python.org/3.5/library/unittest.html

    Test methods on TestCase classes must start with the word test.

    It’s important to write both unit tests (for isolated functionality) and
    integration tests (for modules that interact).


    Tests can be numerous, and their set-up can be repetitive. Luckily,
    we can factor out set-up code by implementing a method called setUp(),
    which the testing framework will automatically call for every single test
    we run.

    If setUp() succeeded, tearDown() will be run whether the test method
    succeeded or not.
    """

    def setUp(self):
        self.int_value = 3
        self.str_value = 'foo'

    def tearDown(self):
        print('bye')

    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('foo', to_str(self.str_value))

    def test_to_str_int(self):
        self.assertRaises(TypeError, to_str, 3)

    def test_to_str_bad(self):
        self.assertRaises(TypeError, to_str, object())

    def test_to_str_bad_verbose(self):
        with self.assertRaises(TypeError):
            to_str(self.int_value)

if __name__ == '__main__':
    main()