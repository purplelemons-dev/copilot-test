
import psutil

def get_process_list():
    """
    Return a list of running processes
    """
    process_list = []
    for proc in psutil.process_iter():
        process_list.append(proc.name())
    return process_list

def get_process_info(process_name):
    """
    Return a list of running processes
    """
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return proc.as_dict(attrs=['pid', 'name', 'username'])

def get_process_info_by_pid(pid):
    for proc in psutil.process_iter():
        if proc.pid == pid:
            return proc.as_dict(attrs=['pid', 'name', 'username'])

# Format get_process_info output
def format_process_info(process_info):
    if process_info:
        return "PID: {pid} | Name: {name} | User: {username}".format(**process_info)
    else:
        return "Process not found"


for proc in get_process_list():
    print(format_process_info(get_process_info(proc)))
