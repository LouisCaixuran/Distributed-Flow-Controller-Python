from pifthon_runner import PifthonRunner

#please check that file
pftester=PifthonRunner("./testJson.json")

#this should be maps between key and tokens
keyMap={"A":"1",
		"B":"2",
		"J":"3"}
#generate labels as tokens
pftester.generateLabels("A",keyMap)

label=pftester.getLabel(["alice","bob","john"])
#check if the user could access the list of address
print(label)

print(pftester.checkSecure(label))


#Only the first time need to generate all the labels in one workerNode. After that, only generate user label is enough
pftester.generateLabels("J")

#This would fail as bob not allow john to access
print(pftester.checkSecure(label))

#This would be success
newLabel=pftester.getLabel(["alice","john"])
print(pftester.checkSecure(newLabel))

#pftester.generateLabels("B")