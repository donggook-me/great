from data_load import *
from msg_detector import *


if __name__ == '__main__':
    X, y = get_data("../input/msg.nl", "../input/input.csv")
    MNB = msgDetector()
    MNB.fit(X[500:], y[500:])
    pred = MNB.predict(X[:500])
    true = y[:500]
    print("pred: ", pred)
    print()
    print("true: ",true)
    accuracy = sum(1 for i in range(len(pred)) if pred[i] == true[i]) / float(len(pred))
    print("\n{0:.4f}".format(accuracy))