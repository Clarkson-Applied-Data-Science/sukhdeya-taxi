#!/usr/bin/env python
# coding: utf-8

# ## 1) a) Number of rows 

# In[64]:


import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))

fn = 'trip_data_6.csv'

f = open(fn, 'r')
reader = csv.reader(f)
n = 0
for row in reader:
    print(row)
    print(len(row))
    n+=1
    if n ==2:
        break
          

    


# ## 1) b) Date time range

# In[66]:


import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))
fn = 'trip_data_6.csv'
lst =[]
f = open(fn, 'r')
reader = csv.reader(f)
import datetime
#fn = 'trip_data_6.csv'

#f = open(fn, 'r')
#reader = csv.reader(f)
minval = None
maxval = None
n = 0
for row in reader:
    if n > 0:
        dto = None
        dts = row[5]
        try:
            dto = datetime.datetime.strptime(dts,"%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(e)
        if dto is not None:
            if maxval is None or dto > maxval:
                maxval = dto
            elif minval is None or dto < minval:
                minval = dto
    n+=1
lst.append(minval)
lst.append(maxval)


# In[67]:


import datetime,csv
fn = 'trip_data_6.csv'
#import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))

#fn = 'trip_data_6.csv'

f = open(fn, 'r')
reader = csv.reader(f)
#f = open(fn, 'r')
#reader = csv.reader(f)
minval = None
maxval = None
n = 0
for row in reader:
    if n > 0:
        dto = None
        dts = row[6]
        try:
            dto = datetime.datetime.strptime(dts,"%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(e)
        if dto is not None:
            if maxval is None or dto > maxval:
                maxval = dto
            elif minval is None or dto < minval:
                minval = dto
    n+=1
lst.append(minval)
lst.append(maxval)
print(lst)


# In[68]:


print(max(lst), min(lst))


# ## Part 2) 

# ### Part 3) & Part 4)

# In[63]:


import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))

fn = 'trip_data_6.csv'

f = open(fn, 'r')
reader = csv.reader(f)
n=0
for row in reader:
  for i in range(14):
    if i!=13:
      print(row[i], end='|')
    else:
      print(row[i])
  
  if n ==0:
    print('---------------------------|'*14)
  n+=1
  if n==5:
    break


# medallion| hack_license| vendor_id| rate_code| store_and_fwd_flag| pickup_datetime| dropoff_datetime| passenger_count| trip_time_in_secs| trip_distance| pickup_longitude| pickup_latitude| dropoff_longitude| dropoff_latitude
# ---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
# D1C79CF706C80D3A1DC7FBCA6CD56E43|DAC7742E8F00034774098DBC6B4FF2B7|CMT|1|N|2013-06-03 00:02:12|2013-06-03 00:10:07|1|474|1.30|-73.981583|40.773529|-73.981827|40.782124
# 3567E8B49FEBFCBB587F1864D723D5C8|430B8022563CDE1D51D44786DFD8D6CB|CMT|1|N|2013-06-03 00:03:03|2013-06-03 00:19:27|1|982|4.90|-73.999565|40.728367|-73.952927|40.729546
# 4220E1995D36A40DF34664AD33ED13F6|48A1C9C9300AFC7BDBB718CE308EE45A|CMT|2|N|2013-06-03 00:01:30|2013-06-03 00:28:11|1|1745|17.70|-73.788445|40.641151|-73.985451|40.744194
# 440900089FF528A873424DED689C77A3|E6A63B40E565A8A03AF32E0B138F5EB1|CMT|1|N|2013-06-03 00:04:14|2013-06-03 00:27:50|1|1415|12.10|-73.862816|40.768875|-74.008797|40.738842
# 
# ```
# # This is formatted as code
# ```
# 
# 

# ## Part 5)

# In[69]:


import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
f = open('trip_data_6.csv', 'r')
reader = csv.reader(f)
mlong = 0
nlong = 0
mlat = 0 
nlat = 0
ex =0
for row in reader:
  try:
    if float(row[10]) >= float(row[12]) and float(row[10]) >= mlong:
      mlong = float(row[10])
    elif float(row[10]) <= float(row[12]) and float(row[10]) <= nlong:
      nlong = float(row[10])
    elif float(row[12]) >= float(row[10]) and float(row[12]) >= mlong:
      mlong = float(row[12])
    elif float(row[12]) <= float(row[10]) and float(row[12]) <= nlong:
      nlong = float(row[12])
    
    if float(row[11]) >= float(row[13]) and float(row[11]) >= mlat:
      mlat = float(row[11])
    elif float(row[11]) <= float(row[13]) and float(row[11]) <= nlat:
      nlat = float(row[11])
    elif float(row[13]) >= float(row[11]) and float(row[13]) >= mlat:
      mlat = float(row[13])
    elif float(row[13]) <= float(row[11]) and float(row[13]) <= nlat:
      nlat = float(row[13])
  except Exception as e:
    ex+=1


