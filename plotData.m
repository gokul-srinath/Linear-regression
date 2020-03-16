function q=plotData(X,y)
t=linspace(-10,10,100);
t1=linspace(-1,4,100);
J_vals=zeros(length(t),length(t1));
for i=1:length(t)
for j=1:length(t1)
t2=[t(i);t1(j)];
J_vals(i,j)=cost(X,y,t2)/10^8;
end
end
figure;
J_vals=J_vals';
surf(t,t1,J_vals);
figure;
contour(t,t1,J_vals,logspace(-2,3,10));
end
