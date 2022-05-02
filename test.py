import unittest
from api_tests.make_item_test import MakeItem

class Test(MakeItem):
    def test_create_item(self):
        return super().create_item()
    
    def test_clear_rows(self):
        return super().clear_rows()
    
if __name__ == '__main__':
    unittest.main()