import os
from sklearn.model_selection import train_test_split
import shutil

X = y= os.listdir('Data/0')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#print(X_train)
os.mkdir('Data/0/train/')
for x in X_train:
    shutil.move('./Data/0/'+x , './Data/0/train/'+x)
os.mkdir('Data/0/test/')
for x in X_test:
    shutil.move('./Data/0/'+x , './Data/0/test/'+x)

X = y= os.listdir('Data/1')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#print(X_train)
os.mkdir('Data/1/train/')
for x in X_train:
    shutil.move('./Data/1/'+x , './Data/1/train/'+x)
os.mkdir('Data/1/test/')
for x in X_test:
    shutil.move('./Data/1/'+x , './Data/1/test/'+x)
