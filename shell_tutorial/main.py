import torch
import torch.nn as nn
from torch.autograd import Variable
#from torchsummary import summary


import argparse
import os

parser = argparse.ArgumentParser(description="One Shot Visual Recognition")

parser.add_argument("-lr", "--learning_rate", type=float, default=0.001)
parser.add_argument("-e", "--max_epoch", type=int, default=25)
parser.add_argument("-b", "--batch_size", type=int, default=8)
parser.add_argument("-m", "--mode", type=str, default="weights_add",help="select fusion mode") #concat/add/weights_add
'''=========================='''
parser.add_argument("-fm", "--fusion_mode", type=int, default=4) #1/2/3/4
'''=========================='''
parser.add_argument("-s", "--sample_num_per_class", type=int, default=1)
parser.add_argument("-t", "--test_episode", type=int, default=1000)
parser.add_argument("-u", "--hidden_unit", type=int, default=10)
args = parser.parse_args()


# Hyper Parameters
MAX_EPOCH = args.max_epoch
LEARNING_RATE = args.learning_rate
BATCH_SIZE = args.batch_size
MODE = args.mode
FUSION_MODE = args.fusion_mode

#print(MAX_EPOCH)

print("epoch: %d ,learning rate: %.4f, mode: %s, fusion_mode: %s" % (MAX_EPOCH,LEARNING_RATE,MODE,FUSION_MODE))


