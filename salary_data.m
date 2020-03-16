clear ; close all; clc
data=csvread('Salary_Data.csv');
X=data(2:31,1);
y=data(2:31,2);
%plot data X vs y
plot(X,y,'rx');
hold on;
theta=zeros(2,1);
X=[ones(length(X),1),X];
j=cost(X,y,theta);
fprintf("cost function :%f\n",j);
iterations = 1000;
alpha = 0.03;
[theta ,J1]= gradientDescent(X, y, theta, alpha, iterations);
fprintf("Theta(0) :%f \nTheta(1) :%f\n",theta(1),theta(2));
z=[zeros(1,1),X(:,2)'];
z=z';
z=[ones(length(z),1),z];
plot(z(:,2),z*theta);
xlabel('yearsOfExperience');
ylabel('Salary')
;
title='yearsOfExperience vs Salary';
hold off;
%convergence Graph
figure;
plot(1:numel(J1),J1);
xlabel('No of iterations');
ylabel('J');
