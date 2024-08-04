'''
접근방식 
1. 각 라운드마다 참가자 번호 재배정
2. A와 B의 번호를 확인하여 동일해질때까지(라운드에서 만날때까지) 반복
3. A와 B의 번호가 서로 다르다면(라운드에서 만나지 않는다면) ROUND증가

제한사항
1. N은 2의 지수승이며 2^1 이상 2^20 이하
2. A와 B는 N 이하의 자연수이며 서로 달라야 함

Pseudo code
1.round 초기화
2.제한사항 함수 선언
3.'A'와 'B'가 동일한 번호를 가질때까지 반복
3-1.'A' 와 'B'의 번호를 (현재번호 +1) // 2로 계산
3-2. 만약 번호가 동일하지 않다면 round ++
'''

def solution(N, A, B):
    def RESTRICTION(N, A, B):
        # N은 2의 지수승이며 2^1 이상 2^20 이하
        if not (2 <= N <= 2**20):
            return False
        if (N & (N - 1)) != 0:
            return False
        
        # A와 B는 N 이하의 자연수이며 서로 달라야 함
        if not (1 <= A <= N and 1 <= B <= N and A != B):
            return False
        
        return True
    
    if not RESTRICTION(N, A, B):
        return "RESTRICTION ERROR"
    
    round = 0
    print(f"round: A={A}, B={B}")
    while A != B:
        A = (A+1) // 2
        B = (B+1) // 2
        round += 1
        print(f"{round}round: A={A}, B={B}")
    
    return round


#Test Case

print(solution(8,4,7))
'''0라운드 4,7 x
1라운드 2,4 x
2라운드 1,2 x
3라운드 1,1 0 - 3라운드 종료
'''
print(solution(8,2,7))
print(solution(8,1,3))

print(f"{solution(8, 4, 7)}")
print(f"{solution(32, 4, 7)}")
print(f"{solution(16, 1, 2)}")
print(f"{solution(64, 30, 59)}")
print(f"{solution(1048576, 1, 1048576)}")
