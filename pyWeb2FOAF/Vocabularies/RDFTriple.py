class RDFTriple: 	
	_subject
	_predicate
	_object
	
	def __init__(self, subject, predicate, object):
		self._subject   = subject
		self._predicate = predicate
		self._object    = object
		
	def setSubject(self, subject):
		self._subject = subject
		
	def getSubject(self):
		return self._subject
		
	def setPredicate(self, predicate):
		self._predicate = predicate
		
	def getPredicate(self):
		return self._predicate
		
	def setObject(self, object):
		self._object = object
		
	def getObject(self):
		return self._object