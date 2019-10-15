"""
-----   __add__ magic method  -----

there are two classes defined, Atom and Molecule.

Give Atom a .__add__(self, other) method that returns a Molecule with the two Atoms.
"""

class Atom:
  def __init__(self, label):
    self.label = label

  def __add__(self, other):
    return Molecule([self, other])

class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms

sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
salt = sodium + chlorine


"""
--- other magic methods ---

1. In script you’ll find the class LawFirm. Give LawFirm a .__len__() method that will return the number of lawyers in the law firm.

2. Give LawFirm a .__contains__() method that takes two parameters: self and lawyer and checks to see if lawyer is in self.lawyers.
"""
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    return lawyer in self.lawyers

d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

# need to remaind it
