import csv

def main():
    capacity = dict()
    with open('flights.csv', "r") as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            capacity[int(row[0])] = int(row[5])

    with open('pnr.csv', "r") as f:
        cr = csv.reader(f)
        h = next(cr)
        for row in cr:
            capacity[int(row[6])] -= int(row[3])

    with open('data/pnr_out.csv', "r") as f:
        cr = csv.reader(f)
        for row in cr:
            capacity[int(row[1])] -= int(row[3])

    with open('data/routes.txt', "r") as f:
        cr = csv.reader(f, delimiter=' ')
        for row in cr:
            n = int(row[0])
            mn = 1938484

            lst_flight = -1
            for i in range(1, n + 1):
                if capacity[int(row[i])] < mn:
                    mn = capacity[int(row[i])]
                    lst_flight = row[i]

            print(lst_flight, mn)


if __name__ == "__main__":
    main()

