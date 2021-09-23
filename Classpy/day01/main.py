from variable import Variable
import numpy as np

if __name__ == "__main__":
    data = np.array(1.0)
    x = Variable(data)
    print(x.data)
    x.data = np.array(5.0)
    print(x.data)
