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
      task_add = [task.name, task.id, task.assignees, task.custom_fields[4], task.custom_fields[5], task.custom_fields[8], 
                  task.custom_fields[11], task.custom_fields[12], task.custom_fields[13], task.custom_fields[14]]

dataframe.task_add
