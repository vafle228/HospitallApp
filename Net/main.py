import torch
import numpy as np
import os


class TimeNet(torch.nn.Module):
    def __init__(self):
        super(TimeNet, self).__init__()
        self.fc1 = torch.nn.Linear(4, 4)
        self.ac1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(4, 7)
        self.ac2 = torch.nn.ReLU()
        self.fc3 = torch.nn.Linear(7, 1)

    def forward(self, x):
        x = self.ac1(self.fc1(x))
        x = self.ac2(self.fc2(x))
        x = self.fc3(x)
        return x


def loss(pred, target):
    squares = (pred - target) ** 2
    return squares.mean()


async def train(model, x_train, y_train):
    optimizer = torch.optim.Adam(time_net.parameters(), lr=1.0e-3)
    batch_size = 4
    for epoh in range(2000):
        order = np.random.permutation(len(x_train))
        for start_index in range(0, len(x_train), batch_size):
            optimizer.zero_grad()

            batch_index = order[start_index:start_index+batch_size]
            X_batch = x_train[batch_index]
            Y_batch = y_train[batch_index]

            preds = model.forward(X_batch)
            loss_val = loss(preds, Y_batch)
            loss_val.backward()

            optimizer.step()

        if epoh % 100 == 0:
            print(f'Epoch {epoh} end!')
    return model


async def save_model(model, PATH):
    torch.save(model.state_dict(), PATH)


async def load_model(PATH):
    model = TimeNet(3)
    model.load_state_dict(torch.load(PATH))
    model.eval()
    return model
