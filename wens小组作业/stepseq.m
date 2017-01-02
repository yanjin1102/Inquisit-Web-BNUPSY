function stepseq = stepseq( k )
%针对随机生成trial的函数
% 输入k是起点数字
k=k+1;%数字从0开始，矩阵从1开始
global map answer
answer=[];
map=1-eye(10);
stepseq=dfs(k);
stepseq=stepseq(1:90);
end

function a=dfs(k)
global map answer
while 1
    temp=[];
    for j=1:10
        if map(k,j)
            temp=[temp j];
        end
    end
        if ~isempty(temp)
            v=temp(randperm(length(temp),1));
            map(k,v)=0;
            answer=dfs(v);
        else
            break;
        end    
end
a=[answer k-1];%数字0-9而不是位置1-10
end
    