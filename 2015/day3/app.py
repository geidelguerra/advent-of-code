def visit(input: str) -> set:
  x = y = 0
  visits = [(x, y)]

  for d in input:
    if d == '^':
      y += 1
    elif d == '>':
      x += 1
    elif d == '<':
      x -= 1
    elif d == 'v':
      y -= 1

    visits.append((x, y))

  return visits

def solve(input: str) -> int:
  return len(set(visit(input)))

def solve2(input: str) -> int:
  return len(set(visit(input[0::2]) + visit(input[1::2])))

if __name__ == '__main__':
  with open('input.txt', 'r') as file:
    input = file.read()
  print(solve(input))
  print(solve2(input))