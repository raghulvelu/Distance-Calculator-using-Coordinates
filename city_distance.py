from math import radians, sin, asin, cos, sqrt
def dist(lat1, lat2, lon1, lon2):
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    z = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    x = 2 * asin(sqrt(z))
    r = 6371
    return (x * r)


lat1 = 13.011760
lon1 = 77.662532
lat2 = 12.958565
lon2 = 77.701304
print("City 1:", lat1, lon1)
print("City 2:", lat2, lon2)
form_dist = "{:.2f}".format(dist(lat1, lat2, lon1, lon2))
print ("City 1 and City 2 are " + form_dist + " KM apart")
