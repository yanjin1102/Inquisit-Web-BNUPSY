clc;clear;
P = 'D:\YING\ʵ��ʵ��\����\black4.jpg';
a = imread(P);
b=rgb2gray(a); %��ʾ���ٱ���ͼƬ����С�����仯
imwrite(b,'D:\YING\ʵ��ʵ��\����\black.jpg');%���Ϊri.jpg
