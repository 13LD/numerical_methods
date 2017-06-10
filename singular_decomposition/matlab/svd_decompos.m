function [U, S, V] = svd_decompos(A)
[U1, B, V1] = biadiag_reduction(A);
U2 = eye(size(U1));
V2 = eye(size(V1));
E = Inf;
while E > 1e-8
    [U3, B, V3, E] = qr_decompos(B);
    U2 = U2 * U3;
    V2 = V2 * V3;
end
U = U1 * U2;
V = V1 * V2;
S = B;
end