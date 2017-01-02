clear all;clc;
% Current Working Path 获得当前文件所在路径，先包含文件名，后去掉
CWPath = fileparts(mfilename('fullpath'));
cd(CWPath);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%生成picture和写<picture>
f=fopen('items.txt','a+');
for i=0:9
    fprintf(f,'<text %d>\r\n',i);
fprintf(f,'    /items = ("%d")\r\n',i);
fprintf(f,'	   /fontstyle = ("楷体", 60ptc, false, false, false, false, 5, 1)\r\n');
fprintf(f,'	   /txcolor = (255,255,255)\r\n');
fprintf(f,'    /txbgcolor = (0, 0, 0)\r\n');
fprintf(f,'</text>\r\n');
end    
    fclose(f);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%写trial偶数F键，奇数J
f=fopen('items.txt','a+');
key={'F','J'};
for i=0:9
     fprintf(f,'<trial F%d>\r\n',i);
% fprintf(f,'    /correctmessage = (correctmsg,500)\r\n');
% fprintf(f,'    /errormessage = (errormsg,500)\r\n');
fprintf(f,'	   /pretrialpause = 500\r\n');
fprintf(f,'	   /correctresponse =("%s")\r\n',key{mod(i,2)+1});%偶数F键，奇数J
fprintf(f,'    /validresponse = ("F","J")\r\n');
fprintf(f,'	   /ontrialbegin = [values.fixationtime = expressions.generaterandomfixation]\r\n');
fprintf(f,'	   /ontrialbegin = [values.shapetime = values.fixationtime + expressions.generaterandomshape]\r\n');
fprintf(f,'	   /ontrialbegin = [values.stimulustimep = values.shapetime + 300]\r\n');
fprintf(f,'	   /ontrialbegin = [trial.F%d.insertstimulustime(text.fixation, 0)]\r\n',i);
fprintf(f,'	   /ontrialbegin = [trial.F%d.insertstimulustime(shape.blank,values.fixationtime)]\r\n',i);
fprintf(f,'	   /ontrialbegin = [trial.F%d.insertstimulustime(text.%d,values.shapetime)]\r\n',i,i);
fprintf(f,'	   /ontrialbegin = [trial.F%d.insertstimulustime(shape.blank,values.stimulustimep)]\r\n',i);
fprintf(f,'	   /ontrialend = [trial.F%d.clearstimulusframes()]\r\n',i);
fprintf(f,'	   /beginresponsetime = values.shapetime\r\n');
fprintf(f,'</trial>\r\n');
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%写trial偶数J键，奇数F
%key={'J','F'};
for i=0:9
     fprintf(f,'<trial J%d>\r\n',i);
% fprintf(f,'    /correctmessage = (correctmsg,500)\r\n');
% fprintf(f,'    /errormessage = (errormsg,500)\r\n');
fprintf(f,'	   /pretrialpause = 500\r\n');
fprintf(f,'	   /correctresponse =("%s")\r\n',key{mod(1+i,2)+1});%偶数J键，奇数F
fprintf(f,'    /validresponse = ("F","J")\r\n');
fprintf(f,'	   /ontrialbegin = [values.fixationtime = expressions.generaterandomfixation]\r\n');
fprintf(f,'	   /ontrialbegin = [values.shapetime = values.fixationtime + expressions.generaterandomshape]\r\n');
fprintf(f,'	   /ontrialbegin = [values.stimulustimep = values.shapetime + 300]\r\n');
fprintf(f,'	   /ontrialbegin = [trial.J%d.insertstimulustime(text.fixation, 0)]\r\n',i);
fprintf(f,'	   /ontrialbegin = [trial.J%d.insertstimulustime(shape.blank,values.fixationtime)]\r\n',i);
fprintf(f,'	   /ontrialbegin = [trial.J%d.insertstimulustime(text.%d,values.shapetime)]\r\n',i,i);
fprintf(f,'	   /ontrialbegin = [trial.J%d.insertstimulustime(shape.blank,values.stimulustimep)]\r\n',i);
fprintf(f,'	   /ontrialend = [trial.J%d.clearstimulusframes()]\r\n',i);
fprintf(f,'	   /beginresponsetime = values.shapetime\r\n');
fprintf(f,'</trial>\r\n');
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%写练习block
for j=1:2
    %a=[];shunxu=[];
    shunxu=randperm(10)-1;%trial顺序随机
    a=randperm(9)-1;
    shunxu=[shunxu a(1) a(2)];
fprintf(f,'<block exerciseblk%d>\r\n',j);
fprintf(f,'     /screencolor = (0,0,0)\r\n');
fprintf(f,'	    /blockfeedback = (meanlatency,correct)\r\n');
fprintf(f,'	    /trials = [');
for i=1:11
    fprintf(f,'%d=%s%d;',i,key{j},shunxu(i));%1对应偶数是F键的
end
i=i+1;
fprintf(f,'%d=%s%d]\r\n',i,key{j},shunxu(i));
fprintf(f,'</block>\r\n');
%两个block,练习加上正式
shunxu2=stepseq(randperm(10,1)-1);%随机90个数
fprintf(f,'<block judgeblk%d>\r\n',j);
fprintf(f,'     /screencolor = (0,0,0)\r\n');
fprintf(f,'	    /blockfeedback = (meanlatency,correct)\r\n');
fprintf(f,'	    /trials = [');
for i=1:89
    fprintf(f,'%d=%s%d;',i,key{j},shunxu2(i));
end
i=i+1;
fprintf(f,'%d=%s%d]\r\n',i,key{j},shunxu2(i));
fprintf(f,'</block>\r\n');
end
fclose(f);