"""
1. You’re invited to a potluck this week and decide to make your own special version of Potato Salad!
Below you’ll find a class called PotatoSalad, make a subclass of PotatoSalad called SpecialPotatoSalad.

2. Your special potato salad recipe is pretty similar to a regular potato salad, so let’s start with making that.

Create a new constructor for SpecialPotatoSalad that just calls the parent constructor for PotatoSalad. Make sure that SpecialPotatoSalad‘s constructor takes the same arguments as PotatoSalad.

3. The difference with your special potato salad is… you add raisins to it! You can’t remember when you started doing this, but Dolores always hoots about it at her potlucks and if that isn’t the nicest thing. You always use the full package of raisins for every potato salad you make, and each package has 40 raisins in it.

In your constructor for SpecialPotatoSalad, after making regular potato salad, set self.raisins = 40.
"""

class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions, raisins=None):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40

# done
