def solve(input: str) -> int:
  floor = 0
  for char in input:
    if char == '(':
      floor += 1
    elif char == ')':
      floor -= 1
  return floor

def solve2(input: str) -> int:
  pos = 1
  floor = 0
  for char in input:
    if char == '(':
      floor += 1
    elif char == ')':
      floor -= 1
    if floor == -1:
      return pos
    pos += 1

  return pos

if __name__ == '__main__':
  with open('input.txt', 'r') as file:
    input = file.read()
  print(solve(input))
  print(solve2(input))