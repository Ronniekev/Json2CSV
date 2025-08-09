import csv
import os

def create_csv(plan_name, plan, plan_time, allocated_time):
    """ Function creates a CSV file containing a list of tasks for the day.
    Params: - plan list with {id} and {duration}
    - plan name
    -total plan time
    -total allocated time"""

    plan_time = 0

    for task in plan:
        plan_time += task['duration']
   
    file_name = f'{plan_name}.csv'
    download = os.path.join(os.path.expanduser('~'), 'Downloads')
    path = os.path.join(download, file_name)

    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer =csv.writer(csvfile, delimiter=' ')
        writer.writerow(plan_name)
        writer.writerow('    '+ plan[1].keys())
        for task in plan:
            row = ['[ ]'] + list(task.values())
            writer.writerow(row)
        writer.writerow([f"This plan uses {plan_time} minutes of {allocated_time} minutes available.\n"])
        return f'File {file_name} created, can be found in downloads folder.'


