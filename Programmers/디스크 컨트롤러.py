import heapq as hq

def solution(jobs):
    answer = 0
    ready = []
    jobs.sort(key=lambda x:(x[0], x[1]))
    length = len(jobs)
    time = 0
    while jobs or ready:
        # 요청순으로 정렬된 작업들에서 요청이 가장빠른친구의 시작시간이 time보다 빠른경우
        # time은 이전의 작업이 종료되는 시간
        if jobs and time >= jobs[0][0]:
            # 작업종료가 빠른순으로 나오도록
            hq.heappush(ready, (jobs[0][1], jobs.pop(0)))
            continue
        
        if ready: # 대기중인 작업이 있다면
            #아이템을 빼서 시간 계산
            item = hq.heappop(ready)
            time += item[1][1]
            answer += time - item[1][0]
            
        else: # 대기중인 작업이 없다면 시간을 다음 작업이 시작할 수 있도록 점프
            time = jobs[0][0]
        
    return answer//length