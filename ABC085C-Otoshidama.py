# https://atcoder.jp/contests/abs/tasks/abc085_c

def main():
  N, Y = map(int, input().split())
  
  a, b, c = -1, -1, -1
  
  #全探索
  for i in range(N+1):
    for j in range(N+1-i):
      k = N - i - j
      kingaku = 10000*i + 5000*j + 1000*k
      #見つかったら出力
      if kingaku == Y:
        a, b, c = i, j, k
        break
         
    if a != -1:
      break

  print("{} {} {}".format(a,b,c))
  
if __name__ == "__main__":
  main()