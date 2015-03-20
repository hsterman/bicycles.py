class ClassName:
  "Optional class documentation string"

    
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
      
      
      
      
  
  

bicycle1 = Bicycle("two wheel","30", "100")
bicycle2 = Bicycle("tricycle", "20", "40")
bicycle3 = Bicycle("unicycle", "15", "20")
bicycle4 = Bicycle("moped", "35", "100")
bicycle5 = Bicycle("scooter", "35", "90")
bicycle6 = Bicycle("ten speed", "25", "70")



customer1 = Customer("Bill","$200")
customer2 = Customer("Betty", "$500")
customer3 = Customer("Bob", "$1000")
    
      
      
      
      
  
  
  
