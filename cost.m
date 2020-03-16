function j=cost(X,y,theta);
  m=length(y);
  j=(0.5/m)*(((X*theta)-y)'*((X*theta)-y));
endfunction
