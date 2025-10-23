param m; # количество культур
param n; # количество типов погоды

param A{1..m, 1..n}; # матрица выигрышей

var x{1..m} >= 0;

minimize Total: sum{i in 1..m} x[i];

subject to Weather{j in 1..n}:
sum{i in 1..m} A[i,j] * x[i] >= 1;