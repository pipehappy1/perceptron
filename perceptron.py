import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt


def perceptron_example():
    data = np.random.random((10, 2))
    data[:5, :] = data[:5, :] + 1

    plt.plot(data[:,0], data[:,1], '.')
    plt.show()

    w = [0, 0.1, 0.1]

    result = (w[0] + w[1]*data[:, 0] + w[2]*data[:,1]) > 0
    print(result)

    for i in range(3):
        for j in range(10):
            r = w[0] + w[1]*data[j, 0] + w[2]*data[j, 1]

            if j < 5:
                if r >= 0:
                    continue
                else:
                    w[0] += 0.01
                    for k in range(2):
                        if data[j, k] >= 0:
                            w[k+1] += 0.01
                        else:
                            w[k+1] -= 0.01
            else:
                if r < 0:
                    continue
                else:
                    w[0] -= 0.01
                    for k in range(2):
                        if data[j, k] >= 0:
                            w[k+1] -= 0.01
                        else:
                            w[k+1] += 0.01

    result = (w[0] + w[1]*data[:, 0] + w[2]*data[:,1]) > 0
    print(result)
                    

if __name__ == "__main__":
    perceptron_example()
