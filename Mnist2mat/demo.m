clear ;
clc;
% 训练与测试文件名
TrainImagesName='train-images-idx3-ubyte';
TrainLabelsName='train-labels-idx1-ubyte';
TestImagesName='t10k-images-idx3-ubyte';
TestLabelsName='t10k-labels-idx1-ubyte';
%读取训练图片数据文件
PathName = uigetdir('','选择数据集路径：');
TrainImagesFile = fullfile(PathName, TrainImagesName);
TrainLabelsFile = fullfile(PathName, TrainLabelsName);
TestImagesFile = fullfile(PathName, TestImagesName);
TestLabelsFile = fullfile(PathName, TestLabelsName);
%% 处理训练图片
fid = fopen(TrainImagesFile,'r'); 
a = fread(fid,16,'uint8'); 
%MagicNum = ((a(1)*256+a(2))*256+a(3))*256+a(4);
ImageNum = ((a(5)*256+a(6))*256+a(7))*256+a(8);
ImageRow = ((a(9)*256+a(10))*256+a(11))*256+a(12);
ImageCol = ((a(13)*256+a(14))*256+a(15))*256+a(16);
trainImages=zeros(ImageRow,ImageCol,ImageNum,'uint8');
for i=1:ImageNum
    b = fread(fid,ImageRow*ImageCol,'uint8');   
    c = reshape(b,[ImageRow ImageCol]); 
    trainImages(:,:,i)=uint8(c');
    disp(['正在处理训练图片，处理进度 (' , num2str(i) , '/' , num2str(ImageNum) ,')']);
end
fclose(fid);
%% 处理测试图片
fid = fopen(TestImagesFile,'r'); 
a = fread(fid,16,'uint8'); 
%MagicNum = ((a(1)*256+a(2))*256+a(3))*256+a(4);
ImageNum = ((a(5)*256+a(6))*256+a(7))*256+a(8);
ImageRow = ((a(9)*256+a(10))*256+a(11))*256+a(12);
ImageCol = ((a(13)*256+a(14))*256+a(15))*256+a(16);
testImages=zeros(ImageRow,ImageCol,ImageNum,'uint8');
for i=1:ImageNum
    b = fread(fid,ImageRow*ImageCol,'uint8');   
    c = reshape(b,[ImageRow ImageCol]); 
    testImages(:,:,i)=uint8(c');
    disp(['正在处理测试图片，处理进度 (' , num2str(i) , '/' , num2str(ImageNum) ,')']);
end
fclose(fid);
%% 处理训练标签
fid = fopen(TrainLabelsFile,'r'); 
a = fread(fid,8,'uint8'); 
%MagicNum = ((a(1)*256+a(2))*256+a(3))*256+a(4);
ImageNum = ((a(5)*256+a(6))*256+a(7))*256+a(8);
%trainLabels=zeros(ImageNum,1);
b = fread(fid,ImageNum,'uint8');   
trainLabels=uint8(b);
disp('训练标签处理完成');
fclose(fid);
%% 处理测试标签
fid = fopen(TestLabelsFile,'r'); 
a = fread(fid,8,'uint8'); 
%MagicNum = ((a(1)*256+a(2))*256+a(3))*256+a(4);
ImageNum = ((a(5)*256+a(6))*256+a(7))*256+a(8);
%testLabels=zeros(ImageNum,1);
b = fread(fid,ImageNum,'uint8');
testLabels=uint8(b);
disp('测试标签处理完成' );
fclose(fid);
% 保存提取的数据
save('mnist.mat','trainImages','trainLabels','testImages','testLabels')