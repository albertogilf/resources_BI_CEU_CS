import sys
sys.path.append('../')
import numpy
from datetime import datetime, date
import random
from utils import Utils
from exceptions.ErrorMouse import ErrorMouse
from animals.EnumsMouse import Gender, Chromosome

#!/usr/bin/env python

"""Mouse.py: Mouse Class for representing the animals of a population"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"

class Mouse: 

  num_reference = 0 
  def __init__(self, reference=None, name=None, birthdate=date.today(), weight=None, gender=None, temperature=None, description="",  probabilityMutation=0.2, chromosome1=None, chromosome2=None):
    """ Constructor of Mouse
      It creates a mouse
      :param reference: Unique identifier of the mouse. Assigned auto incrementally by default
      :param name: By default a name between mouse1 and mouse6
      :param birthdate: Date of birth. By default, the day of the creation
      :param weight: Weight of the mouse. By default, a number between 50 and 100
      :param gender: enum to represents males and females. By default, random.
      :param temperature: Weight of the mouse. By default, a number between 36 and 38
      :param description: By default, and empty description
      :param probabilityMutation Probability of suffer mutations
      :param chromosome1: chromosome1 if None, it will be calculated based on the probability of mutations
      :param chromosome2: chromosome2 if None, it will be calculated based on the probability of mutations
      :type reference: int > 0
      :type name: string
      :type birthdate: date
      :type weight: real > 0
      :type gender: GENDER
      :type temperature: real > 0
      :type description: string
      :type probabilityMutation: real [0-1]
      :type chromosome1: CHROMOSOME
      :type chromosome2: CHROMOSOME
      :raises ErrorMouse when any of the arguments do not fulfill the type specified
    """
    if (isinstance(reference,int) and reference > 0):
      self.__reference= reference 
      if(reference > Mouse.num_reference):
        Mouse.num_reference = reference
    else:
      Mouse.num_reference += 1
      self.__reference = Mouse.num_reference

    if name == None:
      self.__name = Mouse.__generate_random_name()
    else:
      self.set_name(name)

    if isinstance(birthdate, date):
      if(birthdate > date.today()):
        raise ErrorMouse("Date of birth cannot be a future date")
      else:
        self.__birthdate= birthdate
    else:
      raise ErrorMouse("Date of birth should be a date")  

    if(weight == None):
      weight = random.uniform(50,100)
    try:
      self.set_weight(weight)
    except Exception as e:
      raise ErrorMouse(str(e)) 

    if isinstance(gender, Gender):
      self.__gender= gender
    elif gender == None:
      try:
        gender = Mouse.__generate_random_gender()
        self.__gender = gender
      except ValueError:
        raise ErrorMouse("Error generating a gender randomly")
    else:
      raise ErrorMouse("Gender should be a variable of the enum Gender")

    if not (isinstance(chromosome1, Chromosome) and isinstance(chromosome2, Chromosome)):
      if(isinstance(probabilityMutation,(int,float)) and probabilityMutation >= 0 and probabilityMutation <= 1):
        chromosomes = Mouse._generate_random_chromosomes(gender,probabilityMutation)
        self.__chromosome1 = chromosomes[0]
        self.__chromosome2 = chromosomes[1]
      else:
        raise ErrorMouse("Chromosomes should be Chromosome type or probability number should be a number between 0 and 1")
    else:
      self.__chromosome1 = chromosome1
      self.__chromosome2 = chromosome2

    if (temperature == None):
      temperature = random.uniform(36,38)
    try:
      self.set_temperature(temperature)
    except Exception as e:
      raise ErrorMouse(str(e)) 

    if description == None:
      self.__description = ""
    else:
      self.set_description(description)



  def get_reference(self):
    return self.__reference

  def get_name(self):
    return self.__name

  def set_name(self, name):
    if name == None:
      pass
    elif isinstance(name,str):
      self.__name=name
    else:
      self.__name = str(name)

  def get_birthdate(self):
    return self.__birthdate

  def get_weight(self):
    return self.__weight

  def set_weight(self, weight):
    if isinstance(weight,(int,float)):
      if(weight >= 0):
        self.__weight=weight
      else:
        raise ValueError("Weight should be positive") 
    else:
      raise TypeError("Weight should be a number")

  def get_gender(self):
    return self.__gender

  def get_temperature(self):
    return self.__temperature

  def set_temperature(self, temperature):
    if isinstance(temperature, (int,float)):
      if(temperature >= 0):
        self.__temperature = temperature
      else:
        raise ValueError("Temperature should be positive") 
    else:
      raise TypeError("Temperature should be a Number")

  def get_description(self):
    return self.__description

  def set_description(self, description):
    if description == None:
      pass
    elif isinstance(description,str):
      self.__description=description
    else:
      self.__description = str(description)

  def get_chromosome1(self):
    return self.__chromosome1

  def get_chromosome2(self):
    return self.__chromosome2

  def is_steril(self):
    '''
    function to check if the mouse is steril
    :return true if the mouse if steril, false otherwise
    :rtype boolean
    '''
    if(self.__gender == Gender.FEMALE):
      if(self.__chromosome1 == Chromosome.X_MUTATED and self.__chromosome2 == Chromosome.X_MUTATED):
        return True
      else:
        return False
    elif(self.__gender == Gender.MALE):
      if(self.__chromosome1 == Chromosome.X_MUTATED):
        return True

  def is_poligamic(self):
    '''
    function to check if the mouse is poligamic
    :return true if the mouse if poligamic, false otherwise
    :rtype boolean
    '''
    if(self.__gender == Gender.MALE and self.__chromosome2 == Chromosome.Y_MUTATED):
      return True
    return False


  def valuesToCSV(self):
    return  (str(self.__reference) + "," + str(self.__name) + "," + str(self.__birthdate) + "," + str(self.__weight)+ ","+ str(self.__gender)+ "," + str(self.__temperature) + "," + str(self.__description) + "," + str(self.__chromosome1) + "," + str(self.__chromosome2))


  def __str__(self):
    return  ("ref: "+ str(self.__reference) + ", name: " + str(self.__name) + ", birthdate: " +str(self.__birthdate) + ", weight: "+ str(self.__weight)+", gender: "+ str(self.__gender)+ ", temperature: " +str(self.__temperature)+", description: "+str(self.__description))


  def __hash__(self):
    return hash(self.__reference)

  def __eq__(self,other):
    if isinstance(other,self.__class__):
        return self.__reference==other.__reference
    else:
        return False

  def __repr__(self):
    return ("Reference: " + str(self.__reference) +  ", Name: " + str(self.__name)) + ", gender " + str(self.__gender)

  @staticmethod
  def __generate_random_name():
    '''
    It returns a name from mouse1 to mouse6
    :return the name of the mouse randomly generated 
    :rtype string
    '''
    listMouses = ["mouse1", "mouse2", "mouse3", "mouse4", "mouse5", "mouse6"]
    return Utils.get_random_str_from_list(listMouses)

  @staticmethod
  def __generate_random_gender():
    '''
    It returns a gender MALE or FEMALE
    :return the gender of the mouse randomly generated 
    :rtype Gender
    '''
    gender = numpy.random.choice(list(Gender)) 
    return gender

  @staticmethod
  def _generate_random_chromosomes(gender, probabilityMutation):
    '''
    It returns a list with two chromosomes according to the probability of mutations and the gender
    :param gender: 
    :param probabilityMutation a number between 0 and 1 containing the probability of suffering a mutation
    :type gender: Gender
    :type probabilityMutation: float [0-1]
    :return a list with two chromosomes according to the gender 
    :rtype list(Chromosome)
    :raises Value error when any of the arguments do not fulfill the type specified
    '''
    if not isinstance(gender, Gender):
      raise ValueError("Gender not valid")
    
    choice = random.uniform(0, 1)
    if(choice > probabilityMutation):
      chromosome1 = Chromosome.X
      if(gender == Gender.FEMALE):
        chromosome2 = Chromosome.X
      else:
        chromosome2 = Chromosome.Y
    else:
      chromosome1 = Mouse._generate_random_chromosomeX()
      if(chromosome1 == Chromosome.X_MUTATED):
        if(gender == Gender.FEMALE):
          chromosome2 = Mouse._generate_random_chromosomeX()
        else:
          chromosome2 = Mouse._generate_random_chromosomeY()
      else:
        if(gender == Gender.FEMALE):
          chromosome2 = Chromosome.X_MUTATED
        else:
          chromosome2 = Chromosome.Y_MUTATED
    return[chromosome1,chromosome2]

  @staticmethod
  def _generate_random_chromosomeY():
    '''
    It returns a Chromosome according to the probability of mutations 
    :return the chromosome randomly calculated
    :rtype Chromosome
    '''
    chromosomeY = numpy.random.choice([Chromosome.Y,Chromosome.Y_MUTATED]) 
    return chromosomeY

  @staticmethod
  def _generate_random_chromosomeX():
    '''
    It returns a Chromosome according to the probability of mutations
    :return the chromosome randomly calculated
    :rtype Chromosome
    '''
    chromosomeX = numpy.random.choice([Chromosome.X,Chromosome.X_MUTATED]) 
    return chromosomeX



def main():
  
  prob_mutated=0.5
  chromosomes_male = Mouse._generate_random_chromosomes(Gender.MALE,prob_mutated)
  chromosomes_female = Mouse._generate_random_chromosomes(Gender.FEMALE,prob_mutated)
  print(chromosomes_male)
  print(chromosomes_female)
  try:
    Mouse._generate_random_chromosomes(None,prob_mutated)
  except ValueError as ve:
    print("Test random chromosomes passed")
  try:
    mouse1 = Mouse()
    print(mouse1)
    maleesteril=Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.Y_MUTATED)
    if(maleesteril.is_steril() and not maleesteril.is_poligamic()):
      print("Male only steril test passed")
    malepoligamic=Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X, chromosome2=Chromosome.Y_MUTATED)
    if(not malepoligamic.is_steril() and malepoligamic.is_poligamic()):
      print("Male only poligamic test passed")
    malesterilpoligamic=Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.Y_MUTATED)
    if(malesterilpoligamic.is_steril() and malesterilpoligamic.is_poligamic()):
      print("Male steril and poligamic test passed")
    malenormal=Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.Y_MUTATED)
    if(not malenormal.is_steril() and not malenormal.is_poligamic()):
      print("Male normal test passed")
    femaleesteril=Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.X_MUTATED)
    if(femaleesteril.is_steril() and not femaleesteril.is_poligamic()):
      print("Female only steril test passed")
    femalenormal1=Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X, chromosome2=Chromosome.X)
    femalenormal2=Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X, chromosome2=Chromosome.X_MUTATED)
    femalenormal3=Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.X)
    if(not femalenormal1.is_steril() and not femalenormal1.is_poligamic()):
      print("Female normal test passed")
    if(not femalenormal2.is_steril() and not femalenormal2.is_poligamic()):
      print("Female normal chromosome1mutated test passed")
    if(not femalenormal1.is_steril() and not femalenormal1.is_poligamic()):
      print("Female normal chromosome2mutated test passed")
    

  except ErrorMouse as em:
    print(em)
  '''
  for i in range (0,10):
    print(Mouse().get_weight(), Mouse().get_temperature())
  '''

if __name__ == "__main__":
  main()
