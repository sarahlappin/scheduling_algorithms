import sys
import os
import ast
# non-preemptive round robin

# (task_num, len, arrival)
def roundRobin(tasks, quanta):
    time = 0
    queue = []
    sequence = []

    print("tasks {}".format(tasks))
    # if a new task arrives add it to the queue
    for task in tasks:
        if task[2] <= time:
            queue.append(task)
            tasks.remove(task)

    if len(queue) == 0 and len(tasks) != 0:
        time = tasks[0][2]
        queue.append(tasks[0])
        tasks.remove(tasks[0])

    while(len(queue) != 0):
        # print("queue before: {}".format(queue))
        elem = queue.pop(0)
        # print("running task: {}".format(elem))
        # print("queue after: {}".format(queue))
        if (elem[1] <= quanta):
            sequence.append((time, elem[0], elem[1]))
            time += elem[1]
        else:
            sequence.append((time, elem[0], quanta))
            time += quanta
            # print("time before execution: {} ".format((elem[1])))
            # print("time left on task: {} ".format((elem[1]-quanta)))
            queue.append((elem[0], (elem[1]-quanta)))

        # if a new task arrives add it to the queue
        for task in tasks:
            if task[2] <= time:
                queue.append(task)
                tasks.remove(task)

        if len(queue) == 0 and len(tasks) != 0:
            time = tasks[0][2]
            queue.append(tasks[0])
            tasks.remove(tasks[0])

    
    # print(sequence)
    for run in sequence:
        print("{}s: Running task {}. Task ran for {} seconds.".format(run[0], run[1], run[2]))
    return sequence
    # return(1)    



def main(): 
    print(sys.argv)
    if sys.argv[1] == "--RR":
        roundRobin(ast.literal_eval(sys.argv[2]), ast.literal_eval(sys.argv[3]))

if __name__ == "__main__":
    main()