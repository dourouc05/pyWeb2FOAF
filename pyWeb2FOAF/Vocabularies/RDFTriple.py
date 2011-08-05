class RDFTriple: 		
	def __init__(self, subject, predicate, obj):
		self._subject   = subject
		self._predicate = predicate
		self._obj       = obj
	
	@property 
	def subject(self):
		return self._subject

	@subject.setter
	def subject(self, subject):
                self._subject = subject

	@property
	def predicate(self):
		return self._predicate

	@predicate.setter	
	def predicate(self, predicate):
		self._predicate = predicate

	@property
	def obj(self):
		return self._obj

	@obj.setter
	def obj(self, obj):
		self._obj = obj
