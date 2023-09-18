import pandas as pd
from pyclickup import ClickUp
import requests

#parser = argparse.ArgumentParser()
#parser.add_argument('--task_id', type=str, required=True)
#args = parser.parse_args()

def media_harmonica(dif_e, dif_d, qual, k, c):
    dif = []
    for i in range(len(dif_e)):
        dif.append(min((5/qual)*(k+c)/(k/dif_e[i]+c/dif_d[i]), 5))
    return(dif)

def valor_customfield(field):
    try:
        value = field['value']
    except KeyError:
        value = 0
    try:
        result = int(field['type_config']['options'][value]['name'])
    except KeyError:
        result = value + 1
    return(result)

skill_rel = 3
contexto = 0.5

clickup = ClickUp("pk_55121139_JXEIXX3UOVDXVO27V1S5HJHN0KLMDZIE")#ClickUp("pk_75330699_8IIHQQANMOBS4UWKJNPP28VPXPIF0LNU")
#print(clickup.teams[0])
#print(clickup.teams[0].spaces)

main_team = clickup.teams[0]
prodev = main_team.spaces[1]
refined_backlog = prodev.projects[1].lists[0]
tasks_refined_backlog = prodev.projects[1].lists[0].get_all_tasks(include_closed = True, subtasks = True)

for task in tasks_refined_backlog:
    back_dev = valor_customfield(task.custom_fields[13])
    front_dev = valor_customfield(task.custom_fields[14])
    back_esp = valor_customfield(task.custom_fields[16])
    front_esp = valor_customfield(task.custom_fields[17])
    try:
        quality = int(task.custom_fields[8]['value'])
    except KeyError:
        quality = 5
    
    mh = media_harmonica([back_esp, front_esp], [back_dev, front_dev], quality, skill_rel, contexto)
    print(mh)
    value_update = str(format(max(mh[0], mh[1]),".2f"))

    payload = {
        "value": value_update
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "pk_55121139_JXEIXX3UOVDXVO27V1S5HJHN0KLMDZIE"
    }

    url = "https://api.clickup.com/api/v2/task/"+task.id+"/field/806764e9-d2e2-4121-bdf6-59dbe9f49c0c"
    
    requests.post(url, json = payload, headers = headers)

#task name, task_id, 4 Célula 5 Doc Quality 8 Paggo Scorer 11 [Dev] Back Points 12 [Dev] Front Points 13 [Paggo] Back Points 14 [Paggo] Front Points
#['Nome_Task', 'ID_Task', 'Dev', 'Celula', 'Qualidade_doc', 'Paggo Scorer', 'Dev Back', 'Dev Front', 'Paggo Back', 'Paggo Front']

