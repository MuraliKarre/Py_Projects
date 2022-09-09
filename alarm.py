from datetime import datetime
from playsound import playsound


print(datetime)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")

hour = alarm_time[0:2]
minute = alarm_time[3:5]
seconds = alarm_time[6:8]
time_period = alarm_time[9:11].upper()

print("Setting up time......")

while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if time_period == current_period:
        if hour == current_hour:
            if minute == current_minute:
                if seconds == current_seconds:
                    print("Wake Up!")
                    #playsound('audio.mp3')
                    break
# from datetime import datetime
# from playsound import playsound
# alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
# alarm_hour=alarm_time[0:2]
# alarm_minute=alarm_time[3:5]
# alarm_seconds=alarm_time[6:8]
# alarm_period = alarm_time[9:11].upper()
# print("Setting up alarm..")
# while True:
#     now = datetime.now()
#     current_hour = now.strftime("%I")
#     current_minute = now.strftime("%M")
#     current_seconds = now.strftime("%S")
#     current_period = now.strftime("%p")
#     if(alarm_period==current_period):
#         if(alarm_hour==current_hour):
#             if(alarm_minute==current_minute):
#                 if(alarm_seconds==current_seconds):
#                     print("Wake Up!")
#                     playsound('audio.mp3')
#                     break