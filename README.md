# stockPredict
股票预测器（微软股票）
===============
使用微软股票每日最高价（High Price），最低价（Low Price），开盘价（Open Price），收盘价（Close Price）和交易量（Volume）预测当天的收盘价<br>
该问题为回归问题，使用线性回归预测。<br>
经过计算预测准确率=（预测正确样本数）/（总测试样本数）* 100%为0，不理想<br>
加入容错率ErrorTolerance（一般是10%或者5%），达到100%。
