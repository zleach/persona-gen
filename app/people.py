import names
import random
import math
import data
import urllib
import string

import company as companies
import experiment as experiments


class Person(object):
  def __init__(self):
    # Gender
    self.gender = self.gender()
    self.genderTitle = self.genderTitle()
    self.genderPronoun = self.genderPronoun()
    self.genderPossessive = self.genderPossessive()

    # Basics
    self.firstName = names.get_first_name(self.gender)
    self.lastName = names.get_last_name()
    self.wearsGlasses = data.chance(40)
    if self.gender == 'male':
      self.bodyType = data.pick('male.body_type')
    else:
      self.bodyType = data.pick('female.body_type')
      
    self.avatar = Avatar(self)
    self.fullName = '%s %s' % (self.firstName,self.lastName)
  
    # Company
    self.company = companies.Company()  
  
    # Skills
    self.skills = []
  
  def calculateSkillValue(self):
    self.skillValue = 0
    for skill in self.skills:
      self.skillValue = self.skillValue + skill.level
  
  def gender(self):
    if(random.randint(0,99) > 50):
      return 'female'
    else:
      return 'male'

  def genderTitle(self):
    if(self.gender == 'male'): return 'he'
    if(self.gender == 'female'): return 'she'

  def genderPossessive(self):
    if(self.gender == 'male'): return 'his'
    if(self.gender == 'female'): return 'her'

  def genderPronoun(self):
    if(self.gender == 'male'): return 'man'
    if(self.gender == 'female'): return 'woman'
  
  def __str__(self):
    return self.fullName

class Skill(object):
  def __init__(self,name,minLevel,maxLevel):
    self.name = name
    
    icons = {
      'Coding' : 'code',
      'Reading Results' : 'line-chart',
      'Combining Data' : 'lightbulb-o',
      'Creativity + Communication' : 'paint-brush',
    }
    
    self.icon = icons[self.name]
    
    self.level = random.randint(minLevel/20,maxLevel/20)
    if self.level < 0:
      self.level = 0
    if self.level > 5:
      self.level = 5
    
class Avatar(object):  
  def __init__(self,person):
    self.backgroundColor = data.pick('color.background')
    self.pose = data.pick('unisex.pose')
    self.sex = 'unknown'
    self.height = data.pick('unisex.height')
    self.colorData = {
      'hair_color' : data.pick('hair.color'),
      'skin_tone' : data.pick('skin.tone'),
    }
    self.urlTemplate = 'https://da8lb468m8h1w.cloudfront.net//render/{pose}/{model}-v1.png?colours={colours}&pd2={pd2}&body={body}&cropped=%22body%22&proportion=0&sex={sex}&outfit={outfit}&crop_width=300&crop_height=240&style=1'
    self.colorTemplate = '{{%20%22ffcc99%22:%20{skin_tone}%20,%22{hair_color}}}'
    self.colours = self.colorTemplate.format(**self.colorData)
    self.pd2 = '{{{hair},%20%22jaw%22:%20%22{jaw}%22,{beard_stash},%20%22brow_L%22:%20%22{brow}%22,%20%22brow_R%22:%20%22{brow}%22,%20%22eye_L%22:%20%22{eye}%22,%20%22eye_R%22:%20%22{eye}%22,%20%22eyelines_L%22:%20%22eye_n3%22,%20%22eyelines_R%22:%20%22eye_n3%22,%20%22eyelid_L%22:%20%22eyelid_n1_3%22,%20%22eyelid_R%22:%20%22eyelid_n1_3%22,%20%22eyelash_L%22:%20%22{eyelash}%22,%20%22eyelash_R%22:%20%22{eyelash}%22,%20%22pupil_L%22:%20%22{pupil}%22,%20%22pupil_R%22:%20%22{pupil}%22,%20%22nose%22:%20%22{nose}%22,{mouth_tongue},%20%22ear_L%22:%20%22{ear}%22,%20%22ear_R%22:%20%22{ear}%22,%20%22detail_E_L%22:%20%22detail_E_n2%22,%20%22detail_E_R%22:%20%22detail_E_n2%22,%20%22detail_L%22:%20%22_blank%22,%20%22detail_R%22:%20%22_blank%22,%20%22detail_T%22:%20%22_blank%22,%20%22glasses%22:%20%22{glasses}%22%20}}'

    if person.gender == 'male':
      # Male
      self.body = '{%20%22body_height%22:%20'+self.height+',%20%22body_type%22:%20'+person.bodyType+'%20}'
      self.sex = '1'
      self.model = '120449915_1_s1'
      self.outfit = data.pick('outfits.male')
      self.glasses = data.pick('male.glasses')
      self.hair = data.pick('male.hair')
      self.pd2Data = {
        'hair' : self.hair,
        'nose' : data.pick('male.nose'),
        'ear' : data.pick('male.ear'),
        'eye' : data.pick('male.eye'),
        'eyelash' : 'eyelash_blank',
        'beard_stash' : data.pick('male.beard_stash'),
        'jaw' : data.pick('male.jaw'),
        'pupil' : data.pick('male.pupil'),
        'mouth_tongue' : data.pick('male.mouth_tongue'),
        'brow' : data.pick('male.brow'),
        'glasses' : 'glasses_blank',
      }    
      if person.wearsGlasses:
        self.pd2Data['glasses'] = self.glasses
      
    else:
      # Female
      self.breast_type = data.pick('female.breast_type')
      self.body = '{%20%22body_height%22:%20'+self.height+',%20%22body_type%22:%20'+person.bodyType+'%20,%22breast_type%22:'+self.breast_type+'}'
      self.sex = '2'
      self.model = '108768741_1_s1'
      self.outfit = data.pick('outfits.female')
      self.glasses = data.pick('female.glasses')
      self.hair = data.pick('female.hair')    
      self.pd2Data = {
        'hair' : self.hair,
        'nose' : data.pick('male.nose'),
        'ear' : data.pick('male.ear'),
        'eye' : data.pick('male.eye'),
        'eyelash' : data.pick('female.eyelash'),
        'beard_stash': '%20%22beard%22:%20%22beard_blank%22,%20%22stachin%22:%20%22stachin_blank%22,%20%22stachout%22:%20%22stachout_blank%22',
        'jaw' : data.pick('male.jaw'),
        'pupil' : data.pick('male.pupil'),
        'mouth_tongue' : data.pick('male.mouth_tongue'),
        'brow' : data.pick('male.brow'),
        'glasses' : 'glasses_blank',
      }    
      if person.wearsGlasses:
        self.pd2Data['glasses'] = self.glasses
    
    d = {
      'model' : self.model,
      'sex' : self.sex,
      'pose' : self.pose,
      'outfit' : self.outfit,
      'colours': self.colours,
      'pd2' : self.pd2.format(**self.pd2Data),
      'body' : self.body
     }

    self.url =  self.urlTemplate.format(**d)
    self.faceUrl = self.url.replace('cropped=%22body','cropped=%22head')
    self.faceUrl = self.faceUrl.replace(self.pose,'6688424')
      
  def __str__(self):
    return self.url;

