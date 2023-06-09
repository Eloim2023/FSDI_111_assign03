import requests

BACKEND_URL="http://127.0.0.1:5000/tasks"

TASK_EXAMPLES = [
    {
        "summary": "Make dinner",
        "description": "Prepare the chicken that's in the freezer"
    },
    {
        "summary": "Take out the trash",
        "description": "Garbage passes on Tuesdays"
    }
]

def create_task(summary, description):
    task_data = {
        "summary": summary,
        "description": description
    }
    response = requests.post(BACKEND_URL, json=task_data)
    if response.status_code == 204:
        print("Task created succesfully")
    else:
        print("Something went wrong while creating task")

if __name__ == "__main__":
    for task in TASK_EXAMPLES:
        create_task(
            task.get("summary"),
            task.get("description")
        )
    print("Task creation complete.")
