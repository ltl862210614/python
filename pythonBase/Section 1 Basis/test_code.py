#! python3
#encoding:utf-8

class AnnoymousSurvey():
	def __init__(self,question):
		self.question = question
		self.responses = []
		
	def show_question(self):
		print(question)
		
	def store_response(self,new_response):
		self.responses.append(new_response)
		
	def show_results(self):
		print("Survey results:")
		for response in responses:
			print(response+' ')

def get_formatted_name(first_name,last_name,middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()
'''	
print("Enter 'q' to quit at any time.\n")

while True:
	first_name = input("Input the first name:")
	if first_name == 'q':
		break
	last_name = input("Input the last name:")
	if last_name == 'q':
		break
	full_name = get_formatted_name(first_name,last_name)
	print("full name is:"+full_name)
'''	

	