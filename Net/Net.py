import numpy as np
import torch


class TimeNet(torch.nn.Module):
    def __init__(self):
        super(TimeNet, self).__init__()
        self.fc1 = torch.nn.Linear(4, 4)
        self.ac1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(4, 3)
        self.ac2 = torch.nn.ReLU()
        self.fc3 = torch.nn.Linear(3, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.ac1(x)
        x = self.fc2(x)
        x = self.ac2(x)
        x = self.fc3(x)
        return x


def loss(pred, target):
    squares = (pred - target) ** 2
    return squares.mean()


def train(model, X_train, y_train, batch_size, epoch=2000):
    optimizer = torch.optim.Adam(model.parameters(), lr=1.0e-3)
    batch_size = batch_size
    for epoch in range(epoch):
        order = np.random.permutation(len(X_train))
        for start_index in range(0, len(X_train), batch_size):
            optimizer.zero_grad()

            batch_index = order[start_index:start_index + batch_size]

            X_batch = X_train[batch_index]
            y_batch = y_train[batch_index]

            preds = model.forward(X_batch)
            loss_val = loss(preds, y_batch)
            loss_val.backward()
            optimizer.step()
    return model


def saveModel(model, PATH):
    torch.save(model.state_dict(), PATH)


def loadModel(PATH):
    model = TimeNet()
    model.load_state_dict(torch.load(PATH))
    model.eval()
    return model
