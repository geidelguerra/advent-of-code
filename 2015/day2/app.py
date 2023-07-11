def solve(input: list[str]) -> int:
  total = 0
  for item in input:
    [l, w, h] = [int(x) for x in item.split('x')]
    area = (2*l*w + 2*w*h + 2*h*l) + min(l*w, w*h, h*l)
    total += area
  return total

def solve2(input: list[str]) -> int:
  total = 0
  for item in input:
    [l, w, h] = [int(x) for x in item.split('x')]
    total += (min(l+w, w+h, h+l) * 2) + (l * w * h)
  return total

def calc_perimeter(a: int, b: int) -> int:
  return (a + b) * 2

if __name__ == '__main__':
  with open('input.txt', 'r') as file:
    input = file.readlines()
  print(solve(input))
  print(solve2(input))