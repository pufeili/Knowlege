


function [PredFinal] = bayesFusion(all_Pred,all_ConfuMatrix)
% BAYESFUSION 此处显示有关此函数的摘要
% all_Pred为每种方法预测的标签，all_ConfuMatrix为每种方法的混淆矩阵;
% PredFinal	为最终融合后的标签;

N_class = length(all_ConfuMatrix(:,1));   %类别数
N_classifiers = length(all_ConfuMatrix(1,:))/length(all_ConfuMatrix(:,1));   %分类器的数量
N_test = length(all_Pred(:,1));     %测试样本的数量

all_LM =all_ConfuMatrix ./ repmat(sum(all_ConfuMatrix,1),N_class,1);  %得到各类的准确率
index=repmat(0:N_class:(N_classifiers-1)*N_class,N_test,1);
index=index'+all_Pred';
D=all_LM (:,index);                        %提取三种方法每一类的预测准确率
mu_elements=reshape(D,N_class,N_classifiers,N_test);
mu=prod(mu_elements,2);
[~, Ensemble_decision]=max(mu);
Ensemble_decision=reshape(Ensemble_decision,1,N_test);

PredFinal=Ensemble_decision';




end

