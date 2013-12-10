function danger
    % fake inputs for now
    enemyPos = [300,300];
    
    % create axis variables
    x = linspace(1,1000);
    y = linspace(1,1000);
    [X,Y] = meshgrid(x-enemyPos(1),y-enemyPos(2));
    
    % calculate danger
    R = sqrt(X.^2 + Y.^2);
    T = atan(Y./X) + pi*(X<0) - pi/2;
    dist = R./sinc(T/pi);
    
    
    d = exp(-dist.^2/100000) + exp(-R/20000);
    d = d + tanh(10*exp(-((X-500+enemyPos(1)).^2 + (Y-500+enemyPos(2)).^2)/800));
    
    Xp = X + enemyPos(1) - 680;
    Yp = Y + enemyPos(2) - 516;
    d = d + exp(-(sqrt(Xp.^2 + Yp.^2) - 600).^2/1000);
%     d = d + 
    
    %calculate the danger for the pool edge
    surf(x,y,d)
end