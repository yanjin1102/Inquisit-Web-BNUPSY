    clc;clear;
for n = 1:15
path1 =  'E:\常用\文件\大二上\心理\Inquisit\homework1125\n';
format = '.jpg';
seq = num2str(n);
pathname1 = sprintf('%s%s%s',path1,seq,format);
MyPic = imread(pathname1); 
[rows , cols , colors] = size(MyPic); 
MidGrayPic = zeros(rows , cols);
MidGrayPic = uint8(MidGrayPic);
for i = 1:rows  
    for j = 1:cols  
        sum = 0;  
        for k = 1:colors  
            sum = sum + MyPic(i , j , k) / 3;
        end  
        MidGrayPic(i , j) = sum;  
    end  
end 
path2 =  'E:\常用\文件\大二上\心理\Inquisit\homework1125\a';
seq = num2str(n);
pathname2 = sprintf('%s%s%s',path2,seq,format);
imwrite(MidGrayPic , pathname2 , 'jpg');
for i = 1:rows  
    for j = 1:cols  
        sum = 0;  
        for k = 1:colors  
            sum = sum + MyPic(i , j , k) / 10;
        end  
        MidGrayPic(i , j) = sum;  
    end  
end 
path3 =  'E:\常用\文件\大二上\心理\Inquisit\homework1125\s';
format = '.jpg';
seq = num2str(n);
pathname3 = sprintf('%s%s%s',path3,seq,format);
imwrite(MidGrayPic , pathname3 , 'jpg');
end