import random
import csv
import sys
sys.path.append('../')
from datetime import datetime
from utils import Utils
from populations import Population
from animals import Mouse, EnumsMouse
"""InputOutput.py: Utilities containing a set of input/output functions related to the application of mouses"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"

def read_int(question="introduce an integer"):
  """
  read an int
  :param question: question to ask for the integer
  :type question: str
  :return: the integer read
  :rtype: int
  """
  while(True):
    try:
      input1 = input(question + ": \n")
      int1 = int(input1)
      return int1
    except ValueError:
      print("the value should be an integer")
    except Exception:
      print("there was an error reading the input. Please introduce an integer")

def read_positive_int(question="introduce an integer"):
  """
  read an int > 0 from keyboard
  :param question: question to ask for the integer > 0
  :type question: str
  :return: the integer read
  :rtype: int
  """
  while(True):
    try:
      input1 = input(question + ": \n")
      int1 = int(input1)
      if(int1 > 0):
        return int1
      else:
        print("the value should be an integer > 0")
    except ValueError:
      print("the value should be an integer")
    except Exception:
      print("there was an error reading the input. Please introduce an integer")

def read_float(question="introduce a float"):
  """
  read a float
  :param question: question to ask for the float
  :type question: str
  :return: the integer float
  :rtype: float
  """
  while(True):
    try:
      input1 = input(question + ": \n")
      float1 = float(input1)
      return float1
    except ValueError:
      print("the value should be a number")
    except Exception:
      print("there was an error reading the input. Please introduce a number")

def read_float_range(question="introduce a float", start=0, end=1):
  """
  read a float within the range established between start and end
  :param question: question to ask for the integer
  :type question: str
  :param start: start of the range
  :type start: int,float
  :param end: end of the range
  :type end: int, float
  :return: the integer float
  :rtype: float
  :raises a TypeError if start or end are not int or float (numbers)
  """
  if not (isinstance(start,(int,float)) and isinstance(end,(int,float))):
    raise TypeError("start and end should be numbers")
  while(True):
    try:
      input1 = input(question + ": \n")
      float1 = float(input1)
      if(float1 >= start and float1 <= end):
        return float1
      else:
        print("the value should be a float between " + str(start) + " and " + str(end))
    except ValueError:
      print("the value should be a number")
    except Exception:
      print("there was an error reading the input. Please introduce a number")

def read_int_range(question="introduce a float", start=0, end=1):
  """
  read a int within the range established between start and end
  :param question: question to ask for the integer
  :type question: str
  :param start: start of the range
  :type start: int,float
  :param end: end of the range
  :type end: int, float
  :return: the integer int
  :rtype: int
  :raises a TypeError if start or end are not int or float (numbers)
  """
  if not (isinstance(start,(int,float)) and isinstance(end,(int,float))):
    raise TypeError("start and end should be numbers")
  while(True):
    try:
      input1 = input(question + ": \n")
      int1 = int(input1)
      if(int1 >= start and int1 <= end):
        return int1
      else:
        print("the value should be an integer between " + str(start) + " and " + str(end))
    except ValueError:
      print("the value should be a number")
    except Exception:
      print("there was an error reading the input. Please introduce a number")

def read_positive_float(question="introduce an integer"):
  """
  read an float > 0 from keyboard
  :param question: question to ask to read a float
  :type question: str
  :return: the float read
  :rtype: float
  """
  while(True):
    try:
      input1 = input(question + ": \n")
      float1 = float(input1)
      if(float1 > 0):
        return float1
      else:
        print("the value should be a number > 0")
    except ValueError:
      print("the value should be a number")
    except Exception:
      print("there was an error reading the input. Please introduce a number")

def read_date():
  """
  read a date
  :return: the date
  :rtype: date
  """
  while(True):
    try:
      year = read_int_range("Year",1900,2020)
      month = read_int_range("Month",1,12)
      day = read_int_range("Day",1,31)
      date_string = str(year) + "-" + str(month) + "-" + str(day)
      readDate = datetime.strptime(date_string,'%Y-%m-%d').date()
      return readDate
    except ValueError as ve:
      print(str(ve))
    except Exception:
      print("there was an error reading the input. Please introduce a number")



def read_int_in_list(question="introduce an integer within the list", list_to_search=[]):
  """
  read an element from the list
  :param question: question to ask
  :type question: str
  :param list_to_search: list of ints
  :type list_to_search: list of ints
  :return: the integer read
  :rtype: int
  """
  if(not isinstance(list_to_search,list)):
    raise typeError("list_to_search should be a list")
  while(True):
    try:
      input1 = input(question + ": \n")
      int1 = int(input1)
      if(int1 in list_to_search):
        return int1
      else:
        print("the value should be in the list")
        print(str(list_to_search))
    except ValueError:
      print("the value should be an integer")
    except Exception:
      print("there was an error reading the input. Please introduce an integer")

def read_gender_from_keyboard():
  """
  read the gender from keyboard
  :return: the gender mouse
  :rtype: Mouse
  """
  while(True):
    gender = input("Gender (male,female): \n")
    try:
      gender = EnumsMouse.Gender.from_str(gender)
      return gender
    except NotImplementedError as nie: 
      print("Gender should be male or female")

def read_chromosomes_from_keyboard(gender):
  """
  read the chromosomes from keyboard according to the gender
  :param gender: gender of the mouse
  :type gender: Gender
  :return: a list with two chromosomes
  :rtype: list with two chromosomes
  :raises typeError if gender is not Gender
  """
  if(not isinstance(gender,EnumsMouse.Gender)):
    raise typeError("Gender should be a gender type")
  while(True):
    chromosome1 = input("Chromosome 1 (X,X_MUTATED): \n")
    try:
      chromosome1 = EnumsMouse.Chromosome.from_str(chromosome1)

    except NotImplementedError: 
      print("The chromosome should be X or X_MUTATED")
      continue
    if(gender == EnumsMouse.Gender.MALE):
      chromosome2 = input("Chromosome 2 (Y,Y_MUTATED): \n")
      try:
        chromosome2 = EnumsMouse.Chromosome.from_str_Y(chromosome2)
        return([chromosome1,chromosome2])
      except NotImplementedError: 
        print("The chromosome should be Y or Y_MUTATED")
    else:
      try:
        chromosome2 = input("Chromosome 2 (X,X_MUTATED): \n")
        chromosome2 = EnumsMouse.Chromosome.from_str_X(chromosome2)
        return([chromosome1,chromosome2])
      except NotImplementedError: 
        print("The chromosome should be X or X_MUTATED")
  

def read_mouse_from_keyboard(numReference):    #???????????????????????????????
  """
  read a mouse from keyboard
  :return: the read mouse
  :rtype: Mouse
  """
  print("Introduce the data of the mouse\n")
  name = input("Name: \n")
  birthdate = read_date()
  weight = read_positive_float("Weight")
  
  gender = read_gender_from_keyboard()
  temperature = read_positive_float("Temperature")
  description = input("Description of the mouse: \n")
  chromosomes = read_chromosomes_from_keyboard(gender)
  chromosome1 = chromosomes[0]
  chromosome2 = chromosomes[1]

  mouse = Mouse.Mouse(reference=numReference, name=name, birthdate=birthdate, weight=weight, gender=gender, temperature=temperature, description=description,  chromosome1=chromosome1, chromosome2=chromosome2)
  return mouse

def read_name_weight_temperature_description_from_keyboard():
  """
  read a mouse from keyboard
  :return: the read mouse
  :rtype: Mouse
  """
  print("Introduce the data to update the mouse\n")
  name = input("Name: \n")
  weight = read_positive_float("Weight")
  
  temperature = read_positive_float("Temperature")
  description = input("Description of the mouse: \n")
  return name, weight, temperature, description
  

def print_list(list1, label="element", header="list"):
  """
  Print the elements of a list
  :param list1: list to print
  :param label: label for the list
  :param header: header for the list
  :type list1: list
  :type label: str
  :type header: str
  """
  if(len(list1) > 0):
    print("The " + header + " " + label + " are: ")
    for element in list1:
      print(label + ": " +  str(element))
  else:
    print("The " + header + " does not contain any mouse")

def read_population_from_csv(file_name):
  """
  read a csv file with the headers called name,researcher,start_date,num_days,populations and the information about them in the first line
  :param file_name
  :type file_name: str
  :return: the population read from the csv
  :rtype: population
  :raises a ValueError if the csv file does not has the structure list of length 2 containing a list with the headers reference, name, researcher, start_date, num_days, populations in the position 0 and the values in the position 1
  :raises a TypeError if the file_name does not end in csv
  :raises IOError if there is some error reading the file
  """
  if not file_name.endswith(".csv"):
    raise TypeError("file should be a csv")
  
  try:
    with open("csvfiles/" + file_name) as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      populationList=[]
      for row in reader:
        values = []
        for column in row:
          values.append(column)
        populationList.append(values)
      population = Utils.getPopulationFromList(populationList)
      return population
  except IOError as ioe:
    raise ioe

def read_mouses_from_csv(file_name):
  """
  read a csv file with the headers called name,researcher,start_date,num_days,populations and the information about them in the first line
  :param file_name
  :type file_name: str
  :return: the mouses read from the csv
  :rtype: list of Mouse
  :raises a ValueError if the csv file does not has the structure list of length 2 containing a list with the headers reference, name, researcher, start_date, num_days, populations in the position 0 and the values in the position 1
  :raises a TypeError if the file_name does not end in csv
  :raises IOError if there is some error reading the file
  """
  import os
  if not file_name.endswith(".csv"):
    raise TypeError("file should be a csv")
  try:
    with open("csvfiles/" + file_name) as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      mouses_values_list=[]
      for row in reader:
        values = []
        for column in row:
          values.append(column)
        mouses_values_list.append(values)
      mouses_list = Utils.getMousesFromList(mouses_values_list)
      return mouses_list
  except IOError as ioe:
    raise ioe


def write_population_to_csv(population,file_name):
  """
  writes a csv file with the headers called name,researcher,start_date,num_days,populations and the information about the population
  :param population: Population to write in the csv
  :type population: Population
  :param file_name
  :type file_name: str
  :raises a TypeError if the population is not a Population
  :raises a ValueError 
  :raises OSError, IOError if there is some error opening or writing the file
  """

  if not isinstance(population,Population.Population):
    raise TypeError("Population should be a Population")

  if not file_name.endswith(".csv"):
    file_name = str(file_name) + ".csv"
  reference_header = "reference"

  name_header = "name"
  researcher_header = "researcher"
  start_date_header = "start_date"
  num_days_header = "num_days"
  mouses_csv_file_name_header = "populations"

  population_headers = reference_header + "," + name_header + "," + researcher_header + "," + start_date_header + "," + num_days_header + "," + mouses_csv_file_name_header

  reference = population.get_reference()
  name = population.get_name()
  researcher = population.get_researcher()
  start_date = population.get_start_date()
  num_days = population.get_num_days()
  mouses_csv_file_name = file_name[:-4] + "_mouses.csv"
  population_values = str(reference) + "," + name + "," + researcher + "," + str(start_date) + "," + str(num_days) + "," + mouses_csv_file_name
  population_file = open("csvfiles/" + file_name, "w")
  population_file.write(population_headers)
  population_file.write("\n")
  population_file.write(population_values)
  __write_mouses_to_csv(population,mouses_csv_file_name)


def __write_mouses_to_csv(population,file_name):
  """
  writes a csv file with the headers called name,researcher,start_date,num_days,populations and the information about the mouses 
  :param population: Population containing the mouses to write in the csv
  :type population: Population
  :param file_name
  :type file_name: str
  :raises a TypeError if the population is not a Population
  :raises a ValueError 
  :raises OSError, IOError if there is some error opening or writing the file
  """

  if not isinstance(population,Population.Population):
    raise TypeError("Population should be a Population")

  if not file_name.endswith(".csv"):
    file_name = str(file_name) + ".csv"
  reference_header = "reference"
  name_header = "name"
  birthdate_header = "birthdate"
  weight_header = "weight"
  gender_header = "gender"
  temperature_header = "temperature"
  description_header = "description"
  chromosome1_header = "chromosome1"
  chromosome2_header = "chromosome2"

  mouses_headers = reference_header + "," + name_header + "," + birthdate_header + "," + weight_header + "," + gender_header + "," + temperature_header + "," + description_header + "," + chromosome1_header + "," + chromosome2_header
  mouses_file = open("csvfiles/" + file_name, "w")
  mouses_file.write(mouses_headers)
  mouses_file.write("\n")
  mouses = population.get_animal_list()
  for mouse in mouses:
    reference = mouse.get_reference()
    name = mouse.get_name()
    birthdate = mouse.get_birthdate()
    weight = mouse.get_weight()
    gender = mouse.get_gender()
    temperature = mouse.get_temperature()
    description = mouse.get_description()
    chromosome1 = mouse.get_chromosome1()
    chromosome2 = mouse.get_chromosome2()
    mouse_values = str(reference) + "," + name + "," + str(birthdate) + "," + str(weight) + "," + str(gender) + "," + str(temperature) + "," + description + "," + str(chromosome1) + "," + str(chromosome2) 
    mouses_file.write(mouse_values)
    mouses_file.write("\n")

def main():
  list1=[1,2,3,4,5]
  print_list(list1)
  print_list(list1, label="Mouse", header="mouses")
  name, weight, temperature, description = read_name_weight_temperature_description_from_keyboard()
  print(name, weight, temperature, description)
  mouse = read_mouse_from_keyboard()
  print(mouse)

if __name__ == "__main__":
  main()