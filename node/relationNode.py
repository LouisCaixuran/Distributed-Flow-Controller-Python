from ../pifthon/pifthon/rwfm import objects
from ../pifthon/pifthon import parse_json
import storeNode

"""
relation node would work like the central node to process most request and send back information with labels on it
"""

class RelationNode:
	def __init__(self,json_file):
		user_inputs = parse_json.JSONParser(json_files)
		self.globals=user_inputs.getGlobals()
		self.storeNodes=[]
		self.workerNodes=[]
		self.tmpJson={
		global_vars:[]
		}
		



	def create_StoreNode(label,value=None):
		

