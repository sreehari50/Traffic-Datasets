import csv
with open('datasets3.csv', 'w') as csvfile:
    fieldnames = ['Time_interval', 'Arakuzha','Perumballoor','Reach_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    places={"Arakuzha","Perumballoor"}
    Time_interval={1,2,3,4,5}
    interval={"22:00-7:00","7:00-10:00","10:00-16:00","16:00-19:00","19:00-22:00"}
    for i in Time_interval:
        if i==1:
            for j in range(40,81,1):
                for k in range(j+10,j+16,1):
                    writer.writerow({'Time_interval':i, 'Arakuzha':j,'Perumballoor':k,'Reach_time':4.6/k+3.2/j})
        if i==2:
            for j in range(35,71,1):
                for k in range(j+10,j+16,1):
                    writer.writerow({'Time_interval':i, 'Arakuzha':j,'Perumballoor':k,'Reach_time':4.6/k+3.2/j})
        if i==3:
            for j in range(30,61,1):
                for k in range(j+6,j+11,1):
                    writer.writerow({'Time_interval':i, 'Arakuzha':j,'Perumballoor':k,'Reach_time':4.6/k+3.2/j})
        if i==4:
            for j in range(30,56,1):
                for k in range(j+10,j+15,1):
                    writer.writerow({'Time_interval':i, 'Arakuzha':j,'Perumballoor':k,'Reach_time':4.6/k+3.2/j})
        if i==5:
            for j in range(40,71,1):
                for k in range(j+10,j+16,1):
                    writer.writerow({'Time_interval':i, 'Arakuzha':j,'Perumballoor':k,'Reach_time':4.6/k+3.2/j})