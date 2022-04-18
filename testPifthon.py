from pifthon_runner import PifthonRunner

#please check that file
pftester=PifthonRunner("./testJson.json")

#this should be maps between key and tokens
keyMap={"A":"1",
		"B":"2",
		"J":"3"}
#generate labels as tokens
pftester.generateLabels("A",keyMap)

#check if the user could access the list of address
print(pftester.checkSecure(["alice","bob","john"]))


#Only the first time need to generate all the labels in one workerNode. After that, only generate user label is enough
pftester.generateLabels("J")

#This would fail as bob not allow john to access
print(pftester.checkSecure(["alice","bob","john"]))

#This would be success
print(pftester.checkSecure(["alice","john"]))