import csv

riders_temp = []
with open("tourmanager4.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for i, rider in enumerate(csv_reader):
        if i > 0:
            riders_temp.append([rider[2], round(float(rider[-1]) / float(rider[5]), 1)])

l = sorted(riders_temp, key=lambda l: l[1], reverse=True)

with open("Tourmanager2020.txt", "w+", encoding="utf-8") as out:
    out.write("Rytter - Poeng / Pris\n\n")
    for x, y in l:
        out.write(f"{x} - {y}\n")
