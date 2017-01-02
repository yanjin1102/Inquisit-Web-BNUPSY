clear all;clc;
% Current Working Path 获得当前文件所在路径，先包含文件名，后去掉
CWPath = fileparts(mfilename('fullpath'));
cd(CWPath);
yuan = imread('0.jpg');%读取RGB格式的图像

step=0.2;%图片的差异值
number=4;%生成的图片数量

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%之前找到的RGB2gray
%MyFirstGrayPic = rgb2gray(MyYuanLaiPic);%用matlab已有的函数进行RGB到灰度图像的转换
%作者自己的方法
% [rows , cols , colors] = size(MyYuanLaiPic);%得到原来图像的矩阵的参数
% MidGrayPic = zeros(rows , cols);%用得到的参数创建一个全零的矩阵，这个矩阵用来存储用下面的方法产生的灰度图像
% MidGrayPic = uint8(MidGrayPic);%将创建的全零矩阵转化为uint8格式，因为用上面的语句创建之后图像是double型的
% 
% for i = 1:rows
%     for j = 1:cols
%         sum = 0;
%         for k = 1:colors
%             sum = sum + MyYuanLaiPic(i , j , k) / 3;%进行转化的关键公式，sum每次都因为后面的数字而不能超过255
%         end
%         MidGrayPic(i , j) = sum;
%     end
% end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

 h={'/hposition = 25pct','/hposition = 75pct'...
     ,'/hposition = 25pct','/hposition = 75pct'};%图片的位置-水平
 v={'/vposition = 25pct','/vposition = 25pct'...
     ,'/vposition = 75pct','/vposition = 75pct'};%图片的位置-垂直
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%生成picture和写<picture>
p=cell(number,4);%用来放图片<picture >名，用于后面的trial
for i=1:number%(1/step)
    pic=yuan*(step*i+step*floor(((1/step)-number)/2));%取中间部分的
    picname=sprintf('pic_%02d.jpg',i);
    imwrite(pic,picname,'jpg');%生成图片
    for j=1:4
        f=fopen('items.txt','a+');
    fprintf(f,'<picture %02d%d>\r\n    /items = ("%s")\r\n    /size = (300,300)\r\n    %s\r\n    %s\r\n',i,j,picname,h{j},v{j});
    fprintf(f,'</picture>\r\n');
        fclose(f);%写<picture>部分
        p{i,j}=sprintf('%02d%d',i,j);%记录picture名字
    end    
   %fprintf(f,'    /%d = ("%s")\r\n',i,picname);%把item输出到txt文件
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%写trial
f=fopen('items.txt','a+');
con=0;
for i=1:number%这里的是灰度不一样的图片
    
    ku=1:number;%生成所有行
    ku(i)=[];%去掉灰度不一样的那一行
    for j=1:number-1
        con=con+1;
        weizhi=randperm(4);wei=weizhi(1);%出现的位置
        unique=p{i,wei};%s随机一个特殊图片的位置，剩余相同的图片位置也就定了
     fprintf(f,'<trial %d>\r\n',con);
fprintf(f,'    /correctmessage = (correctmsg,500)\r\n');
fprintf(f,'    /errormessage = (errormsg,500)\r\n');
fprintf(f,'	   /pretrialpause = 500\r\n');
fprintf(f,'	   /inputdevice = mouse\r\n');
fprintf(f,'	   /correctresponse = (%s)\r\n',unique);
fprintf(f,'    /validresponse = (%s, %s, %s, %s)\r\n',unique,p{ku(j),weizhi(2)},p{ku(j),weizhi(3)},p{ku(j),weizhi(4)});
fprintf(f,'	   /ontrialbegin = [values.fixationtime = expressions.generaterandomfixation]\r\n');
fprintf(f,'	   /ontrialbegin = [values.shapetime = values.fixationtime + expressions.generaterandomshape]\r\n');
%fprintf(f,'	   /ontrialbegin = [values.stimulustimep = values.shapetime + 300]\r\n');
fprintf(f,'	   /ontrialbegin = [trial.%d.insertstimulustime(text.fixation, 0)]\r\n',con);
fprintf(f,'	   /ontrialbegin = [trial.%d.insertstimulustime(shape.blank,values.fixationtime)]\r\n',con);
fprintf(f,'	   /ontrialbegin = [trial.%d.insertstimulustime(picture.%s,values.shapetime)]\r\n',con,unique);
fprintf(f,'	   /ontrialbegin = [trial.%d.insertstimulustime(picture.%s,values.shapetime)]\r\n',con,p{ku(j),weizhi(2)});
fprintf(f,'	   /ontrialbegin = [trial.%d.insertstimulustime(picture.%s,values.shapetime)]\r\n',con,p{ku(j),weizhi(3)});
fprintf(f,'	   /ontrialbegin = [trial.%d.insertstimulustime(picture.%s,values.shapetime)]\r\n',con,p{ku(j),weizhi(4)});
%fprintf(f,'	   /ontrialbegin = [trial.%d.insertstimulustime(shape.blank,values.stimulustimep)]\r\n',con);
fprintf(f,'	   /ontrialend = [trial.%d.clearstimulusframes()]\r\n',con);
fprintf(f,'	   /beginresponsetime = values.shapetime\r\n');
fprintf(f,'</trial>\r\n');
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%写block
shunxu=randperm(number*(number-1));%trial顺序随机

fprintf(f,'<block exerciseblk1>\r\n');
fprintf(f,'     /screencolor = (0,0,0)\r\n');
fprintf(f,'	    /blockfeedback = (meanlatency,correct)\r\n');
fprintf(f,'	    /trials = [');
for i=1:number*(number-1)/2-1
    fprintf(f,'%d=%d;',i,shunxu(i));
end
i=i+1;
fprintf(f,'%d=%d]\r\n',i,shunxu(i));
fprintf(f,'</block>\r\n');
%两个block平分trial（因为trial数是偶数）
fprintf(f,'<block exerciseblk2>\r\n');
fprintf(f,'     /screencolor = (0,0,0)\r\n');
fprintf(f,'	    /blockfeedback = (meanlatency,correct)\r\n');
fprintf(f,'	    /trials = [');
for i=1+number*(number-1)/2:number*(number-1)-1
    fprintf(f,'%d=%d;',i-number*(number-1)/2,shunxu(i));
end
i=i+1;
fprintf(f,'%d=%d]\r\n',i/2,shunxu(i));
fprintf(f,'</block>\r\n');
fclose(f);