# DataMining_Project2
###### tags: `DataMining`    主題: `透過看劇類型及可負擔之價錢分析適合的影音平台`


### 目標
---
* 給予對各類型的滿意指數及可負擔之價錢，判斷最適合的影音平台

### 各串流平台分析時利用的參考參數
---

```cpp=
'''
# 定義影音串流平台

# 1. Disney+:
#       * 對美劇感到滿意的程度
#       * 一年可負擔 697.5 (四部裝置2790)
# 2. Netflix:
#       * 對韓劇感到滿意的程度
#       * 一年可負擔 1170 (四部裝置4680)
# 3. KKTV:
#       * 對日劇感到滿意的程度
#       * 一年可負擔 833.25 (四部裝置3333)
# 4. iQiyi:
#       * 對陸劇感到滿意的程度
#       * 一年可負擔 1896 (二部裝置3792)

'''
```

### Training & Accuracy
---

* 訓練資料及測試資料以dataset 7:3 之方式區分
  * 資料100筆時，將前70筆作為訓練特徵，後30筆作為測試特徵
  * 資料5000筆時，將前3800筆作為訓練特徵，後1200筆作為測試特徵
  * 資料50000筆時，將前38000筆作為訓練特徵，後12000筆作為測試特徵

* generated data = 100
<img width="400" height="90" src="https://i.imgur.com/UT3TXNa.png"/>
* generated data = 5000
<img width="400" height="90" src="https://i.imgur.com/GXIV89d.png"/>
* generated data = 500000
<img width="400" height="90" src="https://i.imgur.com/2l2so0F.png"/>

### Output Graph
---

* generated data = 100
![](https://i.imgur.com/zUxukIW.png)
* generated data = 5000
![](https://i.imgur.com/fSmNAE7.jpg)
* generated data = 50000
![](https://i.imgur.com/sOkBOAH.png)
