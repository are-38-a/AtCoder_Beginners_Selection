# https://atcoder.jp/contests/abs/tasks/abc081_b

def main():
    N = int(input())
    A = list(map(int, input().split()))
  
    counter = 0
    flg_odd = False
    while(flg_odd == False):
      
        #奇数がないか判定
        for i in range(N):
            if A[i]%2 == 1:
      	        flg_odd = True
    
        #奇数がなければ割る
        if flg_odd == False:
            for i in range(N):
                A[i] /= 2
            counter += 1

    print(counter)
        
if __name__ == "__main__":
  main()