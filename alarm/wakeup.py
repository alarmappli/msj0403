
while True:
    wake_up = input("기상하고 싶은 시간을 입력하세요 (예: 07:30): ")

    # 입력값을 ':'로 나누기
    if ":" in wake_up:
        parts = wake_up.split(":")

        if len(parts) == 2:
            hour = parts[0]
            minute = parts[1]

            # 숫자인지 확인
            if hour.isdigit() and minute.isdigit():
                hour = int(hour)
                minute = int(minute)

                # 시간과 분의 범위가 올바른지 확인
                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    print("기상 시간은 {:02d}시 {:02d}분입니다.".format(hour, minute))
                    break  # 입력이 올바르면 반복 종료
                else:
                    print("시간은 0~23, 분은 0~59 사이로 입력해주세요.")
            else:
                print("숫자 형식으로 입력해주세요. (예: 07:30)")
        else:
            print("시간 형식이 잘못되었습니다. (예: 07:30)")
    