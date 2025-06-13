import requests
import datetime
import datetime
import time
import winsound
import tkinter as tk
from threading import Thread
from ring import set_alarm
import threading

KAKAO_API_KEY = '606eb0e1026765fdeb477779e4235c7d'

def search_location(place):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    headers = {'Authorization': f'KakaoAK {KAKAO_API_KEY}'}
    params = {'query': place}

    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        data = res.json()

        if data['documents']:
            x = float(data['documents'][0]['x'])
            y = float(data['documents'][0]['y'])
            return x, y
        else:
            print(f"'{place}' 검색 결과 없음.")
            return None, None
    except Exception as e:
        print("장소 검색 실패:", e)
        return None, None

def get_route_duration(start_x, start_y, end_x, end_y):
    url = 'https://apis-navi.kakaomobility.com/v1/directions'
    headers = {'Authorization': f'KakaoAK {KAKAO_API_KEY}'}
    params = {
        'origin': f'{start_x},{start_y}',
        'destination': f'{end_x},{end_y}'
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        data = res.json()

        if 'routes' in data and data['routes']:
            duration_sec = data['routes'][0]['summary']['duration']
            return duration_sec // 60
        else:
            print("경로 정보 없음.")
            return None
    except Exception as e:
        print("경로 계산 실패:", e)
        return None

def get_wakeup_time(travel_minutes):
    print("\n=== 기상 시간 계산===")


    prep_input = input("준비 시간(분)을 입력하세요: ")
    prep_minutes = int(prep_input)

    arrival_input = input("도착해야 할 시각을 입력하세요 (예: 08:30): ")
    hour_str, minute_str = arrival_input.split(":")
    arrival_hour = int(hour_str)
    arrival_minute = int(minute_str)

    now = datetime.datetime.now()
    arrival_time = datetime.datetime(
        year=now.year,
        month=now.month,
        day=now.day,
        hour=arrival_hour,
        minute=arrival_minute
    )

    total_minutes = prep_minutes + travel_minutes
    wakeup_time = arrival_time - datetime.timedelta(minutes=total_minutes)

    print("\n===================================")
    print("당신이 일어나야 할 시간은:")
    print(">>", wakeup_time.strftime("%H:%M"))
    print("===================================")


    set_alarm(wakeup_time.hour, wakeup_time.minute)



def main():
    print("교통 소요 시간 계산기")

    while True:
        start = input("출발지 입력: ").strip()
        end = input("도착지 입력: ").strip()

        sx, sy = search_location(start)
        ex, ey = search_location(end)

        if sx is None or sy is None or ex is None or ey is None:
            print("장소를 찾을 수 없습니다. 다시 입력해주세요.\n")
            continue

        time_min = get_route_duration(sx, sy, ex, ey)
        if time_min is not None:
            print(f"예상 소요 시간: {time_min}분")
            get_wakeup_time(time_min)
        else:
            print("소요 시간 계산 실패.")
        break



def set_alarm(hour, minute):
    print(f"⏰ 알람이 {hour:02d}:{minute:02d}에 설정되었습니다.")

    def alarm_thread():
        while True:
            now = datetime.datetime.now()
            target = datetime.datetime(now.year, now.month, now.day, hour, minute)

            if now >= target:
                print("🔔 알람 시간입니다! 일어나세요!")
                for _ in range(5):
                    winsound.Beep(1000, 1000)  # 1초짜리 삐 소리
                    time.sleep(0.5)
                threading.Thread(target=show_wakeup_window).start()
                break

            time.sleep(1)

    threading.Thread(target=alarm_thread).start()

def show_wakeup_window():
    window = tk.Tk()
    window.title("알람")
    label = tk.Label(window, text="일어날 시간입니다!", font=("Arial", 18))
    label.pack(pady=20)
    
    button = tk.Button(window, text="일어남!", font=("Arial", 12), command=window.destroy)
    button.pack(pady=10)
    
    window.mainloop()


if __name__ == '__main__':
    main()