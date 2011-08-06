"""
A RDF triple (output of vocabularies for use by output modules)

This class is used to represent an RDF triple of any ontology.
It will be used by classes in the OUTPUT directory to determine
each RDF triple that should contain the output RDF file.
"""

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
