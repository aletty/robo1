function danger
    % fake inputs for now
    enemyPos = [200.5,200.5];
    
    % create axis variables
    x = linspace(1,1000);
    y = linspace(1,1000);
    [X,Y] = meshgrid(x-enemyPos(1),y-enemyPos(2));
    
    % calculate danger
    R = sqrt(X.^2 + Y.^2);
    T = atan(Y./X) + pi*(X<0) - pi/2;
    dist = R./sinc(T/pi);
    
    
    d = exp(-dist.^2/100000) + exp(-R/20000) + tanh(exp(-((X-300+enemyPos(1)).^2 + (Y-300+enemyPos(2)).^2)/2000));
    surf(x,y,d)
end