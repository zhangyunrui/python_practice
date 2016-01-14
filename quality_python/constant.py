class _const:
	class ConstError(TypeError): pass
	class ConstCaseError(ConstError): pass

	def __setattr__(self, name, value):
		if self.__dict__.has_key(name):
			raise self.ConstError, "Can't change const.{const_name}".format(const_name=name)
		if not name.isupper():
			raise self.ConstCaseError, "const name {const_name} need uppercase".format(const_name=name)
		self.__dict__[name] = value


import sys
sys.modules[__name__] = _const()
# import const
const.MY_CONSTANT = 1