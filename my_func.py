#!/usr/bin/env python



import re

''' This is simple read function with take file name with full file path and returns content of file
     ex. read_file('/tmp/a.txt')'''


def read_file(file_path):

	with open(file_path, 'r') as read_file:

		file_cont = read_file.read()

	return file_cont

'''Simple regex to find INFO, ERROR, WARRING from files'''

info = re.compile(r'INFO')
warn = re.compile(r'WARNING')
error = re.compile(r'ERROR')

 
data = read_file('/home/wilson/Downloads/log.txt')
all_result = warn.findall(data)



'''' This is simple function which return count of INFO, WARNNING and ERROR froma file'''

def count_no(file):

	file_data = read_file(file)

	info_count = info.findall(file_data)
	warn_count = warn.findall(file_data)
	error_count = error.findall(file_data)

	info_count = len(info_count)
	warn_count = len(warn_count)
	error_count = len(error_count)

	return(info_count, warn_count,error_count)


	









