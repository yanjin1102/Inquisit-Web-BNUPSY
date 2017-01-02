clc;clear;
P = 'D:\YING\实心实验\内隐\black4.jpg';
a = imread(P);
b=rgb2gray(a); %显示后再保存图片，大小发生变化
imwrite(b,'D:\YING\实心实验\内隐\black.jpg');%输出为ri.jpg
