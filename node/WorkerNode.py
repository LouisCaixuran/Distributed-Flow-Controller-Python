import threading
import time

"""
worker node is the node to run exact programs and pifthon to analysis it
"""

class WorkerNode():
	"""
	initial the store node
	@name : String  the name of the Node
	@nodePrinciple : Principle for the node
	@remoteS : list of storeNodes name
  @objs : objs need to use in this worker for init
	"""
	def __init__(self, name, nodePrinciple, remoteS, objs ):
  		self.name=name
  		self.nodePrinciple=nodePrinciple
  		self.remoteS= remoteS
  		self.principles=request(self.remoteS,objs);
      self.threads=[];

  """
  request principles of objs needed from the storeNode
  """
  def request(remoteS,objs):
    pass 

  #load program and run pifthon locally for it
  def set_program(path):
    pass

  def updateP(type, name, oldP, newP):
    pass
  	