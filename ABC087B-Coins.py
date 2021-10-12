# https://atcoder.jp/contests/abs/tasks/abc087_b

def main():
  A = int(input())
  B = int(input())
  C = int(input())
  X = int(input())
  
  counter = 0
  for i in range(A+1):
    for j in range(B+1):
      for k in range(C+1):
        sum = 500*i + 100*j + 50*k
        if sum == X:
          counter += 1

  print(counter)

        
if __name__ == "__main__":
  main()