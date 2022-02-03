def solution(play_time, adv_time, logs):
    play_time = toSec(play_time)
    adv_time = toSec(adv_time)
    all_time = [0 for i in range(play_time+1)]

    for log in logs :
        start, end = log.split('-')
        start = toSec(start)
        end = toSec(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)) : # 구간별 시청자수 기록
        all_time[i] += all_time[i-1]

    for i in range(1, len(all_time)) : # 모든 구간 시청자 누적 기록
        all_time[i] += all_time[i-1]

    most_view = 0
    max_time = 0
    for i in range(adv_time-1, play_time) :
        if i >= adv_time :
            if most_view < all_time[i] - all_time[i-adv_time] :
                most_view = all_time[i] - all_time[i-adv_time]
                max_time = i - adv_time+1
        else :
            if most_view < all_time[i] :
                most_view = all_time[i]
                max_time = i - adv_time+1
    return toHms(max_time)

    


def toSec(hms) :
    (hh,mm,ss) = hms.split(':')
    return int(hh)*3600 + int(mm)*60 + int(ss)

def toHms(sec) :
    hh = sec // 3600
    sec = sec - hh*3600
    mm = sec // 60
    ss = sec - mm*60
    return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)
    
