from ../pifthon/pifthon/rwfm import objects
from ../pifthon/pifthon import parse_json

"""
relation node would work like the central node to process most request and send back information with labels on it
"""

class RelationNode:
	def __init__(self,json_file,workerNodes,program):
		user_inputs = parse_json.JSONParser(json_files)