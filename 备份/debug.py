
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


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





f = open("log.txt",'w')

for a in range(4):
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
            
    
test.to_csv("test2.csv")




