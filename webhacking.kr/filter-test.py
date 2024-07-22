filters = input("filter text(split:,): ").split(",")
query = input("query text: ")

for filter in filters:
	if filter in query:
		print("filter: {}".format(filter))
		break

else: print("no filtering")
