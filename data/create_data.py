#!/usr/bin/python
random.seed()
LOCATION_BOUNDARY=[(42,75), (42, 73), (40,75), (40, 73)] #[NW, NE, SW, SE] 
cur={}
cur["Users"]=[]
cur["Stations"]=[]
cur["Docks"]=[]
cur["Bikes"]=[]
cur["Docked_Bikes"]=[]
cur["Trips"]=[]
cur["Reviews"]=[]
def make():
    f0 = open("users.csv", "w")
    n=0
    f0.write("uid, name, location, is_active")
    while n<13:
        m = str(n)
        eth = 'y'
        if random.randint(0, 1) is 0:
            eth='n'
        cur["Users"].append((m, "user_"+m , "("+str(random.randrange(40, 42))+"-"+str(random.randrange(73, 75))+")", eth))
        f0.write(", ".join(cur["Users"][-1]))
        n=n+1
    f0.close()

    f0 = open("stations.csv", "w")
    f0.write("sid, location, name, in_service")
    n=0
    while n<6:
        m=str(n)
        eth="y"
        if random.randint(0, 1) is 0:
            eth="n"
        cur["Stations"].append((m, "("+ str(random.randrange(40, 42))+"-"+str(random.randrange(73, 75))+")", "station_"+m, eth ))
        f0.write(", ".join(cur["Stations"][-1]))
        n=n+1
    f0.close()

    f0 = open("docks.csv", "w")
    f0.write("sid, did")
    n=0
    while n<30:
        m=str(random.randint(0, 6))
        cur["Docks"].append((m, str(n)))
        f0.write(", ".join(cur["Docks"][-1]))
        n=n+1
    f0.close()
    f0 = open("bikes.csv", "w")
    f0.write("bid, in_service")
    n=0
    while n<30:
        m=str(n)
        eth="y"
        if random.randint(0,1) is 0:
            eth='n'
        cur["Bikes"].append((m,eth))
        f0.write(", ".join(cur["Bikes"][-1]))
        n=n+1
    f0.close()

    f0 = open("docked_bikes.csv", "w")
    f0.write("bid, did, sid\n")
    n=0
    while n<12:
        dock = random.randint(0, 30)
        dks = cur["Docks"]
        bike = random.randint(0,30)
        for d in dks:
            if d[1] is str(dock):
                sts = cur["Stations"]
                for s in sts:
                    if s[0] is d[0]:
                        cur["Bikes"].append(())



