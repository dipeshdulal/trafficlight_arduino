def run(commands):
    length = len(commands)
    x = 0
    import threading
    while x < length:
        exec("threading.Thread(target = "+commands[x]+").start()")
        x = x+1
    return True
