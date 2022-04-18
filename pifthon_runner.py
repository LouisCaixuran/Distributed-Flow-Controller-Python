from pifthon.pifthon.parse_json import JSONParser
import json
import copy
from pifthon.pifthon.language import execute
import random


class PifthonRunner:
	#init_json is the initial json file like pifthon
	def __init__(self, init_json):
		self.originJson=json.load(open(init_json))
		self.currentLabel=[]



		for i in self.originJson["configurations"]["global_vars"]:
			self.currentLabel.append((i["id"],i["label"]["owner"],i["label"]["readers"],i["label"]["writers"]))

		self.labelInfo=None
		
		self.originL={"configurations":{
				"file_name": "friendMap.py",
				"parallel":"false",
				"subject":"S",
				"label":{
					"owner" : "S",
					"readers": [],
					"writers": []
				 },
				"global_vars": [],
				"method_label": [],
				"threads": [] }
				}
		self.finalL=copy.deepcopy(self.originL)


	#with keyMap like {id:token}, it would generate labels for each global variables and generate local variable label which could access everything
	def generateGlobalLabels(self,keyMap):
		for i in self.currentLabel:
			tmpLabel={
					"id":i[0],
					"label": {
						"owner" : i[1],
						"readers": [],
						"writers": []}
					}
			tmpR=[]
			for j in i[2]:
				tmpR.append({"id":keyMap[j["id"]]})
			tmpW=[]
			for j in i[3]:
				tmpW.append({"id":keyMap[j["id"]]})
			tmpLabel["label"]["readers"]=tmpR
			tmpLabel["label"]["writers"]=tmpW
			self.finalL["configurations"]["global_vars"].append(tmpLabel)
		for i in keyMap.values():
			self.finalL["configurations"]["label"]["writers"].append({"id":i})

	#with keymap and userName, it would generate a label for the user variable to check in pifthon
	def generateUserLabels(self,user,keyMap):
		tempLabel={
					"id":"finalDestination",
					"label": {
						"owner" : user,
						"readers": [{"id":keyMap[user]}],
						"writers": []}
					}
		for i in keyMap.values():
			tempLabel["label"]["writers"].append({"id":i})
		self.finalL["configurations"]["global_vars"].append(tempLabel)

		
	#generate everything needed and change it to structure pifthon needed
	def generateLabels(self,user,keyMap=None):
		if keyMap==None:
			keyMap=self.keyMap
		else:
			self.keyMap=keyMap
		self.generateGlobalLabels(keyMap)
		self.generateUserLabels(user,keyMap)
		self.labelInfo=JSONParser("",data=self.finalL)
		self.finalL=copy.deepcopy(self.originL)


	def generateStatement(self,requestList):
		statement=""
		userS="tmp="
		for i in requestList:
			statement=statement+i+"="+str(random.random())+"\n"
			userS=userS+i+"+"

		statement=statement+userS[:-1]+"\n"
		return statement+"finalDestination=tmp"





	def checkSecure(self,requestList):
		statement=self.generateStatement(requestList)
		print(statement)
		return self.run_pifthon(statement,self.labelInfo)


	def run_pifthon(self,statement,labelinfo):
		tokens = []
		temp_tokens = None
		try:
			temp_tokens = execute('<stdin>',statement, tokens, labelinfo)
		except Exception:
			#print(tokens)
			return False
		else:
			tokens += temp_tokens
			#print(tokens)
		return True
	   