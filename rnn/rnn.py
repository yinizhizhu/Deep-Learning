import torch
import torch.nn as nn
from torch.autograd import Variable


class RNN(nn.Module):
    def __init__(self, h_size):
        super(RNN, self).__init__()

        self.hidden_size = h_size
        self.t_size = 530

        self.i2h = nn.Linear(self.t_size, self.hidden_size)
        # self.i2o = nn.Linear(self.input_size + self.hidden_size, self.output_size)
        self.tanh = nn.Tanh()

    def forward(self, ret, ref):
        a0 = Variable(torch.zeros(1, self.hidden_size))
        x0 = torch.cat((a0, ret), 1)

        a1 = self.tanh(self.i2h(x0))
        x1 = torch.cat((a1, ref), 1)

        c = self.tanh(self.i2h(x1))
        return c


class classifier(nn.Module):
    def __init__(self, h_size):
        super(classifier, self).__init__()

        self.hidden_size = h_size*2
        self.leftRNN = RNN(h_size)
        self.rightRNN = RNN(h_size)
        self.i2o = nn.Linear(self.hidden_size, 3)

    def forward(self, ret1, ret2, ref):
        c_left = self.leftRNN(ret1, ref)
        print c_left
        c_right = self.rightRNN(ret2, ref)
        print c_right
        c = torch.cat((c_left, c_right), 1)
        o = self.i2o(c)
        return o

model = classifier(18)

ret1 = Variable(torch.zeros((1,512)))
ret2 = Variable(torch.zeros((1,512)))
ref = Variable(torch.zeros((1,512)))

o = model(ret1, ret2, ref)
print o