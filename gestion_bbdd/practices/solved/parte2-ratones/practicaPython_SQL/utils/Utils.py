import sys
sys.path.append('../')
import random
from datetime import datetime
from populations import Population
from utils import inputOutput
from animals import EnumsMouse, Mouse
"""Utils.py: Utilities containing a set of common functions"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"


def get_random_str_from_list(list1):
  """
  :param list1: list of objects to pick a random one
  :type list1: list
  :return: a random object from the list passed as a parameter
  :rtype: element of a list
  """
  if isinstance(list1,list):
    random_num = random.randint(0,len(list1)-1)
    return list1[random_num]


def checkPercentage1(perc1, perc2, perc3):
  """
  :param perc1: first number for percentages
  :param perc2: second number for percentages
  :param perc3: third number for percentages
  :type perc1: int or float
  :type perc3: int or float
  :type perc3: int or float
  :return: true if the addition of the three percentages is 1 +- 0.01 False otherwise
  :rtype: boolean
  """
  if isinstance(perc1,(int,float)) and isinstance(perc2,(int,float)) and isinstance(perc3,(int,float)):
    add = perc1 + perc2 + perc3
    if(add < 1.01 and add > 0.99):
      return True 
  return False


def checkPopulationFromList(list_population):
  """
  :param list_population: list of length 2 containing a list with the headers reference, name, researcher, start_date, num_days, populations in the position 0 and the values in the position 1
  :type list_population: list 
  :raises a valueError if the structure does not contain a list of headers or it contains different values
  :raises a typeErrpr if list_population is not a list
  """
  if(not isinstance(list_population,list)):
    raise TypeError("list_population should be a list")
  if len(list_population)!=2:
    raise ValueError("Length of the list should be 2")
  headers=list_population[0]
  if(headers[0] != 'reference'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[1] != 'name'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[2] != 'researcher'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[3] != 'start_date'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[4] != 'num_days'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[5] != 'populations'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  
  values=list_population[1]
  reference = values[0]
  reference = int(reference)
  if (reference <= 0):
    raise ValueError("Reference of the population should be > 0")
  name = str(values[1])
  researcher = str(values[2])
  start_date = datetime.strptime(values[3],'%Y-%m-%d').date()
  num_days = values[4]
  num_days = int(num_days)
  if (num_days <= 0):
    raise ValueError("Num days of the experiment should be > 0")
  mouses_csv_file_name = str(values[5])

def getPopulationFromList(list_population):
  """
  :param list_population: list of length 2 containing a list with the headers reference, name, researcher, start_date, num_days, populations in the position 0 and the values in the position 1
  :type list_population: list 
  :return: a population with the parameters read in the list_population
  :rtype: Population
  :raises a valueError if the structure does not contain a list of headers or it contains different values
  :raises a typeErrpr if list_population is not a list
  """
  checkPopulationFromList(list_population)
  values=list_population[1]
  reference = values[0]
  reference = int(reference)
  name = str(values[1])
  researcher = str(values[2])
  start_date = datetime.strptime(values[3],'%Y-%m-%d').date()
  num_days = values[4]
  num_days = int(num_days)
  mouses_csv_file_name = str(values[5])
  animal_list = inputOutput.read_mouses_from_csv(mouses_csv_file_name)
  population = Population.Population(reference, name, researcher, start_date, num_days, animal_list)
  return population

    

def getMousesFromList(mouses_values_list):
  """
  :param list_population: list of length 2 containing a list with the headers reference, name, researcher, start_date, num_days, populations in the position 0 and the values in the position 1
  :type list_population: list 
  :return: a population with the parameters read in the list_population
  :rtype: Population
  :raises a valueError if the structure does not contain a list of headers or it contains different values
  :raises a typeError if list_population is not a list
  """
  mouses_list = []

  if(not isinstance(mouses_values_list,list)):
    raise TypeError("list_population should be a list")
  if len(mouses_values_list)<2:
    raise ValueError("Length of the list should be > 2")
  headers=mouses_values_list[0]
  if(headers[0].lower() != 'reference'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[1].lower() != 'name'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[2].lower() != 'birthdate'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[3].lower() != 'weight'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[4].lower() != 'gender'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[5].lower() != 'temperature'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[6].lower() != 'description'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[7].lower() != 'chromosome1'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  if(headers[8].lower() != 'chromosome2'):
    raise ValueError("Headers should be 'reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'")
  

  for i in range(1,len(mouses_values_list)):
    values_mouse=mouses_values_list[i]
    reference = values_mouse[0]
    reference = int(reference)
    if (reference <= 0):
      raise ValueError("The references of the mouses should be > 0")
    name = str(values_mouse[1])
    birthdate = datetime.strptime(str(values_mouse[2]),'%Y-%m-%d').date()
    
    weight = values_mouse[3]
    weight = float(weight)
    if (weight <= 0):
      raise ValueError("The weight of the mouses should be > 0")
    
    try:
      gender = EnumsMouse.Gender.from_str(str(values_mouse[4]))
    except NotImplementedError as nie: 
      print(str(nie))
      raise ValueError("The gender should be Male or female")
    temperature = values_mouse[5]
    temperature = float(temperature)
    if (temperature <= 0):
      raise ValueError("The temperature of the mouses should be > 0")
    description = values_mouse[6]
    try:
      chromosome1 = EnumsMouse.Chromosome.from_str(values_mouse[7])
    except NotImplementedError: 
      raise ValueError("The chromosome should be X, Y, X_MUTATED or Y_MUTATED")
    try:
      chromosome2 = EnumsMouse.Chromosome.from_str(values_mouse[8])
    except NotImplementedError: 
      raise ValueError("The chromosome should be X, Y, X_MUTATED or Y_MUTATED")
    mouse = Mouse.Mouse(reference = reference, name=name, birthdate=birthdate, weight=weight, gender=gender, temperature=temperature, description=description,   chromosome1=chromosome1, chromosome2=chromosome2)
    mouses_list.append(mouse)
  return mouses_list



def main():
  falsePercentage = checkPercentage1(0.2,0.4,0.2)
  if(not falsePercentage):
    print("Test wrong percentage add 1 passed")
  else: 
    print("Test wrong percentage add 1 wrong")
  truePercentage = checkPercentage1(0.4,0.4,0.2)
  if(truePercentage):
    print("Test right percentage add 1 passed")
  else: 
    print("Test right percentage add 1 wrong")
  list_population=[['reference', 'name', 'researcher', 'start_date', 'num_days', 'populations'], ['1', 'population1', 'researcher1', '2019-11-11', '270', 'test_population1_mouses.csv']]
  try:
    checkPopulationFromList(list_population)
    print("Test right list_population passed")
  except Exception as e:
    print("Test right list_population wrong")
  try:
    population=getPopulationFromList(list_population)
    print("Test get population from list_population passed")
  except Exception as e:
    print("Test get population from list_population wrong")
    print(e)

  list_population=[['references', 'name', 'researcher', 'start_date', 'num_days', 'populations'], ['1', 'population1', 'researcher1', '2019-11-11', '270', 'test_population1_mouses.csv']]
  try:
    checkPopulationFromList(list_population)
    print("Test wrong list_population failed")
  except Exception as e:
    print("Test wrong list_population passed")

if __name__ == "__main__":
  main()