

import os
import numpy as np
import torch
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from torch.utils.data import Dataset,DataLoader
import torch.nn as nn
import torchvision.transforms as transform
import torchvision.datasets as dsets
class plot_error_surfaces(object):

    # Construstor
    def __init__(self, w_range, b_range, X, Y, n_samples=30, go=True):
        W = np.linspace(-w_range, w_range, n_samples)
        B = np.linspace(-b_range, b_range, n_samples)
        w, b = np.meshgrid(W, B)
        Z = np.zeros((30, 30))
        print(W,end='next')
        print(B,end='next')
        print(w,end='next')
        print(Z,end='next')
        count1 = 0
        self.y = Y.numpy()
        self.x = X.numpy()
        for w1, b1 in zip(w, b):
            count2 = 0
            for w2, b2 in zip(w1, b1):
                yhat = 1 / (1 + np.exp(-1 * (w2 * self.x + b2)))
                Z[count1, count2] = -1 * np.mean(
                    self.y * np.log(yhat + 1e-16) + (1 - self.y) * np.log(1 - yhat + 1e-16))
                count2 += 1
            count1 += 1
        self.Z = Z
        self.w = w
        self.b = b
        self.W = []
        self.B = []
        self.LOSS = []
        self.n = 0
        if go == True:
            plt.figure()
            plt.figure(figsize=(7.5, 5))
            plt.axes(projection='3d').plot_surface(self.w, self.b, self.Z, rstride=1, cstride=1, cmap='viridis',
                                                   edgecolor='none')
            plt.title('Loss Surface')
            plt.xlabel('w')
            plt.ylabel('b')
            plt.show()
            plt.figure()
            plt.title('Loss Surface Contour')
            plt.xlabel('w')
            plt.ylabel('b')
            plt.contour(self.w, self.b, self.Z)
            plt.show()

        def set_para_loss(self, model, loss):
            self.n = self.n + 1
            self.W.append(list(model.parameters())[0].item())
            self.B.append(list(model.parameters())[1].item())
            self.LOSS.append(loss)

        # Plot diagram
        def final_plot(self):
            ax = plt.axes(projection='3d')
            ax.plot_wireframe(self.w, self.b, self.Z)
            ax.scatter(self.W, self.B, self.LOSS, c='r', marker='x', s=200, alpha=1)
            plt.figure()
            plt.contour(self.w, self.b, self.Z)
            plt.scatter(self.W, self.B, c='r', marker='x')
            plt.xlabel('w')
            plt.ylabel('b')
            plt.show()

        # Plot diagram
        def plot_ps(self):
            plt.subplot(121)
            plt.ylim
            plt.plot(self.x[self.y == 0], self.y[self.y == 0], 'ro', label="training points")
            plt.plot(self.x[self.y == 1], self.y[self.y == 1] - 1, 'o', label="training points")
            plt.plot(self.x, self.W[-1] * self.x + self.B[-1], label="estimated line")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.ylim((-0.1, 2))
            plt.title('Data Space Iteration: ' + str(self.n))
            plt.show()
            plt.subplot(122)
            plt.contour(self.w, self.b, self.Z)
            plt.scatter(self.W, self.B, c='r', marker='x')
            plt.title('Loss Surface Contour Iteration' + str(self.n))
            plt.xlabel('w')
            plt.ylabel('b')

    # Plot the diagram

    def PlotStuff(X, Y, model, epoch, leg=True):

        plt.plot(X.numpy(), model(X).detach().numpy(), label=('epoch ' + str(epoch)))
        plt.plot(X.numpy(), Y.numpy(), 'r')
        if leg == True:
            plt.legend()
        else:
            pass




class Data(Dataset):

    # Constructor
    def __init__(self):
        # Create X values from -1 to 1 with step .1
        self.x = torch.arange(-1, 1, 0.1).view(-1, 1)

        # Create Y values all set to 0
        self.y = torch.zeros(self.x.shape[0], 1)

        # Set the X values above 0.2 to 1
        self.y[self.x[:, 0] > 0.2] = 1
        # Set the .len attribute because we need to override the __len__ method
        self.len = self.x.shape[0]

    # Getter that returns the data at the given index
    def __getitem__(self, index):
        return self.x[index], self.y[index]

    # Get length of the dataset
    def __len__(self):
        return self.len


class logistic_regression(nn.Module):

    # Constructor
    def __init__(self, n_inputs):
        super(logistic_regression, self).__init__()
        # Single layer of Logistic Regression with number of inputs being n_inputs and there being 1 output
        self.linear = nn.Linear(n_inputs, 1)

    # Prediction
    def forward(self, x):
        # Using the input x value puts it through the single layer defined above then puts the output through the sigmoid function and returns the result
        yhat = torch.sigmoid(self.linear(x))
        return yhat




data_set = Data()
model = logistic_regression(1)
x,y= data_set[0]
print((x,y))
sigma = model(x)
print(sigma)
set_surface = plot_error_surfaces(15,13,data_set[:][0],data_set[:][1])
crition = nn.BCELoss()
loss = crition(sigma,y)
print(loss)

trainLoader = DataLoader(dataset=data_set,batch_size=10)
dataset_iter = iter(trainLoader)
x,y = next(dataset_iter)
print(x)




