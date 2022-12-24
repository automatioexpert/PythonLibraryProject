import datetime

current_time=datetime.datetime.now()
print(current_time) #2022-12-24 16:46:44.198167

print(current_time.strftime("%a"))
print(current_time.strftime("%A"))
print(current_time.strftime("%H_%M_%S_%m_%d_%Y"))
print(current_time.strftime("%H_%M_%S_%m_%d_%Y.html")) #16_55_30_12_24_2022



