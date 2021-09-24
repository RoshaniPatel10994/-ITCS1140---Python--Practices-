class SnowRemoval():
  
  def __init__(self, sidwalk, driveway):
    self.sidwalk = sidwalk
    self.driveway = driveway
    self.total = self.CalculateTotal()
    
  # Calculate Total Cost
  def CalculateTotal(self):
    cost = self.sidwalk * 5

    if 0 <= self.driveway <= 3:
      cost += self.driveway * 10
    elif self.driveway >= 4:
      cost += 50
    self.total= cost

  # Return Total Cost
  def ReturnTotal(self):
    return self.total

# Define main
def main():
    snowRemoval = SnowRemoval(15,2)
    snowRemoval.CalculateTotal()
    print(snowRemoval.ReturnTotal())

main()
