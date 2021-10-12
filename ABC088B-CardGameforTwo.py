# https://atcoder.jp/contests/abs/tasks/abc088_b

def main():
  N = int(input())
  A = list(map(int, input().split()))
  
  #何ターン目か
  t = 0
  
  #AliceとBobの得点
  alice = 0
  bob = 0
  
  while t<N:
    if t%2 == 0:
      alice += max(A)
    else:
      bob += max(A)
      
    A.pop(A.index(max(A)))
    t += 1
    
  ans = abs(alice - bob)
  print(ans)
  
if __name__ == "__main__":
  main()