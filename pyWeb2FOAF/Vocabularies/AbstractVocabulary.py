"""
Interface for vocabularies
"""

class AbstractVocabulary:
	def __init__(self)
		raise NotImplementedError("Abstract class")
	
	def getTriples(self):
		raise NotImplementedError("Abstract class")

	def getPrefix(self):
		raise NotImplementedError("Abstract class")
