import time
file_path='C:/1-python/server.log'
def tail_log_file(file_path):
    """Generator that continuously reads new lines from a log"""
    with open(file_path,"r")as file:
        file.seek(0,2)#move to the end of the file
        while True:
            line=file.readline()
            if not line:
                time.sleep(1)#wait for new logs to added
                continue
            yield line.strip()#yield new log line
##example usage: process logs as they come in
for log in tail_log_file(file_path):
    if "ERROR"in log:
        print(f"Alert :{log}")

