import math

def solution(progresses, speeds):
    answer = []
    days_left = []

    # �� ����� �Ϸ�Ǳ���� ���� �ϼ��� ���
    for progress, speed in zip(progresses, speeds):
        days = math.ceil((100 - progress) / speed)
        days_left.append(days)

    # ù ��° ����� ���� �ϼ� ����
    current_deploy_day = days_left[0]
    count = 1
    
    # ���� ��ɵ鿡 ���� ���� �ϼ��� ���
    for day in days_left[1:]:
        if day <= current_deploy_day:
            # ���� ���� �ϼ� ���� �Ϸ�Ǵ� ����̶�� ���� ī��Ʈ ����
            count += 1
        else:
            # ���� ���� �ϼ��� �Ѿ �Ϸ�Ǵ� ����̶�� ���ݱ����� ī��Ʈ �����ϰ� ���� �ϼ� ����
            answer.append(count)
            current_deploy_day = day
            count = 1

    # ������ ���� �ϼ��� ���� ��� ���� ����
    answer.append(count)

    return answer

# ���� ����
print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
