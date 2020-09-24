import sys
sys.path.append('../')
import math
import random
import copy
from datetime import date
from utils import Utils
from exceptions.ErrorPopulation import ErrorPopulation
from animals.EnumsMouse import Gender, Chromosome
from animals import Mouse
from families import Family, NormalFamily, PoligamicFamily

#!/usr/bin/env python

"""Population.py: Population Class for representing a population of animals"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"

class Population: 

  num_reference = 0 
  __choice_poligamic_family=5
  __min_choice_poligamic_family=0
  __max_choice_poligamic_family=9
  def __init__(self, reference=None, name=None, researcher=None, start_date=date.today(), num_days=270, animal_list=None, families_list=None, population_size = 10, male_percentage=0.4, mutated_percentage=0.2, ref_mouse= 1):
    """ Constructor of population
      It creates a Population
      :param reference: Unique identifier of the population. Assigned auto incrementally by default
      :param name: By default a name between experiment1 and experiment6
      :param researcher: By default a name between researcher1 and researcher6
      :param start_date: start date of the population. By default, the day of the creation
      :param num_days: num of the days that the population is active. By default 270
      :param animal_list: list of animals
      :param population_size: size of the virtual_population
      :param male_percentage: Probability of males for virtual populations
      :param mutated_percentage: Probability of mutated animals for virtual populations
      :type reference: int > 0
      :type name: string
      :type researcher: string
      :type start_date: date
      :type num_days: int > 0
      :type animal_list: List of Animals
      :type male_percentage: int > 0
      :type male_percentage: real [0-1]
      :type mutated_percentage: real [0-1]
      :raises ErrorPopulation when any of the arguments do not fulfill the type specified
    """
    if (isinstance(reference,int) and reference > 0):
      self.__reference= reference 
      if(reference > Population.num_reference):
        Population.num_reference = reference
    else:
      Population.num_reference += 1
      self.__reference = Population.num_reference

    if name == None:
      self.__name = Population.__generate_random_name()
    else:
      self.set_name(name)

    if researcher == None:
      self.__researcher = Population.__generate_random_researcher()
    else:
      self.set_researcher(researcher)

    if isinstance(start_date, date):
      if(start_date > date.today()):
        raise ErrorPopulation("start date cannot be a future date")
      else:
        self.__start_date= start_date
    else:
      raise ErrorPopulation("Start date of the experiment should be a date")  

    try:
      self.set_num_days(num_days)
    except Exception as e:
      raise ErrorPopulation(str(e)) 
    if(animal_list == None):
      self.__animal_list = Population.__generate_random_mouses(population_size,male_percentage,mutated_percentage, ref_mouse)
      self.__population_size = len(self.__animal_list)
    elif(isinstance(animal_list,list)):
      for animal in animal_list:
        if(not isinstance(animal,Mouse.Mouse)):
          raise ErrorPopulation("The list of mouses should be a list of objects mouse")
      self.__animal_list = animal_list
      self.__population_size = len(animal_list)
    else:
      raise ErrorPopulation("The list of mouses should be a list of objects mouse")
    if(families_list == None):
      self.__families_list = []
      self.__families_list_size = 0
    elif(isinstance(families_list,list)):
      for family in families_list:
        if(not isinstance(family,Family.Family)):
          raise ErrorPopulation("The list of mouses should be a list of objects mouse")
      self.__families_list = families_list
      self.__families_list_size = len(self.__families_list)
    else:
      raise ErrorPopulation("The list of families should be a list of objects family")


  def get_reference(self):
    return self.__reference


  def get_name(self):
    return self.__name

  def set_name(self, name):
    if name == None:
      pass
    elif isinstance(name,str):
      self.__name = name
    else:
      self.__name = str(name)

  def get_researcher(self):
    return self.__researcher

  def set_researcher(self, researcher):
    if researcher == None:
      pass
    elif isinstance(researcher,str):
      self.__researcher = researcher
    else:
      self.__researcher = str(researcher)

  def get_reference(self):
    return self.__reference

  def set_reference(self, reference):
    if reference == None:
      pass
    elif isinstance(reference,str):
      self.__reference = reference
    else:
      self.__reference = str(reference)

  def get_start_date(self):
    return self.__start_date

  def get_num_days(self):
    return self.__num_days

  def set_num_days(self, num_days):
    if isinstance(num_days,int):
      if(num_days >= 0):
        self.__num_days=num_days
      else:
        raise ValueError("num_days should be positive") 
    else:
      raise TypeError("Weight should be an int")

  def get_animal_list(self):
    return self.__animal_list

  def get_population_size(self):
    return self.__population_size

  def get_families_list(self):
    return self.__families_list
  
  def get_families_list_size(self):
    return self.__families_list_size

  def __str__(self):
    return  ("ref: "+ str(self.__reference) + ", name: " + str(self.__name) + ", researcher: " + str(self.__researcher) + ", start_date: " +str(self.__start_date) + ", num_days: "+ str(self.__num_days))

  def __hash__(self):
    return hash(self.__reference)

  def __eq__(self,other):
    if isinstance(other,self.__class__):
        return self.__reference==other.__reference
    else:
        return False

  def __repr__(self):
    return ("Reference: " + str(self.__reference) +  ", Name: " + str(self.__name))

  def get_references(self):
    """
    :return: the references of the mouses
    :rtype: list of integers 
    """
    mouse_references = []
    for mouse in self.__animal_list:
      mouse_references.append(mouse.get_reference())
    return mouse_references
  
  def add_mouse(self, mouse):
    """
    Add a mouse to the population
    :param mouse: mouse to add to the population
    :type mouse: Mouse
    :raises an errorPopulation if the param is not a mouse
    """
    if(isinstance(mouse,Mouse.Mouse)):
      self.__animal_list.append(mouse)
      self.__population_size = self.__population_size + 1
    else:
      raise ErrorPopulation("The object to append to the list of mouses should be a Mouse")

  def delete_mouse(self, mouse):
    """
    Delete a mouse from the population if it exists
    :param mouse: mouse to delete from the population
    :type mouse: Mouse
    :raises an errorPopulation if the param is not a mouse or a valueError if the mouse is not present in the population
    """
    if(isinstance(mouse,int)):
      mouse = self.get_mouse(mouse)
    if(isinstance(mouse,Mouse.Mouse)):
      try:
        self.__animal_list.remove(mouse)
        self.__population_size = self.__population_size - 1
      except ValueError as ve:
        raise ValueError("The mouse to delete does not exist")
    else:
      raise ErrorPopulation("The object to delete from the list of mouses should be a Mouse")

  def update_mouse(self, mouse, name=None, weight=None, temperature=None, description=None):
    """
    Update the data of a mouse if it exists
    :param mouse: mouse or reference of the mouse to update in the population
    :param name:
    :param weight:
    :param temperature:
    :param description:
    :type mouse: int or mouse
    :type name: str
    :type weight: int,float > 0
    :type temperature: int,float > 0
    :type description: str
    :raises an ErrorMouse if the params types are not correct or a valueError if the mouse or the reference of the mouse is not present
    """
    if(isinstance(mouse,int)):
      mouse = self.get_mouse(mouse)
    if(isinstance(mouse,Mouse.Mouse)):
      if(name != None):
        mouse.set_name(name)
      if(weight != None):
        try:
          mouse.set_weight(weight)
        except e:
          raise MouseError(str(e))
      if(temperature != None):
        try:
          mouse.set_temperature(temperature)
        except e:
          raise MouseError(str(e))
      if(description != None):
        mouse.set_description(description)

  def get_mouse(self, reference):
    """
    get the mouse if it is present in the population
    :param reference: reference of the mouse to return in the population
    :type reference: int
    :raises a valueError if the reference of the mouse is not present
    """
    found=False
    for mouse in self.__animal_list:
      if(reference == mouse.get_reference()):
        return mouse
    raise valueError("The mouse is not in the population")

  @staticmethod
  def __generate_random_name():
    '''
    It returns a name from population1 to population6
    :return: the name of the population randomly generated 
    :rtype: string
    '''
    listPopulations = ["population1", "population2", "population3", "population4", "population5", "population6"]
    return Utils.get_random_str_from_list(listPopulations)

  @staticmethod
  def __generate_random_researcher():
    '''
    It returns a name from researcher1 to researcher6
    :return: the name of the researcher randomly generated 
    :rtype: string
    '''
    listResearchers = ["researcher1", "researcher2", "researcher3", "researcher4", "researcher5", "researcher6"]
    return Utils.get_random_str_from_list(listResearchers)

  @staticmethod
  def __generate_random_mouses(population_size, male_percentage, mutated_percentage, ref_mouse):
    '''
    It returns a list of mouses with the percetange of males especified, the percentage of females = 1 - male_percentages
    If any of the parameters are not specified, it returns an empty list
    :param population_size: size of the population
    :param male_percentage: percentage of males in the population
    :param mutated_percentage: percentage of mutated mouses in the population
    :type population_size: int > 0
    :type male_percentage: float [0-1]
    :type mutated_percentage: float [0-1]
    :return: the list of mouses
    :rtype: list
    :raises an errorPopulation if the population size is < 0 or if the percentages are not in the range [0-1]
    '''
    if((not isinstance(ref_mouse,int)) or ref_mouse < 1):
      ref_mouse = 1 
    if (population_size == None or male_percentage == None or mutated_percentage == None):
      return []
    if(isinstance(male_percentage,(int,float)) and isinstance(mutated_percentage,(int,float)) and (male_percentage < 0 and male_percentage > 1) or (mutated_percentage < 0 and mutated_percentage > 1)):
      raise ErrorPopulation("The percentages of males and mutated should be a number between [0-1]")
    if(isinstance(population_size,int) and population_size > 0):
      num_males = math.floor(population_size*male_percentage)
      num_females = population_size - num_males
      num_males_mutated = math.floor(mutated_percentage*num_males)
      num_males_non_mutated = num_males - num_males_mutated
      num_females_mutated = math.floor(mutated_percentage*num_females)
      num_females_non_mutated = num_females - num_females_mutated
      listMouses = []

      if num_males_non_mutated > 0:
        num_males_non_mutated = num_males_non_mutated - 1                 #para que el for no cree un raton de mas :)
        listMouses.append(Mouse.Mouse(reference=ref_mouse, gender=Gender.MALE, probabilityMutation=0))

      elif num_males_mutated > 0:
        num_males_mutated = num_males_mutated - 1
        listMouses.append(Mouse.Mouse(reference=ref_mouse, gender=Gender.MALE, probabilityMutation=1))

      elif num_females_non_mutated > 0:
        num_females_non_mutated = num_females_non_mutated - 1
        listMouses.append(Mouse.Mouse(reference=ref_mouse, gender=Gender.FEMALE, probabilityMutation=0))

      elif num_females_mutated > 0:
        num_females_mutated = num_females_mutated - 1
        listMouses.append(Mouse.Mouse(reference=ref_mouse, gender=Gender.FEMALE, probabilityMutation=1))
      
      for i in range(0,num_males_non_mutated):
        listMouses.append(Mouse.Mouse(gender=Gender.MALE, probabilityMutation=0))
      for i in range(0,num_males_mutated):
        listMouses.append(Mouse.Mouse(gender=Gender.MALE, probabilityMutation=1))
      for i in range(0,num_females_non_mutated):
        listMouses.append(Mouse.Mouse(gender=Gender.FEMALE, probabilityMutation=0))
      for i in range(0,num_females_mutated):
        listMouses.append(Mouse.Mouse(gender=Gender.FEMALE, probabilityMutation=1))
      
      return listMouses
      
    else:
      raise ErrorPopulation("The population size should be an int > 0")


  def family_creation(self, reference_first_family):                                          #poner reference_first_family como parametro
    '''
    It creates the families based on the mouses present in the population
    :return returns the number of families created
    :rtype int
    '''
    animals = self.get_animal_list()
    population_size = len(animals)
    males = []
    females = []
    for animal in animals:
      if(animal.get_gender()==Gender.MALE):
        males.append(animal)
      elif(animal.get_gender()==Gender.FEMALE):
        females.append(animal)
    
    aux_males = 0;
    aux_females = 0;
    num_families = 0
    while (len(males) > 0 and len(females) > 0):
      male = males.pop(aux_males)
      self.delete_mouse(male)

      if(not male.is_poligamic()):
        # TODO CREATE POLIGAMIC FAMILY
        female = females.pop(aux_females)
        self.delete_mouse(female)
        family = NormalFamily.NormalFamily(parent = male, mother = female, reference = reference_first_family) 
        self.__families_list.append(family)
        num_families = num_families + 1

      else:
        aux_females_family=[]
        more_females=Population.__choice_poligamic_family
        while(more_females >=Population. __choice_poligamic_family and len(females) > 0):
          female = females.pop(aux_females)
          self.delete_mouse(female)
          aux_females_family.append(female)
          more_females = random.randint(Population.__min_choice_poligamic_family,Population.__max_choice_poligamic_family)

        family = PoligamicFamily.PoligamicFamily(parent = male, mothers = aux_females_family, reference = reference_first_family) 
        self.__families_list.append(family)
        num_families = num_families + 1
    self.__families_list_size = self.__families_list_size + num_families
    #print(str(self.__families_list))
    return num_families                  #que devuelva lista con tipo familia, id padre, id madre

  def family_reproduction(self, ref_last_mouse):
    '''
    Reproduces the families of the population
    :return returns the number of new mouses born
    :rtype int
    '''
    num_children = 0
    for family in self.__families_list:
      children = family.reproduce(ref_last_mouse)
      #print(children)
      self.__animal_list.extend(children)
      num_children = num_children + len(children)
    self.__population_size = self.__population_size + num_children
    return num_children


def main():
  male_percentage=0.4
  mutated_percentage=0.2
  
  try:
    population1 = Population(population_size = 40, male_percentage = 0.3, mutated_percentage = 0.2)
    print(population1)
    if(len(population1.get_animal_list()) == 40):
      print("Population size test passed")
    else:
      print("Population size test failed")
    num_males =0
    num_males_sterils = 0
    num_males_poligamics = 0
    num_females = 0
    num_females_sterils = 0
    num_females_poligamics = 0
    for mouse in population1.get_animal_list():
      if(mouse.get_gender() == Gender.MALE):
        if(mouse.is_steril()):
          num_males_sterils+=1
        if(mouse.is_poligamic()):
          num_males_poligamics+=1
        num_males +=1
      elif(mouse.get_gender() == Gender.FEMALE):
        if(mouse.is_steril()):
          num_females_sterils+=1
        if(mouse.is_poligamic()):
          num_females_poligamics+=1
        num_females +=1

    if(num_males == 12):
      print("Male Population size test passed")
    else:
      print("Male Population size test failed")
    if(num_males_sterils + num_males_poligamics == 2):
      print("Male Population mutated size test passed")
    else:
      print("Male Population mutated size test failed")
    if(num_females == 28):
      print("Male Population size test passed")
    else:
      print("Male Population size test failed")
    if(num_females_sterils == 5):
      print("Male Population size test passed")

    print("POP SIZE BEFORE FAMILIES", population1.get_population_size())
    num_families_created = population1.family_creation(reference)
    print("POP SIZE AFTER FAMILIES", population1.get_population_size())
    print("FAMILIES IN POP", population1.get_families_list_size())
    print("FAMILIES CREATED", population1.get_families_list_size())
    
    print("POP SIZE BEFORE REPRODUCTION", population1.get_population_size())
    num_children = population1.family_reproduction()
    print("POP SIZE AFTER REPRODUCTION", population1.get_population_size())
    print("CHILDREN CREATED", num_children)
    '''
    #population1.show_references()

    
    maleesteril=Mouse.Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.Y_MUTATED)
    if(maleesteril.is_steril() and not maleesteril.is_poligamic()):
      print("Male only steril test passed")
    malepoligamic=Mouse.Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X, chromosome2=Chromosome.Y_MUTATED)
    if(not malepoligamic.is_steril() and malepoligamic.is_poligamic()):
      print("Male only poligamic test passed")
    malesterilpoligamic=Mouse.Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.Y_MUTATED)
    if(malesterilpoligamic.is_steril() and malesterilpoligamic.is_poligamic()):
      print("Male steril and poligamic test passed")
    malenormal=Mouse.Mouse(name=None, gender=Gender.MALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.Y_MUTATED)
    if(not malenormal.is_steril() and not malenormal.is_poligamic()):
      print("Male normal test passed")
    femaleesteril=Mouse.Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.X_MUTATED)
    if(femaleesteril.is_steril() and not femaleesteril.is_poligamic()):
      print("Female only steril test passed")
    femalenormal1=Mouse.Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X, chromosome2=Chromosome.X)
    femalenormal2=Mouse.Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X, chromosome2=Chromosome.X_MUTATED)
    femalenormal3=Mouse.Mouse(name=None, gender=Gender.FEMALE, description="asd", chromosome1=Chromosome.X_MUTATED, chromosome2=Chromosome.X)
    if(not femalenormal1.is_steril() and not femalenormal1.is_poligamic()):
      print("Female normal test passed")
    if(not femalenormal2.is_steril() and not femalenormal2.is_poligamic()):
      print("Female normal chromosome1mutated test passed")
    if(not femalenormal1.is_steril() and not femalenormal1.is_poligamic()):
      print("Female normal chromosome2mutated test passed")
  '''
  except ErrorPopulation as ep:
    print(ep)
  #TEST BIRTHDATE
  #if(mouse1.)


if __name__ == "__main__":
  main()
