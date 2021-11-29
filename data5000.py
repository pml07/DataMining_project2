from datetime import time
import random
import numpy as np
import pandas as pd

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

# Number of data M
M = 5000

# k features
k = ['enjoyAmerican', 'enjoyKorean', 'enjoyJapan', 'enjoyChinese', 'money']

# enjoy [美, 韓, 日, 陸]
enjoyAmerican = [random.uniform(0,1) for i in range(M)]
enjoyKorean = [random.uniform(0,1) for i in range(M)]
enjoyJapan = [random.uniform(0,1) for i in range(M)]
enjoyChinese = [random.uniform(0,1) for i in range(M)]
print(enjoyAmerican)
print(enjoyKorean)
print(enjoyJapan)
print(enjoyChinese)

#money
money = [random.randint(700,2000) for i in range(M)]
print(money)


# platform
platform = []
for i in range(M):
    if (max(enjoyAmerican[i], enjoyKorean[i], enjoyJapan[i], enjoyChinese[i]) == enjoyAmerican[i]):
        if (money[i] >= 697.5):
            platform.append('Disney+')
    elif (max(enjoyAmerican[i], enjoyKorean[i], enjoyJapan[i], enjoyChinese[i]) == enjoyKorean[i]):
        if (money[i] >= 1170):
            platform.append('Netflix')
        elif (money[i] >= 833.25):
            platform.append('KKTV')
        else:
            platform.append('Disney+')
    elif (max(enjoyAmerican[i], enjoyKorean[i], enjoyJapan[i], enjoyChinese[i]) == enjoyJapan[i]):
        if (money[i] >= 833.25):
            platform.append('KKTV')
        else:
            platform.append('Disney+')
    elif (max(enjoyAmerican[i], enjoyKorean[i], enjoyJapan[i], enjoyChinese[i]) == enjoyChinese[i]):
        if (money[i] >= 1896):
            platform.append('iQiyi')
        elif (money[i] >= 1170):
            platform.append('Netflix')
        elif (money[i] >= 833.25):
            platform.append('KKTV')
        else:
            platform.append('Disney+')
    else:
        platform.append('Disney+')

print(platform)

data = pd.DataFrame({'enjoyAmerican': enjoyAmerican, 'enjoyKorean': enjoyKorean, 'enjoyJapan': enjoyJapan, 'enjoyChinese': enjoyChinese, 'money': money, 'platform': platform})
data.to_csv('data/data5000.csv', index=False)