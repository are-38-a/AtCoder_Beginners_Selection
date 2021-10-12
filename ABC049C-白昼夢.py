# https://atcoder.jp/contests/abs/tasks/arc065_a
def main():
  S = input()
  
  flg_possible = True

  while 0 < len(S):
    if S[-5:] == "dream":
      S = S[:len(S)-5]
    elif S[-7:] == "dreamer":
      S = S[0:len(S)-7]
    elif S[-5:] == "erase":
      S = S[0:len(S)-5]
    elif S[-6:] == "eraser":
      S = S[0:len(S)-6]
    else:
      flg_possible = False
      break
    
  if flg_possible:
    print("YES")
  else:
    print("NO")
    
if __name__ == "__main__":
  main()