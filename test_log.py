
import re

''' This is a simple read function witch takes file name with full file path as
 argument and returns content of file ex. read_file('/tmp/a.txt')'''


def read_file(file_path):

	with open(file_path, 'r') as read_file:

		file_cont = read_file.read()

	return file_cont

'''Simple regex to find INFO, ERROR, WARRING from files'''

info = re.compile(r'INFO')
warn = re.compile(r'WARNING')
error = re.compile(r'ERROR')

 
#log_data = read_file (r'C:\Users\Admin\Downloads\log.txt')#('/home/wilson/Downloads/log.txt')
#all_result = warn.findall(log_data)



'''' This is simple function which return count of INFO, WARNNING and ERROR froma file'''

def count_no(file_name):

	file_data = read_file(file_name)

	info_count = info.findall(file_data)
	warn_count = warn.findall(file_data)
	error_count = error.findall(file_data)

	info_count = len(info_count)
	warn_count = len(warn_count)
	error_count = len(error_count)

	return(info_count, warn_count,error_count)
	
'''pytest verification '''
file_name = r'C:\Users\Admin\Downloads\new_log.txt'
def  test_log_file():

	info_count, warn_count,error_count = count_no(file_name)

	assert info_count == 50
	assert warn_count == 11
	assert error_count == 30


test_log_file()		

