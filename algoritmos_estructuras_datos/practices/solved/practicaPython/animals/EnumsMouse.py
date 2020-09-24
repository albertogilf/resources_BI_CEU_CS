import enum
import random

class Chromosome(enum.Enum):
    X = 1
    Y = 2
    X_MUTATED = 3
    Y_MUTATED = 4

    def __str__(self):
      return self.name
    
    @staticmethod
    def from_str(label):
      label = label.lower()
      if label == 'x':
        return Chromosome.X
      elif label == 'y':
        return Chromosome.Y
      elif label == 'x_mutated':
        return Chromosome.X_MUTATED
      elif label == 'y_mutated':
        return Chromosome.Y_MUTATED
      else:
        raise NotImplementedError

    @staticmethod
    def from_str_X(label):
      label = label.lower()
      if label == 'x':
        return Chromosome.X
      elif label == 'x_mutated':
        return Chromosome.X_MUTATED
      else:
        raise NotImplementedError

    @staticmethod
    def from_str_Y(label):
      label = label.lower()
      if label == 'y':
        return Chromosome.Y
      elif label == 'y_mutated':
        return Chromosome.Y_MUTATED
      else:
        raise NotImplementedError

class Gender(enum.Enum):
  MALE = 1
  FEMALE = 2
  def __str__(self):
    return self.name
  
  @staticmethod
  def from_str(label):
    label = label.lower()
    if label in ('male', 'man', 'guy', 'boy'):
      return Gender.MALE
    elif label in ('female', 'woman', 'girl'):
      return Gender.FEMALE
    else:
      raise NotImplementedError

def main():
  try:
    gender = Gender.from_str("FEMALE")
    print("Test right Gender From String passed")
  except NotImplementedError as nie:
    print("Test right Gender From String wrong")
  try:
    gender = Gender.from_str("FEMAL")
    gender = Gender.from_str(None)
    print("Test wrong Gender From String wrong")
  except NotImplementedError as nie:
    print("Test wrong Gender From String passed")

if __name__ == "__main__":
  main()
