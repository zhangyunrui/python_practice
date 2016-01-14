# -*- coding: utf-8 -*-
class Behave(object):
	def __init__(self, name):
		self.name = name
	def once(self):
		print "Hello,", self.name
	def rename(self, newName):
		self.name = newName
	def repeat(self, N):
		for i in range(N): self.once()

beehive = Behave("Queen Bee")
beehive.repeat(3)
beehive.rename("Stinger")
beehive.once()
print beehive.name
beehive.name = 'See, you can rebind it "from the outside" too, if you want'
beehive.repeat(2)


# 多态
class Repeater(object):
	def repeat(self, N):
		print N * "*-*"

aMix = beehive, Behave('John'), Repeater(), Behave('world')
for whatever in aMix:
	whatever.repeat(3)


# 重写
class Subclass(Behave):
	def once(self):
		print self.name

subInstance = Subclass("Queen Bee")
subInstance.repeat(3)


# 托管
class OneMore(Behave):
	def repeat(self, N):
		Behave.repeat(self, N+1)

zealant = OneMore("Worker Bee")
zealant.repeat(3)


# 用super实现托管
class OneMore(Behave):
	def repeat(self, N):
		super(OneMore, self).repeat(N+1)

zealant = OneMore("Worker Bee")
zealant.repeat(10)
