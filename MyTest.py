from TestCase import TestCase
from TestResult import TestResult
from TestCaseTest import TestCaseTest
from TestSuite import TestSuite
from TestSuiteTest import TestSuiteTest


class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')


result = TestResult()

test = MyTest('test_a')
test.run(result)

test = MyTest('test_b')
test.run(result)

test = MyTest('test_c')
test.run(result)

print(result.summary())

#Testes do TestCaseTest
result2 = TestResult()

test = TestCaseTest('test_result_success_run')
test.run(result2)

test = TestCaseTest('test_result_failure_run')
test.run(result2)

test = TestCaseTest('test_result_error_run')
test.run(result2)

test = TestCaseTest('test_result_multiple_run')
test.run(result2)

test = TestCaseTest('test_was_set_up')
test.run(result2)

test = TestCaseTest('test_was_run')
test.run(result2)

test = TestCaseTest('test_was_tear_down')
test.run(result2)

test = TestCaseTest('test_template_method')
test.run(result2)

print(result.summary()) 

#Testes do TestSuiteTest e TestCase usando o TestSuite
result3 = TestResult()
suite = TestSuite()

suite.add_test(TestCaseTest('test_result_success_run'))
suite.add_test(TestCaseTest('test_result_failure_run'))
suite.add_test(TestCaseTest('test_result_error_run'))
suite.add_test(TestCaseTest('test_result_multiple_run'))
suite.add_test(TestCaseTest('test_was_set_up'))
suite.add_test(TestCaseTest('test_was_run'))
suite.add_test(TestCaseTest('test_was_tear_down'))
suite.add_test(TestCaseTest('test_template_method'))

suite.add_test(TestSuiteTest('test_suite_size'))
suite.add_test(TestSuiteTest('test_suite_success_run'))
suite.add_test(TestSuiteTest('test_suite_multiple_run'))

suite.run(result3)
print(result3.summary())     