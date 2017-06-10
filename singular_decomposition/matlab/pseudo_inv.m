function X = pseudo_inv(A)
[U, S ,V] = svd(A);
s = 1 ./ diag (S);
n = size(s , 1);
S (1:n , 1:n) = diag(s);
X = V * S' * U';
end