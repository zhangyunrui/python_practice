# -*- coding: utf-8 -*-
def no_new_attributes(wrapped_setattr):
	def _setattr(self, name, value):
		if hasattr(self, name):
			wrapped_setattr(self, name, value)
			# object.__setattr__(self, name, value)
		else:
			raise AttributeError("can't add attribute %r to %s" %(name, self))
		return _setattr


class Person(object):
	firstname = 'A'

	def __init__(self, firstname):
		self.firstname = firstname


me = Person('B')
# _setattr(me, 'firstname', 'Michere')
# no_new_attributes(me.__setattr__('firstname', 'Michere'))
# _setattr(me, 'lastname', 'SMichere')
# no_new_attributes(object.__setattr__(me, 'lastname', 'SMichere'))
no_new_attributes(me.__setattr__('lastname', 'SMichere'))
print me.firstname
print me.lastname




# class NoNewAttrs(object):
# 	__setattr__ = no_new_attributes(object.__setattr__)
# 	class __metaclass__(type):
# 		__setattr__ = no_new_attributes(object.__setattr__)


# new = NoNewAttrs()
# new.firstname = 'C'
# print new.firstname


# class Person(NoNewAttrs):
# # class Person(object):
# 	firstname = ''
# 	lastname = ''
#
# 	def __init__(self, firstname, lastname):
# 		self.firstname = firstname
# 		self.lastname = lastname

	# def __repr__(self):
	# 	return 'Person(%r, %r)' %(self.firstname, self.lastname)





# me = Person('Michere', 'Simionato')
# print me.firstname
# me.firstname = "Michele"
# print me
# try:
# 	Person.address = ''
# except AttributeError, err: print 'raised %r as expected' %err
# try:
# 	me.address = ''
# except AttributeError, err: print 'raised %r as expected' %err
