import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import threading
import time

def job(l, r, test, train_raw, attrs, f): #[l,r)
    for a in range(l, l + 2):
        for b in range(len(train_raw)):
            ok = 1
            for i in range(1, len(attrs)):
                attr = attrs[i]
                if pd.isnull(test[attr][a]):
                    continue
                if train_raw[attr][b] != test[attr][a]:
                    ok = 0
                    break
            if ok:
                test['Response'][a] = train_raw['Response'][b]
                print('testId: %d, train_rawId:%d' % (test['id'][a], train_raw['id'][b]), file=f)
                break



train_raw = pd.read_csv('train2.csv')
test = pd.read_csv('test.csv')
attrs = test.columns
attr_types = [type(test[attrs[i]][0]) for i in range(len(attrs)) ]
attr_types
attrs_raw = train_raw.columns
attr_raw_types = [type(train_raw[attrs_raw[i]][0]) for i in range(len(attrs_raw)) ]
attr_raw_types
attr4 = 'Driving_License'
tmp = train_raw[attr4]
train_raw[attr4] =  tmp.astype('float64')
test['Response'] = 0
num = [0, 6351, 12703, 19053, 25404, 31755, 38106, 44457, 50808, 57159, 63510, 69861, 76220]

f = open("log.txt", "w")
thread_list = []
for index in range(len(num) - 1):
    thread_list.append(threading.Thread(target=job(num[index], num[index + 1], test, train_raw, attrs, f)))
    thread_list[-1].start()
    # thread_list[-1].join()
    
test.to_csv("train2.csv")
print("Done.")
