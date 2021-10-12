# https://atcoder.jp/contests/abs/tasks/abc086_a

def main():
  a, b = map(int, input().split())
  
  if a*b%2 == 1:
    ans = "Odd"
  else:
    ans = "Even"
    
  print(ans)
 
if __name__=="__main__":
  main()