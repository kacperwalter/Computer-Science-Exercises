"""
1. We’ve defined an InsurancePolicy class. Create a subclass of InsurancePolicy called VehicleInsurance.

2. Create a different subclass of InsurancePolicy called HomeInsurance.

3. Give VehicleInsurance a .get_rate() method that takes self as a parameter. Return .001 multiplied by the price of the vehicle.

4. Give HomeInsurance a .get_rate() method that takes self as a parameter. Return .00005 multiplied by the price of the home.
"""

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.00005

# done
