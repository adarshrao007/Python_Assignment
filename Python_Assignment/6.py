"""  Create a list with 5 branches in SOIS. Try to do the following operations a) append b) insert c) sort d) reverse sort """


branches = ["Embedded Systems", "IOT", "BDA", "Medical Software", "VIR"]
print(branches)

print("adding msc")
branches.append("MSC")
print(branches)

print("inserting ewt at 4rd pos")
branches.insert(3,"EWT")
print(branches)


print("Sorting in ascending order")
branches.sort()
print(branches)


print("sorting in descending order")
branches.sort(reverse = True)
print(branches)


