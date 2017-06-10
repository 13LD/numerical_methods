function [U, B, V, E] = qr_decompos(B)
[m, n] = size(B);
U = eye(m);
V = eye(n);
M = min(m, n);
for k = 1:M-1
    [c, s, ~] = givens_rot(B(k , k), B(k, k+1));
    Q = eye(n);
    Q(k:k+1, k:k+1) = [c s; -s c ];
    B = B * Q';
    V = V * Q';
    B((abs(B) < 1.e-13)) = 0 ;
    [c, s, ~] = givens_rot(B(k , k) ,B(k+1, k ));
    Q = eye(m);
    Q(k:k+1, k:k+1) = [ c s ; - s c];
    B = Q * B;
    U = U * Q';
    B((abs(B) < 1.e-13)) = 0 ;
end
I = zeros(m, n);
I(1:M, 1:M) = diag(ones(1, M-1), 1);
E = sum(sum(abs(I .* B)));
end