class LoneWolf(Person):
  def __init__(self):
    Person.__init__(self)
    self.archetype = 'Lone Wolf'
    self.image = 'wolf.svg'

    balance = 0
    self.title = data.pick('company.title.marketing')
    self.skills.append(Skill('Coding'       ,40-balance,90-balance))
    self.skills.append(Skill('Reading Results',60-balance,90-balance))
    self.skills.append(Skill('Combining Data' , 0-balance,40-balance))
    self.skills.append(Skill('Creativity + Communication'  ,40-balance,80-balance))
    self.calculateSkillValue();
   
class Strategist(Person):
  def __init__(self):
    Person.__init__(self)
    self.archetype = 'Strategist'
    self.image = 'strategist.svg'

    balance = 0
    self.title = data.pick('company.title.strategist')
    self.skills.append(Skill('Coding'       ,0-balance,50-balance))
    self.skills.append(Skill('Reading Results',0-balance,90-balance))
    self.skills.append(Skill('Combining Data' ,0-balance,40-balance))
    self.skills.append(Skill('Creativity + Communication'     ,70-balance,100-balance))
    self.calculateSkillValue();

class Implementer(Person):
  def __init__(self):
    Person.__init__(self)
    self.archetype = 'Implementer'
    self.image = 'implementer.svg'
    
    balance = 10
    self.title = data.pick('company.title.developer')
    self.skills.append(Skill('Coding', 40-balance,100-balance))
    self.skills.append(Skill('Reading Results',30-balance,60-balance))
    self.skills.append(Skill('Combining Data' ,0-balance,30-balance))
    self.skills.append(Skill('Creativity + Communication'     ,30-balance,50-balance))
    self.calculateSkillValue();

class Developer(Person):
  def __init__(self):
    Person.__init__(self)
    self.archetype = 'Developer'
    self.image = 'developer.svg'

    balance = 10
    self.title = data.pick('company.title.developer')
    self.skills.append(Skill('Coding'       ,90-balance,100-balance))
    self.skills.append(Skill('Reading Results',0-balance,30-balance))
    self.skills.append(Skill('Combining Data' ,0-balance,30-balance))
    self.skills.append(Skill('Creativity + Communication'     ,0-balance,30-balance))
    self.calculateSkillValue();

class Analyst(Person):
  def __init__(self):
    Person.__init__(self)
    self.archetype = 'Analyst'
    self.image = 'analyst.svg'
    
    balance = 20
    self.title = data.pick('company.title.analyst')
    self.skills.append(Skill('Coding'       ,30-balance,60-balance))
    self.skills.append(Skill('Reading Results',90-balance,100-balance))
    self.skills.append(Skill('Combining Data' ,90-balance,100-balance))
    self.skills.append(Skill('Creativity + Communication'     ,20-balance,50-balance))
    self.calculateSkillValue();


