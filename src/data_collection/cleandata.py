import resnet50
import os
import shutil

pathlist = os.listdir('data_grab')
count = 0
for i in pathlist:
    pathlist[count] = os.path.join('data_grab', pathlist[count])
    count+=1
predictions = resnet50.predict(pathlist)

count = 0
for i in predictions:
    flag = 0
    if i!=None:
        for top in range(3):
            name = i[top][1]
            if name=='toilet_seat':
                flag = 1
    if flag==1:
        shutil.copyfile(pathlist[count], 'cleandata//'+pathlist[count][-9:])
    else:
        shutil.copyfile(pathlist[count], 'dirtydata//'+pathlist[count][-9:])
    count+=1

