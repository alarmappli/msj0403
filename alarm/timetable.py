# 요일과 교시
days = ["월요일", "화요일", "수요일", "목요일", "금요일"]
hours = [f"{i}교시" for i in range(1, 11)]
# 빈 시간표 만들기
timetable = []
for i in range(10): 
    row = []
    for j in range(5): 
        row.append("")
    timetable.append(row)

# 입력 멘트
print("대학교 시간표를 입력하세요!")
print("수업이 없으면 그냥 엔터를 누르세요.\n")

# 수업 입력
for day_index in range(5):
    day = days[day_index]
    print("[" + day + "] 시간표 입력")
    for hour_index in range(10):
        hour = hours[hour_index]
        subject = input(day + " " + hour + " 수업명: ")
        if subject == "":
            subject = "없음"
        timetable[hour_index][day_index] = subject

column_width = 10

# 시간표 출력
print("\n *대학교 시간표* ")
print("         ", end="")
for day in days:
    print(day.center(column_width), end="")
print()

for i in range(10):
    print(hours[i].ljust(column_width), end="")
    for j in range(5):
        print(timetable[i][j].center(column_width), end="")
    print()
