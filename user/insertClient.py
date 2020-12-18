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


def clientAppointment(waitTime, que, client_referral, doctor, date):
    backup_clients = []

    for time in range(8, 22):
        if isFreeTime(swapToTime(3600 * time), swapToTime(time * 3600 + waitTime), que, client_referral):
            backup_clients.append({'time': swapToTime(3600 * time),
                                   'endTime': swapToTime(time * 3600 + waitTime),
                                   'doctor': doctor.pk,
                                   'date': date})

    for client in que:
        if isFreeTime(client['endTime'], swapToTime(swapToSec(client['endTime']) + waitTime), que, client_referral) \
           and swapToSec(client['endTime']) <= 3600 * 22 and swapToSec(client['endTime']) >= 3600 * 8:
            backup_clients.append({'time': client['endTime'],
                                   'endTime': swapToTime(swapToSec(client['endTime']) + waitTime),
                                   'doctor': doctor.pk,
                                   'date': date})
    return backup_clients


def insertClient(waitTime, que, client_referral, date, doctor):
    return clientAppointment(waitTime, que, client_referral, doctor, date)

# 8:00 -> 10 => 8:00 до 8:10
# 8:00 -> 5 => 8:10 до 8:15
# 8:50 -> 30 => 8:50 до 9:20
# 9:00 -> 10 => 10:00 до 10:10 (9 до 10 и 8 до 9)
