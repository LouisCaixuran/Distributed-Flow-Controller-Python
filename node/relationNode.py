from ../pifthon/pifthon import parse_json
import json
import secrets
import storeNode
from ../pifthon/language import execute
"""
relation node would work like the central node to process most request and send back information with labels on it
"""

class RelationNode:
	def __init__(self,json_file,address):
		self.user_inputs = json.load(open(json_file))
		ids=[]
		for i in self.user_inputs["configurations"]["global_vars"]:
			for j in i["label"]["readers"]:
				if j["id"] not in ids:
					ids.append(j["id"])

		self.keyMap=generateKey(ids)

		with open("../keys.json", "w") as outfile:
   	 		json.dump(self.keyMap, outfile)
		
		

		for i in self.user_inputs["configurations"]["global_vars"]:
			globals()[i["id"]] = createStoreNode(address[i["id"]])


		self.newJson=None

		listen()




	def generateLocalLabel(self,user):
		user=self.keyMap[user]
		self.user_inputs["configurations"]["label"]={"owner":user,"readers":[{"id":user}], "writer":[{"id":user}]}
		self.newJson=parse_json.JSONParser("",data=self.user_inputs)

	




	
			

	
#generate random 16 digit hex to replace each label ids
	def generateKey(self,ids):
		keyMap={}
		for i in ids:
			keyMap[i]=secrets.token_hex(16)

		for i in range(len(self.user_inputs["configurations"]["global_vars"])):
			self.user_inputs["configurations"]["global_vars"][i]["owner"]=keyMap[self.user_inputs["configurations"]["global_vars"][i]["owner"]]
			for j in range(len(self.user_inputs["configurations"]["global_vars"][i]["readers"])):
				self.user_inputs["configurations"]["global_vars"][i]["readers"][j]["id"]=keyMap[self.user_inputs["configurations"]["global_vars"][i]["readers"][j]["id"]]
			for j in range(len(self.user_inputs["configurations"]["global_vars"][i]["writers"])):
				self.user_inputs["configurations"]["global_vars"][i]["readers"][j]["id"]=keyMap[self.user_inputs["configurations"]["global_vars"][i]["readers"][j]["id"]]


		return keyMap;
	

	#Not finished, create a store node, would return the node
	def createStoreNode(data):
		return storeNode.StoreNode(data)



	#This is in pifthon/pifthon.py, statement is python code in string
	def run_pifthon(self,statement):
		tokens = []
    	temp_tokens = None
        try:
            temp_tokens = execute('<stdin>',statement, tokens, self.newJson)
        except Exception:
            return False
        else:
            	tokens += temp_tokens
            # print(tokens)
        return True
       

    #This is for communication between nodes
    def listen():

    	#TODO: get request from worker node

    	if pifthon(request):
    		#process
    	else:
    		#refuse
	
	