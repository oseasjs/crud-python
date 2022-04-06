from src.service.task_service_unit_test import TaskServiceUnitTest
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TaskServiceUnitTest)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())