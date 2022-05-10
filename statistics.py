
def calculateStats(numbers):
  computedStats = dict() 
  if len(numbers):
    computedStats['avg'] = sum(numbers) / len(numbers)
    computedStats['max'] = max(numbers)
    computedStats['min'] = min(numbers)
  else:
    computedStats['avg'] = float("nan")
    computedStats['max'] = float("nan")
    computedStats['min'] = float("nan")

  return computedStats 
