import hashlib

def solve(input: str):
  n = 0
  while True:
    hash = hashlib.md5(f"{input}{n}".encode()).hexdigest()
    if hash.startswith('00000'):
      return n
    n += 1

def solve2(input: str):
  n = 0
  while True:
    hash = hashlib.md5(f"{input}{n}".encode()).hexdigest()
    if hash.startswith('000000'):
      return n
    n += 1

if __name__ == '__main__':
  print(solve('bgvyzdsv'))
  print(solve2('bgvyzdsv'))