salary = int(input('Salary?'))
default_fee = 27.
while default_fee > 0.:
	fee = input('Fee or 0 for exit')
	if not fee:
		fee = default_fee
		print("Real value: {0}".format(salary - (salary * (fee * 0.01))))
	else:
		fee = float(fee)
		print("Salary without fee: {0}".format(salary))
			 