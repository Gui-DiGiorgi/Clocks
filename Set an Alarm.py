# Using Python, with this you can ask the user to set an alarm with the weekday, hour and minute as a list, including invalid inputs
# Then use the list to check in with your clock, if it matches, then make it do something

def set_time(time_list,sett_list):
    time_list[i] = input(sett_list[i][0])
    try:
        time_list[i] = int(time_list[i])
        while not (sett_list[i][1]<=time_list[i]<sett_list[i][2]):
            print("Invalid value. Try again...")
            set_time(time_list,sett_list)
    except:
        print("Invalid input type. Try again...")
        set_time(time_list,sett_list)
    

imhd = ["","",""]

sett = [["min? ", 0, 60], ["hrs? ", 0, 24], ["day? ", 1, 8]]

semana = ["Dom","Seg","Ter","Qua","Qui","Sex","Sab"]

for i in range(len(imhd)):
    while type(imhd[i])!=int:
        set_time(imhd,sett)
        
imhd[2] = semana[imhd[2]-1]
