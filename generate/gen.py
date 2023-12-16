import random
import csv

def main():
    hub = 3
    mid = 0
    small = 0

    hubs = []
    mids = []
    smalls = []

    hh = 1
    hm = 1
    hs = .1
    ms = .2
    mm = .5
    ss = .05

    epoch = 172800

    for i in range(1, hub + 1):
        hubs.append(i);

    for i in range(hub + 1, hub + mid + 1):
        mids.append(i);

    for i in range(hub + mid + 1, hub + mid + small + 1):
        smalls.append(i);

    flights = []

    count = 0

    num_hh = round(hub * (hub - 1) * hh)
    num_hm = round(hub * mid * hm)
    num_hs = round(hub * small * hs)
    num_mm = round(mid * (mid - 1) * ms)
    num_ms = round(mid * small * mm)
    num_ss = round(small * (small - 1) * ss)

    total = num_hh + 2 * (num_hm + num_hs + num_ms) + num_mm + num_ss

    print(total)

    if(total > 4000):
        return

    low_time_hh = 3600 * 2
    high_time_hh = 3600 * 4
    low_time_hm = 3600 * 1.5
    high_time_hm = 3600 * 3
    low_time_hs = 3600 * 1.5
    high_time_hs = 3600 * 3
    low_time_ms = 3600 * 1
    high_time_ms = 3600 * 2
    low_time_mm = 3600 * 1.5
    high_time_mm = 3600 * 2.5
    low_time_ss = 3600 * 1
    high_time_ss = 3600 * 1.5

    low_capacity_hh = 200
    high_capacity_hh = 400
    low_capacity_hm = 200
    high_capacity_hm = 400
    low_capacity_hs = 100
    high_capacity_hs = 200
    low_capacity_ms = 150
    high_capacity_ms = 300
    low_capacity_mm = 150
    high_capacity_mm = 300
    low_capacity_ss = 100
    high_capacity_ss = 150


    flights = []

    count = 0 

    for i in range(0, num_hh):
        x = random.choice(hubs)
        y = random.choice(hubs)
        while x == y:
            y = random.choice(hubs)
        
        capacity = random.randint(low_capacity_hh, high_capacity_hh)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_hh, high_time_hh)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        """
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1
        """

    for i in range(0, num_hm):
        x = random.choice(hubs)
        y = random.choice(mids)

        capacity = random.randint(low_capacity_hm, high_capacity_hm)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_hm, high_time_hm)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1

    for i in range(0, num_hm):
        x = random.choice(mids)
        y = random.choice(hubs)

        capacity = random.randint(low_capacity_hm, high_capacity_hm)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_hm, high_time_hm)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1

    for i in range(0, num_hs):
        x = random.choice(hubs)
        y = random.choice(smalls)

        capacity = random.randint(low_capacity_hs, high_capacity_hs)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_hs, high_time_hs)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1
    
    for i in range(0, num_hs):
        x = random.choice(smalls)
        y = random.choice(hubs)

        capacity = random.randint(low_capacity_hs, high_capacity_hs)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_hs, high_time_hs)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1

    for i in range(0, num_mm):
        x = random.choice(mids)
        y = random.choice(mids)

        while x == y:
            y = random.choice(mids)

        capacity = random.randint(low_capacity_mm, high_capacity_mm)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_mm, high_time_mm)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1

    for i in range(0, num_ms):
        x = random.choice(mids)
        y = random.choice(smalls)

        capacity = random.randint(low_capacity_ms, high_capacity_ms)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_ms, high_time_ms)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1

    for i in range(0, num_ms):
        x = random.choice(smalls)
        y = random.choice(mids)

        capacity = random.randint(low_capacity_ms, high_capacity_ms)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_ms, high_time_ms)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1

    for i in range(0, num_ss):
        x = random.choice(smalls)
        y = random.choice(smalls)

        while x == y:
            y = random.choice(smalls)

        capacity = random.randint(low_capacity_ss, high_capacity_ss)
        fc = round(capacity * 0.1)
        bc = round(capacity * 0.2)
        pc = round(capacity * 0.3)
        ec = capacity - fc - bc - pc

        dept = random.randint(1, epoch)
        arr = dept + random.randint(low_time_ss, high_time_ss)

        flight_num = random.randint(1, 20000)

        flights.append([count, flight_num, x, y, "FC", fc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "BC", bc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "PC", pc, dept, arr])
        count += 1
        flights.append([count, flight_num, x, y, "EC", ec, dept, arr])
        count += 1

    fields = ["UniqueId", "FlightNumber", "DeptAirport", "ArrAirport", "Class", "Capacity", "DeptTime", "ArrTime"]

    with open('flights.csv', 'w') as f:
        write = csv.writer(f)

        write.writerow(fields)
        write.writerows(flights)

if __name__ == "__main__":
    main()
