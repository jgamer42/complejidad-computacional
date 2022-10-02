import os
import sys
import psutil
import datetime
from data_geneator import generate

comparations = 0
changes = 0
def partition(array, low, high):
    global comparations
    global changes
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        comparations += 1
        if array[j] <= pivot:
            i = i + 1
            changes += 1
            (array[i], array[j]) = (array[j], array[i])
    changes+=1
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quickSort(array, low, high):
    global comparations
    global changes
    comparations += 1
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

size = int(sys.argv[1])
sys.setrecursionlimit(150000)
target_array = generate(size)
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss
start_time = datetime.datetime.now()
quickSort(target_array,0,len(target_array)-1)
end_time = datetime.datetime.now()
end_memory = process.memory_info().rss
print(f"{end_time-start_time},{(end_memory-start_memory)/1024},{comparations},{changes}",end="")