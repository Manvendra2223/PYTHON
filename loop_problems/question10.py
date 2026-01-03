

## Exponential Backoff 

## implement an exponential backoff strategy that doubles the wait time between retries, strating from 1 second, but stops after 5 retries.

import time

wait_time = 1  # initial wait time in seconds
max_retries = 5  # maximum number of retries
attempts = 0  # counter for attempts

while attempts < max_retries:
    print("Attempts",attempts+ 1, "wait_time", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1