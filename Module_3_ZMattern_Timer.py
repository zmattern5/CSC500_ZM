
def alarm_check():
    #24 Hours is used for military time so stop there
    hours_to_stop = int(24)
    #All input to be string to allow for minutes potentially being selected
    current_time = (input('Enter Current Time in Military Time (Hours or hh:mm format) : '))
    #Enter the number of hours to wait
    hours_to_wait = (int(input('How many hours do you want to wait for the Alarm: ')))
    #If Minutes are included in the input then assign them
    if ':' in current_time:
        split_current_time = current_time.split(':')
        #split_currenttime = current_Time.split(':')
        current_hours = split_current_time[0]
        current_minutes = split_current_time[1]
    #If no minutes assigned default to 00 minutes
    else:
        current_hours = current_time
        current_minutes = '00'
    #Loop for each hour that was added from the input as Hours to Wait
    for i in range(0,hours_to_wait):
        #If current hours are less then the stopping point then increment
        if int(current_hours) < hours_to_stop:
            current_hours = (int(current_hours) + 1)
        #If current hours is currently 24 then reset back to 0
        else:
            current_hours = 0
    #Join hours and minutes
    set_alarm = (str(current_hours)+":"+current_minutes)
    #Clean string
    set_alarm = set_alarm.replace(" ", "")
    print('Alarm time will be:',set_alarm)

alarm_check()