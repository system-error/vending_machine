coins = [[2,20],[1,20],[0.5,20],[0.2,40],[0.1,40],[0.05,100]]

answer = 'y'
while answer == 'y':
	payment = float(input("Payment amount: "))
	inserted = float(input("Inserted amount: "))

	change = round(inserted - payment,2)
	pos = 0
	while change > 0:
		print(coins[0][1])
		print(change)
		print(pos)
		if coins[pos][0] > change or coins[pos][1] == 0:
			if pos < len(coins) - 1:
				pos += 1
			else:
				print("Sorry, no more change")
				break	
			continue

		print ("Give change ", coins[pos][0])
		change = round(change - coins[pos][0])
		coins[pos][1] -= 1
	answer = input("Continue? ") 		
#testing
