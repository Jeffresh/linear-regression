function  plot_data (x,y)
%plot_data Plots the data.

plot(x,y,'rx','MarkerSize', 10);
axis([0,100,0, 300])
ylabel('Heart rate: beats per minute');
xlabel('Body Weight: Kg'); 

end

