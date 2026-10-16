# Minimize Wait Time

A Python solution that finds the minimum total waiting time by serving shorter appointments first.

[min_wait_time.py](min_wait_time.py) sorts the appointment durations and multiplies each duration by the number of patients still waiting after it. The original list stays unchanged.

For `[15, 20, 10]`, the best order is `[10, 15, 20]`. The patients wait 0, 10, and 25 time units, giving a total of **35**. The program uses this sample list and prints the result.
