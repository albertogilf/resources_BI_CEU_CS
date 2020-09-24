import sys
sys.path.append('../')
import random
from animals.Mouse import Mouse
from utils import inputOutput
from populations.Population import Population
from exceptions.ErrorPopulation import ErrorPopulation

"""lab.py: main application processing the mouse populations of the laboratory """

__author__    = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"



def main():
  current_population = None
  file_name = None
  work_saved = True
  print("Welcome to the lab population mouses application")
  while True:
    print("")
    print("1. Open file")
    print("2. Create a new virtual population")
    print("3. Create a new empty population")
    print("4. List all mouses from the current population")
    print("5. Add a new mouse to the current population manually")
    print("6. Add a new random mouse to the current population indicating only the name")
    print("7. Delete a mouse from the current population")
    print("8. Update data from a mouse in the current population")
    print("9. Show details of a mouse from the current population")
    print("10. Create new families from the current population")
    print("11. Reproduce the families from the current population")
    print("12. Save")
    print("13. Save as")
    print("14. Exit")
    print("")
    try:
      option=int(input("Choose an action: \n")) 

      if option==1:
        file_name = input("Write the file name with the extension(including absolute path if necessary)" + ": \n")
        try:
          current_population = inputOutput.read_population_from_csv(file_name)
          print("Population open: " + str(current_population))
        except TypeError as e:
          print(str(e))
          print("The file " + file_name +  " is not a csv")
        except IOError as ioe:
          print("Error reading the file: " + file_name)
          print("check if the files " + file_name + " and " + file_name[:-4] + "_mouses.csv" + " exist")
        except ValueError as ve:
          print(ve)

      if option==2:
        population_size = inputOutput.read_positive_int("Size of the population")
        male_percentage = inputOutput.read_float_range("Introduce the percentage of male mouses between 0 and 1", 0, 1)
        mutated_percentage = inputOutput.read_float_range("Introduce the percentage of mutated mouses between 0 and 1", 0, 1)
        current_population = Population(population_size = population_size, male_percentage = male_percentage, mutated_percentage = mutated_percentage)
        print(current_population)
        work_saved = False

      if option==3:
        current_population = Population(animal_list=[])
        print(current_population)
        work_saved = False
          
      if option==4:
        isPopulationOpen(current_population)
        references = current_population.get_references()
        inputOutput.print_list(references,"mouse","population")

      if option==5:
        isPopulationOpen(current_population)

        mouse = inputOutput.read_mouse_from_keyboard()
        current_population.add_mouse(mouse)
        
        work_saved = False

      if option==6:
        isPopulationOpen(current_population)
        print("Introduce the name of the mouse\n")
        name = input("Name: \n")
        mutation_probability=inputOutput.read_float_range(question="Introduce the mutation probability (a number between 0 and 1)", start=0, end=1)
        mouse = Mouse(name = name, probabilityMutation = mutation_probability)
        current_population.add_mouse(mouse)
        work_saved = False

      if option==7:
        isPopulationOpen(current_population)
        references = current_population.get_references()
        inputOutput.print_list(references,"mouse","population")
        mouse_selected = inputOutput.read_int_in_list("Introduce the reference of the list of mouses",references)
        try:
            current_population.delete_mouse(mouse_selected)
            print("The mouse with reference " + str(mouse_selected) + " was deleted")
            work_saved = False
        except Exception as e:
            print(str(e))
            print("The mouse was not deleted")

      if option==8:
        isPopulationOpen(current_population)
        references = current_population.get_references()
        inputOutput.print_list(references,"mouse","population")
        mouse_selected = inputOutput.read_int_in_list("Introduce the reference of the list of mouses",references)
        try:
            name, weight, temperature, description = inputOutput.read_name_weight_temperature_description_from_keyboard()
            current_population.update_mouse(mouse_selected, name, weight, temperature, description)
            print("The mouse with reference " + str(mouse_selected) + " was updated")
            work_saved = False
        except Exception as e:
            print(str(e))
            print("The mouse was not updated")
      
      if option==9:
        isPopulationOpen(current_population)
        references = current_population.get_references()
        inputOutput.print_list(references,"mouse","population")
        mouse_selected = inputOutput.read_int_in_list("Introduce the reference of the list of mouses",references)
        try:
            mouse = current_population.get_mouse(mouse_selected)
            print("Information of the mouse " + str(mouse_selected))
            print(str(mouse))
            work_saved = False
        except Exception as e:
            print(str(e))
            print("The mouse was not updated")

      if option == 10:
        isPopulationOpen(current_population)
        num_families = current_population.family_creation()
        print("Created ", num_families, " families")
        work_saved = False

      if option == 11:
        # TODO
        isPopulationOpen(current_population)
        num_children = current_population.family_reproduction()
        print("New ", num_children, " were born")
        work_saved = False
      
      if option == 12:
        isPopulationOpen(current_population)
        if(file_name == None):
          len_file_name = 0
        while(len_file_name<2):
          file_name = input("Introduce the file name (ends in .csv): \n")
          len_file_name = len(file_name)
        tmp_work_saved = save_experiment(current_population, file_name)
        if(tmp_work_saved):
          work_saved = True

      if option == 13:
        isPopulationOpen(current_population)
        file_name = input("Introduce the file name (ends in .csv): \n")
        tmp_work_saved = save_experiment(current_population, file_name)
        if(tmp_work_saved):
          work_saved = True

      if option == 14:
        if(not work_saved):
          try:
            save_work = inputOutput.read_int_range("Do you want to save your changes? \n 1. Yes \n 2. No", 1, 2)
            if(save_work == 1):
              save_as=inputOutput.read_int_range(" 1. Save \n 2. Save as", 1, 2)
              if(save_as == 1):
                tmp_work_saved = save_experiment(current_population, file_name)
              elif(save_as == 2):
                file_name = input("Introduce the file name (ends in .csv): \n")
                tmp_work_saved = save_experiment(current_population, file_name)
              print("Work saved in: " + file_name)
            elif(save_work==2):
              pass
            else:
              print("Option not recognized, your work has not been saved")
              print("ELSE")
          except Exception as e:
            print("Option not recognized, your work has not been saved")
            print("EXCEPTION" + str(e))
        print("Thank you. See you soon")
        sys.exit()

    except ErrorPopulation:
      print("The population is not open")
    except ValueError:
      print("You should choose an action between 1 and 14")


def save_experiment(current_population, file_name):
  '''
  saves the population into the filename
  :param current_population
  :type current_population: Population
  :param file_name: file name to save. If None, it asks for the file_name
  :type file_name: str or None
  :return: true if the work is saved. False otherwise
  :rtype: boolean
  :raises PopulationError if current_population is None or is not a Population istance
  '''
  try:
    inputOutput.write_population_to_csv(current_population,file_name)
    return True
  except IOError as ioe:
    print("Error writing the file. Try it again")
  except PermissionError as pe:
    print("Error writing the file due to the permissions. check if the file is open and if the user has permission to write on it")
  return False

def isFilePathOpen(file_name):
  '''
  Raise an ErrorPopulation if the population is not a population
  '''
  if (file_name == None or not isinstance(file_name,str)):
    raise ErrorFileNotOpen("The experiment was not saved before")

def isPopulationOpen(current_population):
  '''
  Raise an ErrorPopulation if the population is not a population
  '''
  if (current_population == None or not isinstance(current_population,Population)):
    raise ErrorPopulation("The population is not open")

if __name__ == "__main__":
  main()
   