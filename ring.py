import datetime
import time
import winsound
import tkinter as tk
from threading import Thread

def show_wakeup_window():
    def on_click():
        print("기상 확인됨!")
        window.destroy()

    window = tk.Tk()
    window.title("기상 확인")
    window.geometry("300x150")
    
    label = tk.Label(window, text="일어났나요?", font=("Arial", 14))
    label.pack(pady=20)

    button = tk.Button(window, text="일어났어요!", font=("Arial", 12), command=on_click)
    button.pack()

    window.mainloop()

def set_alarm():
    alarm_time = input("알람 시간을 HH:MM 형식으로 입력하세요 (예: 07:30): ")

    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        print(f"알람이 {alarm_hour:02d}:{alarm_minute:02d}에 설정되었습니다.")
    except ValueError:
        print("올바른 형식으로 입력해주세요.")
        return

    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_minute:
            print("알람 시간입니다! 일어날 시간이에요!")
            for _ in range(5):
                winsound.Beep(1000, 1000)
                time.sleep(0.5)

            
            Thread(target=show_wakeup_window).start()
            break

        time.sleep(10)

if __name__ == "__main__":
    set_alarm()
