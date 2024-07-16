#Problem 1: Pokemon Class
class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

my_pokemon = Pokemon("Pikacu", "Electric")
print(my_pokemon.name)

Problem 2: Create Squirtle
class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })
    
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()

#Problem 3: Is Caught
class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = True

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": True
      })

squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()

Problem 4: Catch Pokemon
class Pokemon():
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = True

  def print_pokemon(self):
    print({'name': self.name, 'types': self.types,
           'is_caught': self.is_caught})

  def catch(self):
    self.is_caught = True

#Problem 5: Choose Pokemon
class Pokemon():
  def  __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False

  def print_pokemon(self):
      print( {
        "name": self.name,
        "types": self.types,
        "is_caught": self.is_caught
      })

  def catch(self):
    self.is_caught = True

  def choose(self):
      if self.is_caught:
          print(f"{self.name} I choose you!")
      else:
          print(f"{self.name} is wild! Catch them if you can!")

#Problem 6: Add Pokemon Type
class Pokemon():
    def  __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False
  
    def print_pokemon(self):
        print( {
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def catch(self):
      self.is_caught = True

    def choose(self):
      if self.is_caught:
            print(f"{self.name} I choose you!")
      else:
        print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

#Problem 7: Get Pokemon
class Pokemon:

  def find_pokemon(my_pokemon, pokemon_type):
      have_type = []

      for pokemon in my_pokemon:
          if pokemon_type in pokemon.types:
              have_type.append(pokemon)

      return have_type


    ## Testing example:
    have_type = find_pokemon(my_pokemon, pokemon_type)
    for pokemon in have_type:
      print(pokemon.name)
      
#Problem 8:
def evolve(starter_pokemon):
  evolution = [starter_pokemon]

  current_pokemon = starter_pokemon
  while current_pokemon.evolution:
    evolution.append(current_pokemon.evolution)
    current_pokemon = current_pokemon.evolution

  return evolution

# Testing:
evolution = evolve(charmander)
for pokemon in evolution:
  print(pokemon.name)
  