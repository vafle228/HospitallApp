def swapToSec(time):
    time = time.split(':')
    return (int(time[0]) * 3600) + (int(time[1]) * 60)


def swapToTime(sec):
    hour = sec // 3600
    minute = (sec - (hour * 3600)) // 60
    return '{0}:{1}'.format(hour, str(minute).zfill(2))


def isFreeTime(startTime, endTime):
    startTime = swapToSec(startTime)
    endTime = swapToSec(endTime)

    for client in que + client_referral:
        clientStart = swapToSec(client['time'])
        clientEnd = swapToSec(client['endTime'])

        if (clientStart < startTime < clientEnd) or (clientStart < endTime < clientEnd) or \
                (startTime < clientStart < endTime) or (startTime < clientEnd < endTime):
            return False
    return True


def insertClient(name, wishedTime, waitTime):
    nearest_clients = [{'Name': 'test', 'time': '0:00', 'endTime': '0:00'}]
    backup_clients = [{'Name': 'test', 'time': '0:00', 'endTime': '0:00'}]

    if isFreeTime(wishedTime, swapToTime(swapToSec(wishedTime) + waitTime)):
        return {'Name': name, 'time': wishedTime, 'endTime': swapToTime(swapToSec(wishedTime) + waitTime)}

    for client in que + client_referral:
        for nearest_client in nearest_clients:
            if abs(swapToSec(wishedTime) - swapToSec(nearest_client['endTime'])) > \
               abs(swapToSec(wishedTime) - swapToSec(client['endTime'])) \
               and abs(swapToSec(wishedTime) - swapToSec(client['endTime'])) <= 3600 \
               and isFreeTime(client['endTime'], swapToTime(waitTime + swapToSec(client['endTime']))):
                nearest_clients.append(client)

        for backup_client in backup_clients:
            if abs(swapToSec(wishedTime) - swapToSec(backup_client['endTime'])) > abs(
               swapToSec(wishedTime) - swapToSec(client['endTime'])) >= 3600 \
               and isFreeTime(client['endTime'], swapToTime(waitTime + swapToSec(client['endTime']))):
                backup_clients.append(client)

    if len(nearest_clients):
        variants = []
        for nearest_client in nearest_clients[1:]:
            variants.append({'Name': name,
                             'time': nearest_client['endTime'],
                             'endTime': swapToTime(swapToSec(nearest_client['endTime']) + waitTime)}
                            )
        return variants
    else:
        variants = []
        for backup_client in backup_clients[1:]:
            variants.append({'Name': name,
                             'time': backup_client['endTime'],
                             'endTime': swapToTime(swapToSec(backup_client['endTime']) + waitTime)}
                            )
        return variants


que = [{'Name': 'Петя', 'time': '8:00', 'endTime': '8:12'},
       {'Name': 'Вася', 'time': '9:00', 'endTime': '9:12'}]

client_referral = [{'time': '8:20', 'endTime': '8:35'}]

print(insertClient('Вадим', '9:00', 600))

# 8:00 -> 10 => 8:00 до 8:10
# 8:00 -> 5 => 8:10 до 8:15
# 8:50 -> 30 => 8:50 до 9:20
# 9:00 -> 10 => 9:00 до 9:10 (9 до 10 и 8 до 9)
