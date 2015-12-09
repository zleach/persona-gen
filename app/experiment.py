import names
import random
import math
import data
import string

class Skill(object):
  def __init__(self,name,minLevel,maxLevel):
    self.name = name
    self.level = random.randint(minLevel/20,maxLevel/20)
    if self.level < 0:
      self.level = 0
    if self.level > 5:
      self.level = 5



class Experiment(object):
  def __init__(self):
    balance = 0
    self.name = data.pick('experiment.name')
    self.skills = []
    self.skills.append(Skill('Coding'         ,0,100))
    self.skills.append(Skill('Reading Results',0,100))
    self.skills.append(Skill('Combining Data' ,0,100))
    self.skills.append(Skill('Creativity + Communication'     ,0,100))

    self.skillValue = 0
    for skill in self.skills:
      self.skillValue = self.skillValue + skill.level
      self.skillValue = (self.skillValue/3)+1

    self.resultValue = str(round(self.skillValue * random.uniform(1,2),0)).rstrip('.0');
    
  def __str__(self):
    return self.name
