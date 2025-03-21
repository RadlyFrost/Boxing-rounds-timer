import time
import winsound

total_rounds = int(input("Enter the number of rounds: "))
round_duration = int(input("Enter the duration of a round (in seconds): "))
break_duration = int(input("Enter the break duration (in seconds): "))

for round_num in range(1, total_rounds + 1):
    print(f"Round {round_num} has started! Get ready!")
    winsound.Beep(1000, 500)
    time.sleep(round_duration)
    
    print(f"Round {round_num} is over! Break for {break_duration} seconds.")
    winsound.Beep(1000, 500)
    time.sleep(break_duration)

print("All rounds are completed! Training is over.")
winsound.Beep(1000, 500)
