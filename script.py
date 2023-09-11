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
for task in prodev.projects[1].lists[2].get_all_tasks(include_closed = True):
    if task.id == task_id:
      task_add = {'Nome_Task': task.name, 'ID_Task': task.id, 'Dev' : task.assignees, 'Celula': task.custom_fields[4], 'Qualidade_doc': task.custom_fields[5], 
                  'Paggo Scorer': task.custom_fields[8], 'Dev Back': task.custom_fields[11], 'Dev Front': task.custom_fields[12], 'Paggo Back': task.custom_fields[13],
                  'Paggo Front': task.custom_fields[14]}

excel_file_path = 'data_tasks.xlsx'
existing_df = pd.read_excel(excel_file_path)

# Append the new row to the existing DataFrame
updated_df = existing_df.append(task_add, ignore_index=True)

# Save the updated DataFrame back to the Excel file
updated_df.to_excel(excel_file_path, index=False)
