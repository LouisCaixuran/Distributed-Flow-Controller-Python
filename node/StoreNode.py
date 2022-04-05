import json
import threading
import time

"""
StoreNode is to store all the labels and ensure untrust host could not attend high security level information
"""

class StoreNode():
	"""
	initial the store node
	@name : String  the name of the Node
	@nodePrinciple : Principle for the node
	@principles : path of jason file which store all the principles
	"""
	def __init__(self, name, nodePrinciple, principles ):
  		self.name=name
  		self.nodePrinciple=nodePrinciple
  		self.principle_file=principles
  		self.workers=[]
  		with open('data.json') as json_file:
  			self.principles = json.load(json_file)
  		self.synThread=threading.Thread(target=synch_thread,args=(1,))

  		self.synThread.start();

  	"""
	@request_tyoe: var, function or thread
	@worker: the worker name request the principle
	@specific name of the object it required
	@rw: read or write
  	"""
  	def checkPrinciple(request_type,worker,name, rw):
  		pass


  	# get the node principle
    def getNodPrincipal():
    	return self.nodePrinciple
    
    def getVarP(worker, varN):
    	if(checkPrinciple("var", worker, varN, "r")):
    		return self.principles["global_vars"][varN]
    	return None


    def getFunP(worker, funN):
    	if(checkPrinciple("fun", worker,"r")):
    		return self.principles["method_label"][funN]
    	return None

    def getThreadP(worker, threadN):
    	if(checkPrinciple("thread", worker,"r")):
    		return self.principles["threads"][threadN]
    	return None


    def setVarP(worker, varN, oldP, newP):
    	if(checkPrinciple("var", worker,"w")):
    		return update("var", varN, oldP, newP)
    		
    	return False

    def setFunP(worker, funN, oldP, newP):
    	if(checkPrinciple("fun", worker,"w")):
    		return update("fun", funN, oldP, newP)
    		
    	return False

    def removeWorker(worker, threadN, oldP, newP):
    	if(checkPrinciple("thread", worker,"w")):
    		return update("thread", threadN, oldP, newP)		
    	return False




    def update(type, name, oldPrinciple, newPrinciple):
    	pass

    def synchronize(worker):
    	pass

    def synch_thread():
    	while True:
    		time.sleep(5)
    		for worker in self.workers:
    			synchronize(worker)


    def addWorker(worker, workerPrinciple, workerObjs){
    	newWorker={
    		"workerName": worker,
    		"nodePrinciple": workerPrinciple,
    		"workerObjs": workerObjs
    	}
    	self.workers.append(worker)

    }