print(ex, mlong,nlong, mlat,nlat)


# ### Part 6)

# In[73]:


#import csv
from math import radians, cos, sin, asin, sqrt

import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))

#fn = 'trip_data_6.csv'

f = open('trip_data_6.csv', 'r')
reader = csv.reader(f)

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


n=0
hd = 0.0
ex_dp =0
x = []
for row in reader:
  n+=1
  try:
    a,b,c,d = float(row[10]),float(row[11]),float(row[12]),float(row[13])
    hd += haversine(a,b,c,d)
    #print(hd)
    x.append(haversine(float(row[10]),float(row[11]),float(row[12]),float(row[13])))
  except Exception as e:
    ex_dp +=1
    #print(float(row[10]),float(row[11]),float(row[12]),float(row[13]))
    #print(e)
  #if n==5000:
    #break
       

    


# In[74]:


print("Average Haversine Distance =", hd/(n-ex_dp) )


# In[75]:


print(x[:5])
mx = max(x)
mn = min(x)
print(mx,mn)


# In[78]:


print(x[:5])
#import matplotlib
from matplotlib import pyplot as plt
plt.style.use('seaborn')
import numpy as np
 
# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(x, bins = [0,5,10,15,20,25,30])
 
# Show plot
plt.show()

fig, ax = plt.subplots(figsize =(10, 5))
ax.hist(x, bins = [0,2500, 5000,7500,10000,12500])
 
# Show plot
plt.show()


# ##Part 7)

# In[86]:


from math import radians, cos, sin, asin, sqrt

import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))

fn = 'trip_data_6.csv'
n=0
med = dict()
hack_l = dict()
vid = dict()
rc= dict()
snff= dict()
pc = dict()
tt = dict()
f = open(fn, 'r')
reader = csv.reader(f)
for row in reader:
  if row[0] in med:
    med[row[0]]+=1
  else:
    med[row[0]]=1

  if row[1] in hack_l:
    hack_l[row[1]]+=1
  else:
    hack_l[row[1]]=1

  if row[2] in vid:
    vid[row[2]]+=1
  else:
    vid[row[2]]=1

  if row[3] in rc:
    rc[row[3]]+=1
  else:
    rc[row[3]]=1

  if row[4] in snff:
    snff[row[4]]+=1
  else:
    snff[row[4]]=1

  if row[7] in pc:
    pc[row[7]]+=1
  else:
    pc[row[7]]=1
  
  if row[8] in tt:
    tt[row[8]] +=1
  else:
    tt[row[8]] =1
  n+=1

print(len(med), len(hack_l), len(vid), len(rc), len(snff), len(pc),len(tt))


# In[88]:


import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
f = open('trip_data_6.csv', 'r')
reader = csv.reader(f)

td_9 = dict()
plong_10 = dict()
plat_11 = dict()
dlong_12 = dict()
dlat_13 = dict()
for row in reader:
  if row[9] in td_9:
    td_9[row[9]]+=1
  else:
    td_9[row[9]]=1 

  if row[10] in plong_10:
    plong_10[row[10]]+=1
  else:
    plong_10[row[10]]=1 

  if row[11] in plat_11:
    plat_11[row[11]]+=1
  else:
    plat_11[row[11]]=1

  if row[12] in dlong_12:
    dlong_12[row[12]]+=1
  else:
    dlong_12[row[12]]=1

  if row[13] in dlat_13:
    dlat_13[row[13]]+=1
  else:
    dlat_13[row[13]]=1

print(len(td_9),len(plong_10),len(plat_11),len(dlong_12),len(dlat_13))


# In[89]:


print(rc)


# ### Part 8

# In[110]:


import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
f = open('trip_data_6.csv', 'r')
reader = csv.reader(f)


# In[112]:


