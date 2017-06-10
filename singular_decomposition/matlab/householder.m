function H = householder(x, k)
[n, ~] = size(x);
u = zeros(n, 1);
u(k) = x(k) + sign(x(k)) * sqrt(sum(x(k:n) .^ 2 ));
u((k+1):n) = x((k+1):n);
H = eye (n) - 2 .* (u * u') / dot (u , u);
end