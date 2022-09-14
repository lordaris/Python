morning = "12:01:00AM"
evening = "7:00:00PM"
midnight = "12:01:00PM"

def timeConversion(s):
    time = s[-2:]
    if time == "AM":
        s = s.replace("AM", "")
        s = s.split(sep=":")
        if s[0] == "12":
            s[0] = "00"
    elif time == "PM":
        s = s.replace("PM", "")
        s = s.split(sep=":")
        if s[0] == "12":
            pass
        elif int(s[0]) < 12:
            s[0] = str(int(s[0]) + 12)
    s = ":".join(s)
    return s

    

timeConversion(morning)
