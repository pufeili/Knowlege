
clc;
clear;

load('pca_pred.mat');
load('lda_pred.mat');
load('lpp_pred.mat');

load('pca_cm.mat');
load('lda_cm.mat');
load('lpp_cm.mat');
%pred是预测的标签；cm是混淆矩阵

allpred =[pca_pre lda_pre lpp_pre];
allcm = [CM_pca CM_lda CM_lpp ];

[bayesPred] = bayesFusion(allpred,allcm);%贝叶斯融合