min_rc = 0
max_rc = 0
min_pc= 0
max_pc = 0
min_tis = 0
max_tis= 0
min_td = 0
max_td = 0
n=0
for row in reader:
  #print(row[3])
  n+=1
  try:
    if int(row[3]) <= min_rc or min_rc ==0:
      min_rc = int(row[3])
    if int(row[3]) >= max_rc or max_rc ==0:
      max_rc = int(row[3])
  except Exception as e:
    print(e)
  try:
    if int(row[7]) <= min_pc or min_pc ==0:
      min_pc = int(row[7])
    if int(row[7]) >= max_pc or max_pc ==0:
      max_pc = int(row[7])
  except Exception as e:
    print(e)
  try:
    if int(row[8]) <= min_tis or min_tis ==0:
      min_tis = int(row[8])
    if int(row[8]) >= max_tis or max_tis ==0:
      max_tis = int(row[8])
  except Exception as e:
    print(e)
  try:
    if float(row[9]) <= min_td or min_td ==0:
      min_td = float(row[9])
    if float(row[9]) >= max_tis or max_td ==0:
      max_td = float(row[9])
  except Exception as e:
    print(e)


print(n)



# In[114]:


print(max_rc, min_rc)
print(max_pc, min_pc)
print(max_tis, min_tis)
print(max_td, min_td)


# ### Part 9

# In[115]:


import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
f = open('trip_data_6.csv', 'r')
reader = csv.reader(f)


# In[118]:


import datetime,csv
fn = 'trip_data_6.csv'
import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))

#fn = 'trip_data_6.csv'

f = open(fn, 'r')
reader = csv.reader(f)
exp =0
n=0
pcl =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hc =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#f = open(fn, 'r')
#reader = csv.reader(f)
for row in reader:
  n+=1
  try:
    dts = row[5]
    dto = datetime.datetime.strptime(dts,"%Y-%m-%d %H:%M:%S")
  except Exception as e:
    exp+=1
    print(e)
  h = dto.hour  
  try:
    ipc = int(row[7])    
    hc[h]+=1
    pcl[h]+=ipc
  except Exception as e:
    print(e)

        #except Exception as e:
         # exp+=1
          #print(e)



# In[119]:


averages = []

for i in range(len(hc)):
  averages.append(pcl[i] / hc[i])


# In[120]:


from matplotlib import pyplot as plt
plt.style.use('seaborn')
import numpy as np
 
# Creating histogram
plt.figure(figsize=(20,6))
plt.xlabel('Hour of the day')
plt.ylabel('Average number of taxi passengers')
plt.title('Average number of taxi passengers for each hour of the day')
plt.bar(x=range(0,24), height=averages)
plt.show()


# ## Part 10) & Part 11)

# In[27]:


import csv
fn = 'trip_data_6.csv'
f = open(fn, 'r')
reader = csv.reader(f)
fnew = open('new.csv', 'w')
fnew.write('')
fnew.close()
fnew = open('new.csv', 'w')
writer = csv.writer(fnew,delimiter=',',lineterminator='\n')

n = 0
nn=0
for row in reader:
    if n % 1000 == 0:
        nn+=1
        writer.writerow(row)
    n+=1
print(n,nn)
fnew.close


# In[28]:


import csv
fnew = 'new.csv'
reader = open(fnew,'r')
n=0
for row in reader:
    n+=1
print(n)    


# In[30]:


import datetime,csv
#fn = 'trip_data_6.csv'
#import csv
#https://drive.google.com/file/d/13gclMmH86q8pwj0qUfTbAjl595B2rov6/view?usp=sharing
#from google.colab import drive
#drive.mount('/content/gdrive') 
#from google.colab import files
#uploaded = files.upload()
#import io
#reader = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))

#fn = 'new.csv'

f = open('new.csv', 'r')
reader = csv.reader(f)
exp =0
n=0
pcl =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hc =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#f = open(fn, 'r')
#reader = csv.reader(f)
for row in reader:
  n+=1
  try:
    dts = row[5]
    dto = datetime.datetime.strptime(dts,"%Y-%m-%d %H:%M:%S")
  except Exception as e:
    exp+=1
    print(e)
  h = dto.hour  
  try:
    ipc = int(row[7])    
    hc[h]+=1
    pcl[h]+=ipc
  except Exception as e:
    print(e)

        #except Exception as e:
         # exp+=1
          #print(e)



# In[31]:


averages = []

for i in range(len(hc)):
  averages.append(pcl[i] / hc[i])


# In[34]:


get_ipython().system('pip install matplotlib')
from matplotlib import pyplot as plt
plt.style.use('seaborn')
import numpy as np
 
# Creating histogram
plt.figure(figsize=(20,6))
plt.xlabel('Hour of the day')
plt.ylabel('Average number of taxi passengers')
plt.title('Average number of taxi passengers for each hour of the day')
plt.bar(x=range(0,24), height=averages)
plt.show()

