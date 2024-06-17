'''Radio Stations'''
import json

def main(_, num):
    '''Radio station Greedy'''

    station = []
    result = []
    check = []
    check_dic = []

    for i in range(num):
        city_dic = json.loads(input())
        station.append(city_dic)

    most_city = sorted(station, key=lambda x: len(x["Cities"]), reverse=True)

    for i in most_city:
        count = 0
        new = []

        if result == []:
            result.append(i["Name"])
            check.extend(i["Cities"])
        else:
            for j in i["Cities"]:
                if j not in check:
                    count += 1
                    new.append(j)
            check_dic.append([i["Name"], new, int(count)])

    for i in sorted(check_dic, key=lambda x: x[2], reverse=True):
        if i[2] != 0 and all(city not in check for city in i[1]):
            result.append(i[0])
            check.extend(i[1])

    print(sorted(result))

main(json.loads(input()), int(input()))


'''
"""Radio Stations"""
import json
def findstations(stations, num):
    """finStations"""
    dic = {}
    result = []
    for _ in range(num):
        data = json.loads(input())
        dic[data["Name"]] = set(data["Cities"])
    while dic:
        best = max(dic, key=lambda x: len(dic[x].intersection(stations)))
        result.append(best)
        cover = dic[best]
        dic = {sta: city - cover for sta, city in dic.items()}
        dic = {sta: city for sta, city in dic.items() if city}
    print(sorted(result))
findstations(json.loads(input()), int(input()))
'''
