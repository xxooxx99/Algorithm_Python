#BAEKJOON 10813
'''
PSEUDO CODE
제한사항 
n,m map,split
바구니 초기화 -> 바구니에 동일한 공 번호 초기화
m만큼 추가 입력, a,b map,split, a는 바구니번호, b는 공번호
끝나면 교환된 번호 출력
'''

def RESTRICTION(N,M,i=None,j=None):
        if((1>N or N > 100) or (1 > M or M > 100)):
            return True
        
        if i is not None and j is not None:
            if i <1 or j > N:
                return True
        return False

def numberExchange(baskets,i,j):
     baskets[i], baskets[j] = baskets[j], baskets[i]
     
def main():
        #N과 M 입력받기
        N,M = map(int,input().split())

        #제한사항 확인
        if(RESTRICTION(N,M)) == True:
            raise ValueError("Restriction Error")
        

        #N개의 바구니 및 번호 초기화
        baskets = list(range(1,N+1))

        #M만큼 추가 입력 받기
        for _ in range(M):
            i,j = map(int,input().split())
            #i와 j에 대한 제한사항 확인
            if(RESTRICTION(N,M,i,j)) == True:
                 raise ValueError("RESTRICTION ERROR")

            #A B 주머니 속 번호 바꿔주는 함수
            
            numberExchange(baskets, i-1, j-1)

        print(" ".join(map(str,baskets)))

if __name__ == "__main__" :
     main()
