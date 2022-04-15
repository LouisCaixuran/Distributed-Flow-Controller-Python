
#This function is used for pifthon, which should be in string format, which could generate x with user list, and pifthon would check if its flow is secure

re="""def request(address, requestList):
	alice=address["alice"]
	bob=address["bob"]
	john=address["john"]

	for i in requestList:
		x=x+i

	return x"""