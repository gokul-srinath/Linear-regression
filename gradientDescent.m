function [theta, J1] = gradientDescent(X, y, theta, alpha, num_iters)
m = length(y); % number of training examples
J1 = zeros(num_iters, 1);
for iter = 1:num_iters
h=(X*theta)-y;
temp0=theta(1)-alpha*(1/m)*sum(h);
temp1=theta(2)-alpha*(1/m)*sum((h).*X(:,2));
theta=[temp0;temp1];
J1(iter) = cost(X, y, theta);

end

end
