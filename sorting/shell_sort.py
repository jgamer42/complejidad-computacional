from profiler import profiler

@profiler
def shell_sort(array):
    comparations = 0 
    changes = 0
    interval = len(array)//2
    comparations += 1
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            comparations += 1
            while j >= interval and array[j - interval] > temp:
                changes += 1
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
    return comparations,changes
shell_sort()

