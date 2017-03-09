class Car(object):
  def __init__(self, vehicle_type = None, model="GM", name="General"):
    self.model=model
    self.name=name
    self.vehicle_type=vehicle_type
    self.speed = 0
    
    if self.name is 'Porshe' or self.name is 'Koenigsegg':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
      
    if self.vehicle_type is 'trailer':
      self.num_of_wheels=8
    else:
      self.num_of_wheels=4
    
    
 
      
  def is_saloon(self):
    if self.vehicle_type is not 'trailer':
      self.vehicle_type = 'saloon'
      return True
    return False
      
      
  def drive(self,moving_speed):
    if self.vehicle_type is 'trailer':
      moving_speed=77
    else:
      moving_speed=pow(10,moving_speed)
      
      return moving_speed







