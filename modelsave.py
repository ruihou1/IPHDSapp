#把标准化过程打包
import pandas as pd
import numpy as np
from pandas import read_csv
from sas7bdat import SAS7BDAT
feature=SAS7BDAT(r'E:/DIAPRE/文章最终结果数据/allbasenew.sas7bdat',encoding="gb2312").to_data_frame()#导入sas数据集#导入有中文时需要加encoding="gbk"
#数据标准化
from sklearn.preprocessing import StandardScaler
import numpy as np
#应该先用70%训练集，30%内部验证集训练方法
#先划分两个数据集训练集和测试集
X=feature[feature["year"]==2011]
X1=feature[feature["year"]==2012]
Xtrain=X[[ 'Glu0',"HbA1c","bmi","age" ,"hr","ALT","TG","LDL","sbp","HDL"]]
ss=StandardScaler()#构建estimator
ss.fit(Xtrain)
print(ss.mean_)
XX1 = ss.transform(Xtrain)
XX1 = pd.DataFrame(Xtrain, columns=Xtrain.columns)
import joblib
joblib.dump(ss, 'E:/DIAPRE/文章最终结果数据/scalarsave')
#需要指明axis=1才是删除列，不然默认删除为行
yy1=X["glu"]
#把预测模型打包
# keras for nn building
from keras.models import Sequential, load_model

# a dense network
from keras.layers import Dense, Dropout

# import the numpy library
import numpy as np

# to plot error
import matplotlib.pyplot as plt

# pandas for data analysis
import pandas as pd

# confusion matrix from scikit learn
from sklearn.metrics import confusion_matrix

# for visualisation
import seaborn as sns

# for roc-curve
from sklearn.metrics import roc_curve

import seaborn as sns
sns.set()
# building the nn
dnn = Sequential()


# Add the first hidden layer两个隐含层
dnn.add(Dense(200, activation='sigmoid', input_dim=XX1.shape[1]))

# Add the second hidden layer
dnn.add(Dense(200, activation='sigmoid'))

#Add the third hidden layer
#dnn.add(Dense(100, activation='sigmoid'))

#Add the four hidden layer
#model.add(Dense(100, activation='sigmoid'))

# Add the output layer
dnn.add(Dense(1, activation='sigmoid'))

# Compile the model
dnn.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
#fit
history = dnn.fit(XX1, yy1, epochs=20)#学习次数'
dnn.save('E:/DIAPRE/文章最终结果数据/model.h6')
model = load_model('E:/DIAPRE/文章最终结果数据/model.h5')