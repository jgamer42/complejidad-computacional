import os
import sys
import psutil
import datetime
from data_geneator import generate
def profiler(function):
    def profile(*args,**kwargs):
        size = int(sys.argv[1])
        target_array = generate(size)
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss
        start_time = datetime.datetime.now()
        comparations,changes = function(target_array,*args,**kwargs)
        end_time = datetime.datetime.now()
        end_memory = process.memory_info().rss
        print(f"{end_time-start_time},{(end_memory-start_memory)/1024},{comparations},{changes}",end="")
    return profile
        