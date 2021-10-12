# https://atcoder.jp/contests/abs/tasks/abc083_b

def sum_digit(num :int):
  s = str(num)
  list_num = list(map(int, s))
  sum_num = sum(list_num)
  return sum_num

def main():
  N, A, B = map(int, input().split())
  ans = 0
  
  for i in range(N+1):
    sum_num = sum_digit(i)
    if A <= sum_num <= B:
      ans += i
      
  print(ans)
  
  
        
if __name__ == "__main__":
  main()