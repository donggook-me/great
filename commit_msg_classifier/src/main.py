from data_load import *
from msg_detector import *
from pathlib import Path
from random import shuffle

if __name__ == '__main__':
    # Repository root path
    root_path = str(Path(__file__).parent.parent.resolve())
    
    # Load dataset & shuffle it
    data = get_data(root_path + "/input/msg.nl", root_path + "/input/input.csv")
    shuffle(data)
    
    X = [d[0] for d in data]
    y = [d[1] for d in data]
    
    # Variables
    train_size = len(X) * 7 // 10 
    test_size = len(X) - train_size
    
    # Fitting
    MNB = msgDetector()
    MNB.fit(X[:train_size], y[:train_size])
    
    # Result
    pred = MNB.predict(X[train_size:])
    expected = y[train_size:]
    
    # Console log
    print(f'train data size: {train_size}\ntest data size: {test_size}')
    # for y_hat, y in zip(pred, expected):
    #     print(f'predict y: {y_hat}, expected y: {y}')
    accuracy = sum(1 for i in range(len(pred)) if pred[i] == expected[i]) / float(len(pred))
    print("Accuracy: {0:.4f}".format(accuracy))