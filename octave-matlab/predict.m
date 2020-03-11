function h = predict(input,theta)
%PREDICT Summary of this function goes here
%   Detailed explanation goes here

h =[ones(1,size(input,2));input]' *theta;

end

