function [U, B, V] = biadiag_reduction(A)
[m, n] = size(A) ;
B = A;
U = eye(m) ;
V = eye(n) ;
for k = 1:min(m, n)
    H1 = householder(B(: , k) , k);
    B = H1 * B;
    U = U * H1';
    if k < min(m, n) - 1
        H2 = householder(B(k , :)', k+1);
        B = B * H2';
        V = V * H2';
    end
end
end