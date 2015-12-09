import names
import random
import math
import data
import string

class Company(object):
  def __init__(self):
    self.name = names.get_company_name()
    
  def __str__(self):
    return self.name
