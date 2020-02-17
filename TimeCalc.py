

class MillisecondStamp:

    def __init__(self, time_stamp):
        try:
            self.fixed_time_stamp = fix_time(time_stamp)
            self.millisec = int(self.fixed_time_stamp[-3:])
            self.seconds = int(self.fixed_time_stamp[-6:-4]) * 1000
            self.minutes = int(self.fixed_time_stamp[-9:-7]) * (60 * 1000)
            self.hours = int(self.fixed_time_stamp[-12:-10]) * ((60 * 1000) * 60)
            self.total_ms = self.millisec + self.seconds + self.minutes + self.hours
        except ValueError:
            print('Value Error - CalcMs({timestamp})'.format(timestamp=time_stamp))


def fix_time(t):
    default = '00:00:00.000'
    if t == '':
        result = default
    else:
        if t[-4] != '.':
            t = t + '.000'
        if len(t) < 12:
            result = default[:12 - len(t)] + t
        else:
            result = t
    return result


def fix_stamp(t):
    if t < 10:
        t = "0" + str(t)
    return t


def fix_stamp_ms(t):
    default = "000"
    t = str(t)
    if len(t) < 3:
        t = default[:3 - len(t)] + t
    return t


def gen_time_stamp(milliseconds):
    millisecond_str = str(int(milliseconds))
    total_seconds = milliseconds / 1000
    millisec = fix_stamp_ms(int(millisecond_str[-3:]))
    second = fix_stamp(int(total_seconds % 60))
    minute = fix_stamp(int((total_seconds / 60) % 60))
    hour = fix_stamp(int((total_seconds / 60) / 60))
    return '{hour}:{minute}:{second}.{millisec}'.format(hour=hour, minute=minute, second=second, millisec=millisec)
