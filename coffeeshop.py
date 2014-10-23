import six
from abc import ABCMeta

########################################################################
@six.add_metaclass(ABCMeta)
class Abstract_Coffee(object):
	""" The decorator syntax above this class definition 
	means that this is an abstract class, 
	and cannot itself be instantiatied. 
	"""

	def getCost(self):
		# An abstract cup of coffee has no cost, 
		# so returns None. However, including this 
		# definition is important because 
		# our coffee decorator objects 
		# like Sugar and Milk will assume they 
		# can inherit the getCost behavior from 
		# the decorated_coffee objects 
		# passed to their __init__ constructors. 
		# Since Sugar and Milk will only only ever 
		# be passed concrete instances of 
		# subclasses of the abstract_coffee class, 
		# including this definition here guarantees 
		# that the required behavior will be inherited. 
		# See below. 
		pass

	def getIngredients(self):
		# Same comments apply here as in 
		# the definition of the getCost method above.
		pass

########################################################################
class Concrete_Coffee(Abstract_Coffee):
	""" Concrete subclass of abstract_coffee. 
	This class does permit instantiation."""

	def getCost(self):
		# Override the getCost method of the abstract class.
		return 1.00

	def getIngredients(self):
		# Override the getIngredients method of the abstract class.
		return 'coffee'

########################################################################
@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstract_Coffee):
	""" Abstract base class for all decorators of coffee objects. 

	Note the following critical feature of this class: 
	the __init__ constructor is passed a 
	decorated_coffee object. This class will presume 
	that the passed decorated_coffee object 
	is a concrete instance of some subclass of abstract_coffee. 
	In particular, it is presumed that 
	the passed decorated_coffee object 
	carries with it the getCost and getIngredients methods. 

	"""

	def __init__(self,decorated_coffee):
		""" Bind the passed abstract_coffee object 
		to the class instance. This way, the methods 
		of this class will inherit the baseline behavior 
		of the abstract_coffee super class.
		"""
		self.decorated_coffee = decorated_coffee

	def getCost(self):
		# Inherit the behavior of getCost from the abstract_coffee super class.
		return self.decorated_coffee.getCost()

	def getIngredients(self):
		# Inherit the behavior of getIngredients from the abstract_coffee super class.
		return self.decorated_coffee.getIngredients()

########################################################################
class Sugar(Abstract_Coffee_Decorator):

	def __init__(self,decorated_coffee):
		""" We need to bind the decorated_coffee object 
		to the Sugar class, so that we can inherit its behavior. 
		We could do this as above, 
		via self.decorated_coffee = decorated_coffee. 
		Or we can rely on the __init__ constructor 
		of the super class to do this.
		"""
		Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
		# Formally equivalent approach not taken here:
		# self.decorated_coffee = decorated_coffee

	def getCost(self):
		# Sugar is usually free
		return self.decorated_coffee.getCost()

	def getIngredients(self):
		""" Now for the first example of decoration. 
		This is an override of the 
		inherited getIngredients method, with some 
		new behavior added on. 
		"""
		return self.decorated_coffee.getIngredients() + ', sugar'

########################################################################
class Milk(Abstract_Coffee_Decorator):

	def __init__(self,decorated_coffee):
		Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

	def getCost(self):
		# Milk is usually free, 
		# but for illustration purposes, 
		# let's suppose this coffee shop charges 
		# an additional $0.25 for it.
		return self.decorated_coffee.getCost() + 0.25

	def getIngredients(self):
		return self.decorated_coffee.getIngredients() + ', milk'

########################################################################
class Vanilla(Abstract_Coffee_Decorator):

	def __init__(self,decorated_coffee):
		Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

	def getCost(self):
		return self.decorated_coffee.getCost() + 0.75

	def getIngredients(self):
		return self.decorated_coffee.getIngredients() + ', vanilla'

