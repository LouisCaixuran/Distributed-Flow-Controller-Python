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

pftester.generateLabels("J",keyMap)

print(pftester.checkSecure(["alice","bob","john"]))