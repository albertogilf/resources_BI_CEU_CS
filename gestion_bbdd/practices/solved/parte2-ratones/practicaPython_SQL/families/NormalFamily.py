import sys
sys.path.append('../')
import random
from animals import Mouse, EnumsMouse
from families.Family import Family
#!/usr/bin/env python

"""NormalFamily.py: Family Class for representing the families of mouses with no mutations"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"

class NormalFamily(Family): 

  def __init__(self, parent, mother, reference=None, children=None):
    '''
    Constructor of a Normal Family with a parent, a mother and 0 or more children
    :param parent: parent of the family
    :param reference: reference of the family
    :param parent: parent of the family
    :param reference: reference of the family
    :type parent: Mouse
    :type reference: int
    :raises ErrorFamily if parent, mother or the list of children are not mouses
    '''
    super().__init__(parent, reference, children) 

    if isinstance(mother,Mouse.Mouse):
      self.__mother = mother
    else: 
      raise ErrorFamily.ErrorFamily("Parent should be a Mouse instance")

  def get_mother(self):
    return self.__mother

  def reproduce(self, ref_last_mouse):
    '''
    reproduces the normal family between the parent and the mother and saves 
    the list of the new children in the family
    :return the list of new born children
    :rtype list
    '''
    if((not isinstance(ref_last_mouse,int)) or ref_last_mouse < 1):
      ref_last_mouse = 1 
    children = []
    # Mother steril
    if(self.__mother.is_steril()):
      return children
    # Father esteril
    elif(self.get_parent().is_steril()):
      probability_list = Family._dict_probabilities_father_steril.items()
    #Both normal
    else:
      probability_list = Family._dict_probabilities_normal.items()
    # Reproduce according to the probabilities
    choice = random.randint(Family._min_choice_num_children, Family._max_choice_num_children)
    for prob,num_children in probability_list:
      if choice < prob:
        for i in range(0,num_children):
          mouse = Mouse.Mouse(ref_last_mouse)
          children.append(mouse)
          self.add_children(mouse)
        break
    return children
  
    

  def __str__(self):
    return  ("Normal " + super().__str__() + ", mother: " + str(self.__mother) + ", children: " + str(super().get_children()))

  def __repr__(self):
    return ("Normal " + super().__repr__() + ", mother: " + str(self.__mother) + ", num_children: " + str(self._children_size))


def main():
  try:
    mouse1 = Mouse.Mouse(name=None, gender=EnumsMouse.Gender.MALE, description="asd", chromosome1=EnumsMouse.Chromosome.X, chromosome2=EnumsMouse.Chromosome.Y)
    mouse2 = Mouse.Mouse(name=None, gender=EnumsMouse.Gender.MALE, description="asd", chromosome1=EnumsMouse.Chromosome.X, chromosome2=EnumsMouse.Chromosome.X)
    normalFamily = NormalFamily(mouse1, mouse2)
    print(normalFamily)
  except Exception as ef:
    print(str(ef))

if __name__ == '__main__':
  main()
