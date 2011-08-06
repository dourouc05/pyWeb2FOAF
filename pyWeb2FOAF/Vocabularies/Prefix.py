"""
A prefix used by a vocabulary. 
"""

class Prefix: 
	def __init__(self, prefix, uri):
		self._prefix = prefix
		self._uri    = uri
		
	@property
	def prefix(self)
		return self._prefix
		
	@prefix.setter
	def prefix(self, prefix)
		self._prefix = prefix
		
	@property
	def uri(self)
		return self._uri
		
	@uri.setter
	def uri(self, uri)
		self._prefix = uri