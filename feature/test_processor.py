from processor import OutliersFilter
from processor import ReduceVIF


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from itertools import combinations
from sklearn.grid_search import GridSearchCV

for num in [10, 50, 100, 1000]:
    x = np.random.normal(0, 0.5, num-3)
    x = np.r_[x, -3, -10, 12]

df=pd.DataFrame(x,columns=["test"])

ot = OutliersFilter("test",method="percentile",threshold=95)
ot.fit(df)
o = ot.transform(df)

ot = OutliersFilter("test",method="mad",threshold=3.5)
ot.fit(df)
o = ot.transform(df)




pg = {'clf__C': [0.1, 1, 10, 100]}

grid = GridSearchCV(pipeline, param_grid=pg, cv=5)
grid.fit(data_train, y_train)

grid.best_params_
# {'clf__C': 0.1}

grid.best_score_
# 0.702290076336



# ReduceVIF test
X = pd.read_csv('../input/train.csv', index_col=0, parse_dates=['timestamp'])
y = X.pop('price_doc')
X.head()


transformer = ReduceVIF()

# Only use 10 columns for speed in this example
X = transformer.fit_transform(X[X.columns[-10:]], y)

X.head()