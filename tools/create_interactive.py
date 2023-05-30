from create_task import create_task

if __name__ == "__main__":
    print("Create task (interactive mode):")
    summary = input("Enter summary:")
    description = input("Enter description:")
    create_task(summary, description)