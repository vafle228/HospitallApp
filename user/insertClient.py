def swapToSec(str_time):
    str_time = str_time.split(':')
    return (int(str_time[0]) * 3600) + (int(str_time[1]) * 60)


def swapToTime(sec):
    hour = sec // 3600
    minute = (sec - (hour * 3600)) // 60
    return '{0}:{1}'.format(hour, str(minute).zfill(2))


def isFreeTime(startTime, endTime, que, client_referral):
    startTime = swapToSec(startTime)
    endTime = swapToSec(endTime)

    for client in que + client_referral:
        clientStart = swapToSec(client['time'])
        clientEnd = swapToSec(client['endTime'])

        if startTime == clientStart and endTime == clientEnd:
            return False
        if (clientStart < startTime < clientEnd) or (clientStart < endTime < clientEnd) or \
                (startTime < clientStart < endTime) or (startTime < clientEnd < endTime):
            return False
    return True


def createVariants(clients, waitTime, doctor, date):
    variants = []
    for client in clients:
        variant = ({'time': client['endTime'],
                    'endTime': swapToTime(swapToSec(client['endTime']) + waitTime),
                    'doctor': doctor.pk,
                    'date': date})
        if variant not in variants:
            variants.append(variant)
    return variants


def clientAppointment(wishedTime, waitTime, que, client_referral, doctor, date):
    backup_clients = [{'time': '0:00', 'endTime': '0:00', 'doctor': None, 'date': '01:01'}]

    if isFreeTime(wishedTime, swapToTime(swapToSec(wishedTime) + waitTime), que, client_referral):
        return {'time': wishedTime,
                'endTime': swapToTime(swapToSec(wishedTime) + waitTime),
                'doctor': doctor,
                'date': date}

    for client in que:
        for backup_client in backup_clients:
            time = swapToTime(waitTime + swapToSec(client['endTime']))
            if abs(swapToSec(wishedTime) - swapToSec(backup_client['endTime'])) > \
                    abs(swapToSec(wishedTime) - swapToSec(client['endTime'])) \
                    and isFreeTime(client['endTime'], time, que, client_referral):
                backup_clients.append(client)
    return createVariants(backup_clients[1:], waitTime, doctor, date)


def insertClient(wishedTime, waitTime, que, client_referral, date, doctor):
    return clientAppointment(wishedTime, waitTime, que, client_referral, doctor, date)

# 8:00 -> 10 => 8:00 до 8:10
# 8:00 -> 5 => 8:10 до 8:15
# 8:50 -> 30 => 8:50 до 9:20
# 9:00 -> 10 => 10:00 до 10:10 (9 до 10 и 8 до 9)
