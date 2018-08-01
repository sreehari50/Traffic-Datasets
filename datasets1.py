import csv

with open('datasets3copy.csv', 'w') as csvfile:
    fieldnames = ['Route','Time_interval', 'Kothamangalam','Mathirappilly','Karukadam','Puthuppady','Reach_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    places={"Kothamangalam","Mathirappilly","Karukadam","Puthuppady"}
    Time_interval={1,2,3,4,5}
    interval={"22:00-7:00","7:00-10:00","10:00-16:00","16:00-19:00","19:00-22:00"}
    for i in Time_interval:
        if(i==1):
            for j in range(40,90,1):
                for k in range(j+30,j+41,1):
                    writer.writerow({'Time_interval':i, 'Kothamangalam':j,'Mathirappilly':k,'Karukadam':k,
                                     'Puthuppady':k,
                                     'Reach_time':4.1/k + 2/j})
        if(i==2):
            for j in range(30,81,1):
                for k in range(j+30,j+51,1):
                    for l in range(20,31,1):
                        for m in range(30,41,1):
                            writer.writerow(
                                {'Time_interval': i, 'Kothamangalam': j, 'Mathirappilly': k, 'Karukadam': l, 
                                 'Puthuppady': m,
                                 'Reach_time': 4.1 / k +  2/j + 2.9/l +4.4/m})
        if(i==3):
            for j in range(20,95,1):
                for k in range(j+30,j+51,1):
                    for l in range(40,70,1):
                        for m in range(30,50,1):
                            writer.writerow(
                                {'Time_interval': i, 'Kothamangalam': j, 'Mathirappilly': k, 'Karukadam': l, 
                                 'Puthuppady': m,
                                 'Reach_time': 4.1 / k + 2 / j+2.9/l+4.4/m})
        if(i==4):
            for j in range(25,85,1):
                for k in range(j+30,j+51,1):
                    for l in range(20,26,1):
                        for m in range(20,36,1):
                            writer.writerow(
                                {'Time_interval': i, 'Kothamangalam': j, 'Mathirappilly': k, 'Karukadam': l,
                                 'Puthuppady': m,
                                 'Reach_time': 4.1 / k + 2/ j+2.9/l+4.4/m})
        if(i==5):
            for j in range(30,89,1):
                for k in range(j+30,j+51,1):
                    for l in range(40,60,1):
                        for m in range(30,60,1):
                            writer.writerow(
                                {'Time_interval': i, 'Kothamangalam': j, 'Mathirappilly': k, 'Karukadam': l, 
                                 'Puthuppady': m,
                                 'Reach_time':4.1 / k + 2/ j+2.9/l+4.4/m})










