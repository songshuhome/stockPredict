# coding=utf-8

from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option('expand_frame_repr',False)

# 导入股票数据，进行预处理
def getStock():
    df=pd.read_csv('stock_data.csv')
    x=df.ix[:,df.columns!='Close Price']
    y=df.ix[:,df.columns=='Close Price']
    x=x.drop('Date',axis=1)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
    return x_train,x_test,y_train,y_test

# 进行训练数据
def train(x_train,y_train):
    regr=linear_model.LinearRegression()
    regr.fit(x_train,y_train)
    return  regr;

if __name__=='__main__':
    x_train,x_test,y_train,y_test=getStock()
    regr=train(x_train.values,y_train.values)
    predict=regr.predict(x_test.values)
    plt.plot(x_test,predict,color='red',linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()

    test=np.array([[45,43,44,30302400]])
    print(regr.predict(test))

    # 正确率
    accuracy=((y_test==predict).sum().values[0]/y_test.shape[0])
    # 加入容错率5%
    accuracyError=(((abs(predict-y_test)/y_test)<=0.05).sum().values[0])/y_test.shape[0]
    print(accuracy)
    print(accuracyError)