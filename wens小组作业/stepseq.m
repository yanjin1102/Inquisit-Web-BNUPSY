function stepseq = stepseq( k )
%����������trial�ĺ���
% ����k���������
k=k+1;%���ִ�0��ʼ�������1��ʼ
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
a=[answer k-1];%����0-9������λ��1-10
end
    