#! python3
#encoding:utf-8
'''
标准库中的模块unittest 提供了代码测试工具。
单元测试用于核实函数的某个方面没有问题；测试用例是一组单元测试
'''
import unittest
from test_code import get_formatted_name
from test_code import AnnoymousSurvey as ASy


#测试函数
class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('hello','world')
		self.assertEqual(formatted_name,'Hello World')
		
	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name(
			'hello','world','python')
		self.assertEqual(formatted_name,'Hello Python World')
		
class SurveyTestCase(unittest.TestCase):
	'''unittest.TestCase 类包含方法setUp(),将先运行它，再运行各个以test_打头的方法'''
	def setUp(self):
		'''可在setUp() 方法中创建一系列实例并设置它们的属性，不用在每个测试方法中都创建实例并设置其属性'''
		question = "How old are you?"
		self.my_survey = ASy(question)
		self.responses = [18,20,22]
		
	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)
		
	def test_store_muti_responses(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)
	
unittest.main()

