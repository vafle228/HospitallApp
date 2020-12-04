import torch

class DataSet:
    def __init__(self):
        self.X_data = []
        self.y_data = []

    def add(self, gender, age, why, specialist, answer):
        self.X_data.append([gender, age, why, specialist])
        self.y_data.append(answer)

    def add(self, datas, answers):
        self.X_data.append(datas)
        self.y_data.append(answers)

    def dataSet(self):
        return torch.Tensor(self.X_data), torch.Tensor(self.y_data)

    def remove(self):
        self.X_data = []
        self.y_data = []
