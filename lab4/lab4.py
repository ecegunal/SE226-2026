n = int(input("Enter number of tasks: "))

tasks = {}

for _ in range(n):
    taskadi = input("\nEnter task name: ")

    depsayisi = int(input(f"How many dependencies for {taskadi}? "))

    dependencies = []
    for i in range(depsayisi):
        dep = input(f"Enter dependency {i + 1}: ")
        dependencies.append(dep)

    tasks[taskadi] = dependencies

print("\nTASK STRUCTURE:")
for task in tasks:
    print(f"{task} -> {tasks[task]}")

print("\nINITIAL TASKS (no dependencies):")
initial_tasks = [t for t in tasks if len(tasks[t]) == 0]

if initial_tasks:
    for t in initial_tasks:
        print(t)
else:
    print("None")

completed = set()
execution_order = []
step = 1

print("\nEXECUTION ORDER:")

while len(completed) < len(tasks):
    executed_in_this_round = False

    for task in tasks:
        if task not in completed:
            if all(dep in completed for dep in tasks[task]):
                execution_order.append(task)

                completed.add(task)

                print(f"Step {step}: {task}")
                step += 1
                executed_in_this_round = True

    if not executed_in_this_round:
        break

if len(completed) == len(tasks):

    print("\nALL TASKS COMPLETED SUCCESSFULLY")
else:

    print("\nNo task can be started.")

    print("\nERROR: Circular dependency detected!")


    print("These tasks could not be completed:")

    for task in tasks:
        if task not in completed:
            print(task)
