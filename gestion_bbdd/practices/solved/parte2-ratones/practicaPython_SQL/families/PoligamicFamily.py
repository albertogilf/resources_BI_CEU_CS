import sys
sys.path.append('../')
import random
from animals import Mouse, EnumsMouse
from families.Family import Family
#!/usr/bin/env python

"""FemaleSterilFamily.py: Family Class for representing the families of poligamic mouses"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"

class PoligamicFamily(Family): 

  def __init__(self, parent, mothers, reference=None, children=None):
    '''
    Constructor of a poligamic Family with a parent, 1 or N mothers and 0 or more children
    :param parent: parent of the family
    :param reference: reference of the family
    :param parent: parent of the family
    :param reference: reference of the family
    :type parent: Mouse
    :type reference: int
    :raises ErrorFamily if parent, list of mothers or the list of children are not mouses
    '''
    super().__init__(parent, reference, children) 
    if isinstance(mothers,Mouse.Mouse):
      self.__mothers = []
      self.__mothers.append(mothers)
      self.__mothers_size = len(self.__mothers)
    elif isinstance(mothers,list) and len(mothers) >= 1:
      for animal in mothers:
        if ((not isinstance(animal, Mouse.Mouse)) or (not animal.get_gender() == EnumsMouse.Gender.FEMALE)):
          raise ErrorFamily.ErrorFamily("The list of mothers should be a list of female mouses")
      self.__mothers = mothers
      self.__mothers_size = len(self.__mothers)
    else: 
      raise ErrorFamily.ErrorFamily("The list of mothers should be a list of female mouses")
    

  def get_mothers(self):
    return self.__mothers

  def get_mothers_size(self):
    return self.__mothers_size

  def reproduce(self, ref_last_mouse):
    '''
    reproduces the poligamic family between the parent and the mothers and saves 
    the list of the new children in the family
    :return the list of new born children
    :rtype list
    '''
    if((not isinstance(ref_last_mouse,int)) or ref_last_mouse < 1):
      ref_last_mouse = 1 
    children = []
    mothers = self.__mothers
    #Father steril
    if self.get_parent().is_steril():
      dict_probabilities = Family._dict_probabilities_father_steril.items()
    # Mother steril
    elif len(mothers) == 1:
      dict_probabilities = Family._dict_probabilities_normal.items()
    else:
      dict_probabilities = Family._dict_probabilities_poligamic.items()
    for mother in mothers:
      if(mother.is_steril()):
        continue
      # Reproduce according to the probabilities
      choice = random.randint(Family._min_choice_num_children, Family._max_choice_num_children)
      for prob,num_children in dict_probabilities:
        if choice < prob:
          for i in range(0,num_children):
            mouse = Mouse.Mouse(ref_last_mouse)
            children.append(mouse)
            self.add_children(mouse)
          break

    return children

  def __str__(self):
    return  ("Polygamic " + super().__str__() + ", mothers: " + str(self.__mothers) + ", children: " + str(super().get_children()) )

  def __repr__(self):
    return ("Polygamic " + super().__repr__() + ", num_mothers: " + str(self.__mothers_size) + ", num_children: " + str(self._children_size))

def main():
  try:
    mouse1 = Mouse.Mouse(name=None, gender=EnumsMouse.Gender.MALE, description="asd", chromosome1=EnumsMouse.Chromosome.X, chromosome2=EnumsMouse.Chromosome.Y)
    mouse2 = Mouse.Mouse(name=None, gender=EnumsMouse.Gender.FEMALE, description="asd", chromosome1=EnumsMouse.Chromosome.X, chromosome2=EnumsMouse.Chromosome.X)
    mouse3 = Mouse.Mouse(name=None, gender=EnumsMouse.Gender.FEMALE, description="asd", chromosome1=EnumsMouse.Chromosome.X, chromosome2=EnumsMouse.Chromosome.X)
    poligamicFamily = PoligamicFamily(mouse1, [mouse2,mouse3])
    print(poligamicFamily)
    poligamicFamily.reproduce()
  except Exception as ef:
    print(str(ef))

if __name__ == '__main__':
  main()