import time

file = open("sub.srt", encoding="UTF-8")

li = file.readlines()
li_res = []
file.close()

skip = int(input('Enter number sek: '))

for i in range(len(li)//4):
	str1 = li[4*(i)]
	str2 = li[4*(i)+1]
	str3 = li[4*(i)+2]
	str4 = li[4*(i)+3]
	
	time1 = str2[:-22]
	time2 = str2[17:-5]
	
	time1_sek = (int(time1[:-6])*60+int(time1[3:-3]))*60+int(time1[6:])
	time2_sek = (int(time2[:-6])*60+int(time2[3:-3]))*60+int(time2[6:])

	time1_sek = time1_sek + skip;
	time2_sek = time2_sek + skip;

	time1_res = time.strftime("%H:%M:%S",time.gmtime(time1_sek))
	time2_res = time.strftime("%H:%M:%S",time.gmtime(time2_sek))
     
	str2 = time1_res + str2[8:-13] + time2_res + str2[25:]
	
	li_res.append(str1)
	li_res.append(str2)
	li_res.append(str3)
	li_res.append(str4)
	
	print(str2)
	
file_res = open("sub_res.srt", 'w', encoding="UTF-8")

file_res.writelines(li_res)

file_res.close()