class ClassName:
  "Optional class documentation string"
   class_suite
    
class Bicycle:
  "Common base class for all Bicycles"
  empCount = 0 
  def __init__(self, name, weight, cost):
      self.name = name 
      self.weight = weight
      self.cost = cost
      Bicycle.empCount +=1
      
      
class Shop:
  "Common base class for all Shops"
  empCount = 0    
      
  def __init__(self, name, inventory, cost, profit):
      self.name = name
      self.invetory = inventory
      self.cost = cost
      self.profit = profit
      Shop.empCount +=1
      
class Customers:
  "Common base class for all Customers"
  empCount = 0
  def __init__(self, name, fund, bicycle):
      self.name = name
      self.fund = fund
      self.bicycle = bicycle
      Shop.empCount +=1
      
      
      
      
  
  
  
