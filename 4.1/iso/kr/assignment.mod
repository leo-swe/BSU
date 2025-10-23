
set WORKERS;
set TASKS;

param time{WORKERS, TASKS} >= 0;

var x{WORKERS, TASKS} binary;

minimize TotalTime:
sum{i in WORKERS, j in TASKS} time[i,j] * x[i,j];


# каждая задача выполняется ровно одним работником
subject to TaskAssignment{j in TASKS}:
sum{i in WORKERS} x[i,j] = 1;

# каждый работник выполняет не более одной задачи
subject to WorkerLimit{i in WORKERS}:
sum{j in TASKS} x[i,j] <= 1;