import sys
sys.path.append('../')

from animals import Mouse, EnumsMouse
from abc import ABCMeta, abstractmethod
from exceptions import ErrorFamily
#!/usr/bin/env python

"""Family.py: Abstract Family Class for representing the families of mouses"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"

class Family(object, metaclass = ABCMeta): 
  
  family_reference = 0 
  _min_choice_num_children=0
  _max_choice_num_children=99
  _dict_probabilities_normal = {5:2,15:3,30:4,50:5,70:6,85:7,95:8,99:9}
  _dict_probabilities_poligamic = {10:2,25:3,45:4,60:5,75:6,95:7,99:8}
  _dict_probabilities_father_steril = {15:2,35:3,70:4,90:5,99:6}
  @abstractmethod
  def __init__(self, parent, reference=None, children=None):
    '''
    Constructor of Family with a parent to be instantiated
    :param parent: parent of the family
    :param reference: reference of the family
    :type parent: Mouse
    :type reference: int
    :raises ErrorFamily if parent is not a Mouse
    '''
    if (isinstance(reference,int) and reference > Family.family_reference):
      self._reference = reference 
      Family.family_reference = reference
    else:
      Family.family_reference += 1
      self._reference = Family.family_reference
    
    if isinstance(parent,Mouse.Mouse):
      self._parent = parent
    else: 
      raise ErrorFamily.ErrorFamily("Parent should be a Mouse instance")
    if children == None:
      self.__children = []
    elif(isinstance(children,list)):
      for animal in children:
        if(not isinstance(animal, Mouse.Mouse)):
          raise ErrorFamily.ErrorFamily("The list of children should be a list of objects mouse")
      self.__children = children
    else: 
      raise ErrorFamily.ErrorFamily("The list of children should be a list of objects mouse")
    self._children_size = len(self.__children)

  def get_reference(self):
    return self._reference



  def set_reference(self,reference):
    if (isinstance(reference, int) and reference > 0):
      self._reference = reference
    else:
      raise ErrorFamily.ErrorFamily("The reference is not an integrer > 0 ")



  def get_parent(self):
    return self._parent

  def get_children(self):
    return self.__children

  def get_children_size(self):
    return self._children_size

  def add_children(self, children):
    if(not isinstance(children, Mouse.Mouse)):
      raise ErrorFamily.ErrorFamily("The children should be a mouse")
    self.__children.append(children)
    self._children_size = self._children_size + 1

  @abstractmethod
  def reproduce(self):
    pass

  def __str__(self):
    return ("FAMILY -> ref: "+ str(self._reference) + ", parent: " + str(self._parent))

  def __hash__(self):
    return hash(self._reference)

  def __eq__(self,other):
    if isinstance(other,self.__class__):
        return self._reference==other._reference
    else:
        return False

  def __repr__(self):
    return ("Reference: " + str(self._reference) +  ", parent: " + str(self._parent))

def main():
  try:
    mouse = Mouse.Mouse(name=None, gender=EnumsMouse.Gender.MALE, description="asd", chromosome1=EnumsMouse.Chromosome.X_MUTATED, chromosome2=EnumsMouse.Chromosome.Y_MUTATED)
    family = Family(mouse)
  except Exception as ef:
    print(str(ef))

if __name__ == '__main__':
  main()
