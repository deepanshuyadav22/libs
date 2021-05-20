import time

seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)

for i in range (1,6):
   print(i)
   time.sleep(1)

#https://www.tutorialspoint.com/how-to-access-and-convert-time-using-the-time-library-in-python#:~:text=The%20time%20library%20in%20Python%20is%20used%20to,install%20it%20separately%20using%20the%20PIP%20package%20manager.
