
% MNIST数据库读取
 clc;clear;close all;
%读取MNIST数据集中的图片
train_images = readMNISTImages('train-images-idx3-ubyte'); %60000个训练集,大小为28*28*60000
test_images =  readMNISTImages('t10k-images-idx3-ubyte');  %10000个训练集,大小为28*28*10000
 
%读取MNIST数据集中的标签
train_labels1 = readMNISTLabels('train-labels-idx1-ubyte');%标签0~9；60000个标签，大小为60000*1
test_labels1 = readMNISTLabels('t10k-labels-idx1-ubyte'); %10000个标签，大小为10000*1