import os
import csv
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    flights = []
    with open("flights.csv", 'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)

        for row in csvreader:
            flights.append(row)

    total = len(flights) // 4

    idx = [i for i in range(total)]

    for num_cancelled in [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]:
        # temp = [num_cancelled]
        
        idx_cnc = np.random.choice(idx, num_cancelled, replace=False)
        flights_cnc = []

        # print(idx_cnc)

        for flight in idx_cnc:
            flights_cnc.append([flights[4*flight][1]])

        print(flights_cnc)

        with open("flights_cancelled.csv", 'w') as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(["FlightKey"])
            csvwriter.writerows(flights_cnc)


        os.system("time ./bin/python classical_csv.py")
    

    data = pd.read_csv("./output/summary.csv")

    data.sort_values("Search", inplace=True)

    plt.plot(data["Search"], data["Time"])
    plt.xlabel("Size of Search Space")
    plt.ylabel("Time (s)")
    plt.title("Time taken for classical algorithm to run")

    plt.savefig("./output/classical_search_time.png")
    

if __name__ == "__main__":
    main()