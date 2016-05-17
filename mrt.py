import json
import urllib.request
from tkinter import *
from tkinter import ttk

stations = "http://data.kaohsiung.gov.tw/Opendata/DownLoad.aspx?Type=2&CaseNo1=AP&CaseNo2=17&FileType=2&Lang=C&FolderType="
station_data = json.loads(urllib.request.urlopen(stations).read().decode('utf8'))

stations_by_name = {}
stations_by_code = {}
for stop in station_data:
	stations_by_name["{} {}".format(stop["ODMRT_Name"], stop["ODMRT_CName"])] = int(stop["ODMRT_Code"])
	stations_by_code[int(stop["ODMRT_Code"])] = "{} {}".format(stop["ODMRT_Name"], stop["ODMRT_CName"])

	#key: code and name, #value: code
data = 0
def printer(value):
	c_station_code = stations_by_name[value]
	current_station_code.set(c_station_code)
	url = "http://data.kaohsiung.gov.tw/Opendata/MrtJsonGet.aspx?site={}".format(c_station_code)
	response = urllib.request.urlopen(url)
	data = json.loads(response.readline().decode('utf8')) #this is now json string
	for rowx in range(len(data['MRT'])):
		entry = data['MRT'][rowx]
		Label(root, text='Train from {} to {} will arrive in {} minute(s) and {} minute(s)'.format(value, entry['descr'], entry['arrival'], entry['next_arrival'])).grid(row=2+rowx, column=0)


root = Tk()
root.title("Kaohsiung MRT Live")

station_name = StringVar()
station_name.set("Select station")

current_station_code = StringVar()
l = Label(root, textvariable=current_station_code).grid(row=1, column=0, columnspan=3)


drop = OptionMenu(root, station_name, *stations_by_code.values(), command=printer).grid(row=0, column=0, columnspan=3)
root.grid_columnconfigure(1, minsize=12)
print(data)	

root.mainloop()

# found = 0
# while (not found):
# 	station_query = input("What station are you at: ")
# 	for stop in station_data:
# 		if stop["ODMRT_Name"] == station_query:
# 			station_code = stop["ODMRT_Code"]
# 			station_name = stop["ODMRT_CName"]
# 			found = 1
# 			break
# station_code = 204
# url = "http://data.kaohsiung.gov.tw/Opendata/MrtJsonGet.aspx?site={}".format(station_code)
# response = urllib.request.urlopen(url)
# data = response.readline().decode('utf8') #this is now json string

# data = json.loads(data)



# for entry in data['MRT']:
	# print('Train from {} to {} will arrive in {} minute(s) and {} minute(s)'.format(station_name, entry['descr'], entry['arrival'], entry['next_arrival']))