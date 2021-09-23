from variable import Variable
from functions import Square
import numpy as np

if __name__ == "__main__":
    x = Variable(np.array(10))
    f = Square()
    y = f(x)

    print(type(y))
    print(y.data)
