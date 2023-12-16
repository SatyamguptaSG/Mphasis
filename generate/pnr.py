import csv
import random

def main():
    pnr = []

    flights = []

    with open("flights.csv", 'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)

        for row in csvreader:
            flights.append(row)


    low = [5000, 4500, 4000, 3500]
    high = [5500, 5000, 4500, 4000]

    key = 0
    for flight in flights:
        num = random.randint(int(flight[5]) - 20, int(flight[5]))
        while num <= 0:
            num = random.randint(int(flight[5]) - 20, int(flight[5]))
    
        for _ in range(num):
            score = random.randint(low[int(flight[0]) % 4], high[int(flight[0]) % 4])        
            pnr.append([key, flight[0], score])
            key += 1

    
    with open("pnr.csv", 'w') as f:
        csvwriter = csv.writer(f)

        csvwriter.writerow(["Key", "FlightKey", "Score"])
        csvwriter.writerows(pnr)

if __name__ == "__main__":
    main()
