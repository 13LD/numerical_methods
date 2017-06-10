function [c , s, r] = givens_rot(f, g)
    if f == 0
        c = 0; 
        s = 1; 
        r = g;
    else if abs(f) > abs(g)
        t = g / f; 
        t1 = sqrt(1 + t ^2);
        c = 1 / t1; 
        s = t * c; 
        r = f * t1;
    else
        t = f / g; 
        t1 = sqrt(1 + t ^2);
        s = 1 / t1; 
        c = t * s; 
        r = g * t1 ;
    end
end