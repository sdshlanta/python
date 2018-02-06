import os
import sys

if(len(sys.argv) == 2):
    program_used = str(sys.argv[1])
    userpath = str(os.environ['USERPROFILE'])
    file_path = userpath + "/Documents/python/gui_interface/log_count.txt"
    try:
        append = open(file_path,"a")
        append.write(program_used + "\n")
        append.close()
    except FileNotFoundError: # if the file doesn't exist then create it
        write = open(file_path,"w")
        write.write(program_used + "\n")
        write.close()
else:
    pass
    