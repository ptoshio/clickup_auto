import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyclickup import ClickUp

parser = argparse.ArgumentParser()
parser.add_argument('--task_id', type=str, required=True)
args = parser.parse_args()

task_id = args.task_id

clickup = ClickUp("pk_75330699_8IIHQQANMOBS4UWKJNPP28VPXPIF0LNU")

main_team = clickup.teams[0]
prodev = main_team.spaces[3]

task_add = []
#task name, task_id, 4 Célula 5 Doc Quality 8 Paggo Scorer 11 [Dev] Back Points 12 [Dev] Front Points 13 [Paggo] Back Points 14 [Paggo] Front Points
#['Nome_Task', 'ID_Task', 'Dev', 'Celula', 'Qualidade_doc', 'Paggo Scorer', 'Dev Back', 'Dev Front', 'Paggo Back', 'Paggo Front']
for task in prodev.projects[1].lists[2].get_all_tasks(include_closed = True):
    if task.id == task_id:
      task_add = [task.name, task.id, task.assignees, task.custom_fields[4], task.custom_fields[5], task.custom_fields[8], task.custom_fields[11], 
                  task.custom_fields[12], task.custom_fields[13], task.custom_fields[14]

# Create a DataFrame from the new row data
new_row_df = pd.DataFrame(task_add)

# Load the existing CSV file (change 'existing_file.csv' to your file path)
csv_file_path = 'task_dif.csv'
existing_df = pd.read_csv(csv_file_path)

# Append the new row to the existing DataFrame
updated_df = existing_df.append(new_row_df, ignore_index=True)

# Save the updated DataFrame back to the CSV file
updated_df.to_csv(csv_file_path, index=False)
