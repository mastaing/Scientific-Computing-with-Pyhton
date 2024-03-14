def add_time(start,duration,day=""):
    
    start_time = start.split(" ")
    duration_time = duration.split(":")
    
    initial_time = start_time[0]
    initial_time = initial_time.split(":")

    list_day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    hours_initial = int(initial_time[0])
    minutes_initial =  int(initial_time[1])

    hours_duration = int(duration_time[0])
    minutes_duration = int(duration_time[1])
        
    new_hours = hours_initial + hours_duration
    total_hours = new_hours

    new_minutes = minutes_initial + minutes_duration

    day_past =""

    if new_minutes >= 60 :
                
        new_minutes -= 60
        new_hours += 1
        total_hours += 1
        
        if new_minutes < 10 :

            new_minutes = f"0{new_minutes}"

        else :
            pass

    else :
        if new_minutes < 10:
            new_minutes = f"0{new_minutes}"
        else : 
            pass
        pass

    if new_hours > 24 :
            
        x = new_hours / 24
        
            
        if x > 1 and start_time[1] == "PM":
            x = int(x)
            x += 1 
            day_past = f"({x} days later)"
            
            x -= 1
            
        elif x > 2 and start_time[1] == "AM" :
            x = int(x)
            day_past = f"({x} days later)"

        else :

            day_past = "(next day)"

        if start_time[1] == "PM" :
            x = int(x)    
            new_hours = new_hours - (24*x+12)
            
        else :
            x = int(x)
            new_hours = new_hours - 24*x

        if new_hours > 12 :

            acronym = "PM"
            new_hours -= 12

        elif new_hours == 0 :

            new_hours = 12
            acronym = "AM"
        else :

            acronym = "AM"
        
        
    elif new_hours > 12 and start_time[1] == "PM":

        new_hours -= 12

        acronym = "AM"

        day_past = "(next day)"

        

    elif new_hours > 12 and start_time[1] == "AM" :
        
        new_hours -= 12

        acronym = "PM"
        day_past = ""

    elif new_hours == 12 and start_time[1] == "AM" :
        
        acronym = "PM"
        day_past = ""
    

    else :
        acronym = f"{start_time[1]}"
        day_past = ""

    if day == "" and day_past != "" :
        new_time = f"{new_hours}:{new_minutes} {acronym} {day_past}"
    
    elif day == "" and day_past == "" :
        new_time = f"{new_hours}:{new_minutes} {acronym}"
    
    else :
        if start_time[1] == "PM" :
            total_hours += 12
            
        else :
            pass
    
        x = int(total_hours / 24)
        day = day.capitalize()
        actual_indice = list_day.index(day)
        new_indice = actual_indice + x
        
        while new_indice >= 7 :
            
            new_indice -= 7
            print(new_indice)

        actual_day = list_day[new_indice]

        if day_past != "" :
            new_time = f"{new_hours}:{new_minutes} {acronym}, {actual_day} {day_past}"

        else : 
            new_time = f"{new_hours}:{new_minutes} {acronym}, {actual_day}"
    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))
