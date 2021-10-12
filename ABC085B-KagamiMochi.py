# https://atcoder.jp/contests/abs/tasks/abc085_b

def main():
  N = int(input())
  
  #円盤をlistに格納
  list_disk = []
  for _ in range(N):
    list_disk.append(int(input()))
    
  #setにして重複を排除
  set_disk = set(list_disk)
  
  #全部並べたものが最大なので枚数を数える
  ans = len(set_disk)
  
  print(ans)
  
if __name__ == "__main__":
  main()