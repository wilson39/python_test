#!/usr/bin/env python


import my_func

path = '/home/wilson/Downloads/log.txt'

def  test_log_file():


	info_count, warn_count,error_count = my_func.count_no(path)

	
	assert info_count == 50
	assert warn_count == 11
	assert error_count == 30


test_log_file()	
