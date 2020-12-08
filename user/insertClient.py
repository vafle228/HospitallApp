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

        if (clientStart < startTime < clientEnd) or (clientStart < endTime < clientEnd) or \
                (startTime < clientStart < endTime) or (startTime < clientEnd < endTime):
            return False
    return True


def createQue(profession, Doctor, Appointment):
    doctors, que = Doctor.objects.filter(profession=profession), []
    for doctor in doctors:
        appointments = Appointment.objects.filter(doctor=doctor)
        for appointment in appointments:
            que.append({'time': ':'.join(str(appointment.appointment_start).split(':')[:2]),
                        'endTime': ':'.join(str(appointment.appointment_end).split(':')[:2])
                        })
    return que


def createReferral(client, HospitalUser, Appointment):
    hospital_user = HospitalUser.objects.filter(name=client)[0]
    appointments = Appointment.objects.filter(client_name=hospital_user)
    referral = []

    for appointment in appointments:
        referral.append({'time': ':'.join(str(appointment.appointment_start).split(':')[:2]),
                         'endTime': ':'.join(str(appointment.appointment_end).split(':')[:2])
                         })
    return referral


def createVariants(clients, waitTime):
    variants = []
    for client in clients:
        variants.append({'time': client['endTime'], 'endTime': swapToTime(swapToSec(client['endTime']) + waitTime)})
    return variants


def clientAppointment(wishedTime, waitTime, que, client_referral):
    nearest_clients = [{'time': '0:00', 'endTime': '0:00'}]
    backup_clients = [{'time': '0:00', 'endTime': '0:00'}]

    if isFreeTime(wishedTime, swapToTime(swapToSec(wishedTime) + waitTime), que, client_referral):
        return {'time': wishedTime, 'endTime': swapToTime(swapToSec(wishedTime) + waitTime)}

    for client in que + client_referral:
        for nearest_client in nearest_clients:
            time = swapToTime(waitTime + swapToSec(client['endTime']))
            if abs(swapToSec(wishedTime) - swapToSec(nearest_client['endTime'])) > \
                    abs(swapToSec(wishedTime) - swapToSec(client['endTime'])) \
                    and abs(swapToSec(wishedTime) - swapToSec(client['endTime'])) <= 3600 \
                    and isFreeTime(client['endTime'], time, que, client_referral):
                nearest_clients.append(client)

        for backup_client in backup_clients:
            time = swapToTime(waitTime + swapToSec(client['endTime']))
            if abs(swapToSec(wishedTime) - swapToSec(backup_client['endTime'])) > abs(
                    swapToSec(wishedTime) - swapToSec(client['endTime'])) >= 3600 \
                    and isFreeTime(client['endTime'], time, que, client_referral):
                backup_clients.append(client)

    if len(nearest_clients[1:]):
        return createVariants(nearest_clients[1:], waitTime)
    return createVariants(backup_clients[1:], waitTime)


def insertClient(client, wishedTime, waitTime, profession, Doctor, Appointment, HospitalUser):
    que = createQue(profession, Doctor, Appointment)
    client_referral = createReferral(client, HospitalUser, Appointment)

    return clientAppointment(wishedTime, waitTime, que, client_referral)

# 8:00 -> 10 => 8:00 до 8:10
# 8:00 -> 5 => 8:10 до 8:15
# 8:50 -> 30 => 8:50 до 9:20
# 9:00 -> 10 => 9:00 до 9:10 (9 до 10 и 8 до 9)
