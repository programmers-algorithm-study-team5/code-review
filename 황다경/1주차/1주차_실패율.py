def solution(N, stages):
    # N = 전체 스테이지 개수
    # stages = 사용자가 현재 멈춰있는 스테이지 번호 배열
    # return = 실패율 높은 스테이지부터 내림차순 정렬한 숫자 배열

    # 1. 스테이지에 머무는 사용자 수를 딕셔너리 저장(N+1 제외)
    stage_count = {}
    for stage in stages:
        if stage <= N: 
            stage_count[stage] = stage_count.get(stage, 0) + 1

    # 2. 각 스테이지 순회하며 실패율 계산
    fail_rates = []
    total_users = len(stages)

    for stage in range(1, N + 1):
        if total_users == 0:
            fail_rate = 0
        else:
            stuck_users = stage_count.get(stage, 0)
            fail_rate = stuck_users / total_users
            total_users -= stuck_users
        fail_rates.append((stage, fail_rate))

    # 3. 내림차순 정렬(-x[1])
    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    answer = [stage for stage, _ in fail_rates]

    return answer
