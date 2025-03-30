import pandas
import statistics
import numpy

df = pandas.read_excel("Southern Company - UA Innovate 2025 - Data File.xlsx")
df = df[["SchEndDateTime", "ActualEndDateTime"]]

df.insert(2, 'EndDiff', 0.0)

difference_times = []

for i in range(1336):
    scheduled_end = df.loc[i, "SchEndDateTime"]
    actual_end = df.loc[i, "ActualEndDateTime"]

    scheduled_end = scheduled_end.timestamp()
    actual_end = actual_end.timestamp()

    df.loc[i, "EndDiff"] = (scheduled_end - actual_end) / 3600
    
    
    if ((scheduled_end-actual_end)/3600) > 8000:
        continue
    difference_times.append((scheduled_end-actual_end) / 3600)


print(df)
print("Average Difference in Scheduled vs Actual End Times: ", sum(difference_times) / len(difference_times))
print("Standard Deviation of Difference in Scheduled vs Actual End Times: ", statistics.stdev(difference_times))


low_pris = []
med_pris = []

for i in range(1336):
    start_time = df.loc[i, "SchStartDateTime"]
    end_time = df.loc[i, "SchEndDateTime"]

    start_time = start_time.timestamp()
    end_time = end_time.timestamp()
    diff1 = (end_time-start_time) / 3600
    df.loc[i, "ScheduledDiff"] = diff1

    start_time = df.loc[i, "ActualStartDateTime"]
    end_time = df.loc[i, "ActualEndDateTime"]

    start_time = start_time.timestamp()
    end_time = end_time.timestamp()
    diff2 = (end_time-start_time) / 3600
    df.loc[i, "ActualDiff"] = diff2

    ratio = diff2/diff1
    df.loc[i, "Ratio"] = ratio

    if df.loc[i, "Priority"] == "Low":
        low_pris.append(ratio)
    else:
        med_pris.append(ratio)

low_pri_avg = sum(low_pris) / len(low_pris)
med_pri_avg = sum(med_pris) / len(med_pris)

print("Average Ratio of Low Priority Changes: ", low_pri_avg)
print("Average Ratio of Med Priority Changes: ", med_pri_avg)


    

