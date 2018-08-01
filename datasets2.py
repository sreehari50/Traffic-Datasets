import csv
with open('datasets2.csv', 'w') as csvfile:
    fieldnames = ['Time_interval', 'Vazhakulam','Avoly','Anicadu','Kizhakkekara','Reach_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    places={"Vazhakulam","Avoly","Anicadu","Kizhakkekara"}
    Time_interval={1,2,3,4,5}
    interval={"22:00-7:00","7:00-10:00","10:00-16:00","16:00-19:00","19:00-22:00"}
    for i in Time_interval:
        if i==1:
            for j in range(30,81,1):
                for k in range(j+10,j+30,1):
                    for l in range(35,71,1):
                        for m in range(30,61,1):
                            writer.writerow({'Time_interval':i, 'Vazhakulam':j,'Avoly':k,'Anicadu':l,'Kizhakkekara':m,'Reach_time': 2.8 / k + 1.5 / j+ 2.3/l+3.1/m})
        if i==2:
            for j in range(25,41,1):
                for k in range(j+10,j+20,1):
                    for l in range(30,71,1):
                        for m in range(30,61,1):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'Avoly': k, 'Anicadu': l, 'Kizhakkekara': m,
                                 'Reach_time': 2.8 / k + 1.5 / j+ 2.3/l+3.1/m})
        if i==3:
            for j in range(30,51,1):
                for k in range(j+20,j+30,1):
                    for l in range(40,70,1):
                        for m in range(30,50,1):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'Avoly': k, 'Anicadu': l, 'Kizhakkekara': m,
                                 'Reach_time': 2.8 / k + 1.5 / j+2.3/l+3.1/m})
        if i==4:
            for j in range(25,46,1):
                for k in range(j+10,j+15,1):
                    for l in range(20,26,1):
                        for m in range(20,36,1):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'Avoly': k, 'Anicadu': l, 'Kizhakkekara': m,
                                 'Reach_time': 2.8 / k + 1.5 / j+2.3/l+3.1/m})
        if i==5:
            for j in range(20,31,1):
                for k in range(j+10,j+41,1):
                    for l in range(40,60,1):
                        for m in range(30,60,1):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'Avoly': k, 'Anicadu': l, 'Kizhakkekara': m,
                                 'Reach_time': 2.8 / k + 1.5 / j+2.3/l+3.1/m}) 