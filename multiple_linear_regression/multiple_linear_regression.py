import random
import pandas as pd
import matplotlib.pyplot as plt
from rich import print
from sklearn import linear_model
from sklearn.model_selection import train_test_split


def generate_data(n=10000):
    """generate random data"""
    header = ['a', 'b', 'c', 'd', 'e', 'out']
    data = [[random.randrange(11) for x in range(6)] for y in range(n)]
    df = pd.DataFrame(data)
    df.columns = header
    df['out'] = df['a'] * df['b'] + df['c'] - df['d'] * df['e']
    return df
    
    
def simple_without_split():
    """simple multiple linear regression without splitting data"""
    # ******* generate & prepare data *******
    df = generate_data(10000)
    input_columns = ['a', 'b', 'c', 'd', 'e']
    X = df[input_columns]
    Y = df['out']
    
    # ******* create model *******
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    
    # ******* make prediction *******
    df['predict'] = regr.predict(df[input_columns])
    print(df.head(20))
    
    # ******* show diff between out & predict *******
    df = df.head(100)  # to be more clear
    df[['out', 'predict']].plot.line()
    plt.tight_layout()
    plt.show()
    return None
    
    
if __name__ == "__main__":
    # ******* generate & prepare data *******
    df = generate_data(10000)
    input_columns = ['a', 'b', 'c', 'd', 'e']
    X = df[input_columns]
    Y = df['out']
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1)
    
    # ******* create model *******
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    
    # ******* make prediction *******
    predicts = x_test
    predicts['out'] = y_test
    predicts['predict'] = regr.predict(predicts[input_columns])
    predicts.reset_index(drop=True, inplace=True)
    print(predicts.head(20))
    
    # ******* show diff between out & predict *******
    predicts = predicts.head(100)  # to be more clear
    predicts[['out', 'predict']].plot.line()
    plt.tight_layout()
    plt.show()
    
    
"""
useful:
    https://datatofish.com/multiple-linear-regression-python/
    https://www.analyticsvidhya.com/blog/2021/05/multiple-linear-regression-using-python-and-scikit-learn/
    https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9
    
"""
