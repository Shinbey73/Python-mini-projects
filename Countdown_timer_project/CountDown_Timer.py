import time

def timer():

    print("\n================= COUNTDOWN TIMER =================\n")

    print("HI! I am a countdown timer. I will help you to count down the time.\n")
    print("Please enter the time in seconds and I will count down the time for you.\n")

    while True:
        try:
            input_time = int(input("Enter the time in second: "))
            
            if input_time < 0:
                raise positive
            
            if input_time == 0:
                print("Time is up!")
                return
                
            for i in range(input_time,0,-1):
                
                second = i % 60
                minute = i // 60
                hour = i // 3600
                print(f'{hour:02d}:{minute:02d}:{second:02d}', end='\r')
                time.sleep(1)
            print("Time is up!")
        
        except ValueError as positive:
            print("\nPlease enter a positive number.\n")
            continue
        


if __name__ == "__main__":
    timer()