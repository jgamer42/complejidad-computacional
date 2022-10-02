#! /bin/bash
echo "iteration,size,time,memory,comparations,changes,algorithm" >> datos.csv
for algorithm in list_sort.py quick_sort.py shell_sort.py sorted_method.py
do
    for iteration in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    do
        for size in 100 1000 10000 100000 1000000 1500000 2000000
        do  
            echo -n "$iteration,$size," >> datos.csv
            python $algorithm $size >> datos.csv
            echo -n ",$algorithm" >> datos.csv
            echo -e "" >>datos.csv
        done
    done
done