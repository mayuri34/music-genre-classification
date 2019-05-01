import numpy as np

def loadall(filename=''):
    tmp = np.load(filename)
    x_train = tmp['x_train']
    y_train = tmp['y_train']
    x_test = tmp['x_test']
    y_test = tmp['y_test']
    x_cv = tmp['x_cv']
    y_cv = tmp['y_cv']
    return {'x_train' : x_train, 'y_train' : y_train,
            'x_test' : x_test, 'y_test' : y_test,
            'x_cv' : x_cv, 'y_cv' : y_cv, }