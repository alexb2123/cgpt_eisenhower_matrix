import pandas as pd

def eisenhower_matrix():
    print("Welcome to the Eisenhower Matrix Task Organizer!")
    print("Classify your tasks into the following categories:")
    print("1: Important and Urgent (Do it now)")
    print("2: Important but Not Urgent (Plan to do it)")
    print("3: Not Important but Urgent (Delegate it)")
    print("4: Not Important and Not Urgent (Eliminate it)")

    tasks = []
    
    while True:
        task_name = input("\nEnter a task (or type 'done' to finish): ").strip()
        if task_name.lower() == 'done':
            break
        try:
            priority = int(input("Enter the priority (1, 2, 3, or 4): "))
            if priority not in [1, 2, 3, 4]:
                print("Invalid input! Please enter a number between 1 and 4.")
                continue
            tasks.append({'Task': task_name, 'Priority': priority})
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Organize tasks into quadrants
    quadrants = {
        1: "Important and Urgent (Do it now)",
        2: "Important but Not Urgent (Plan to do it)",
        3: "Not Important but Urgent (Delegate it)",
        4: "Not Important and Not Urgent (Eliminate it)"
    }
    
    df = pd.DataFrame(tasks)
    df['Category'] = df['Priority'].map(quadrants)

    print("\nYour Tasks Organized by the Eisenhower Matrix:")
    print(df[['Task', 'Category']])
    
    save = input("\nWould you like to save the task list as a CSV file? (yes/no): ").strip().lower()
    if save == 'yes':
        filename = input("Enter the filename (e.g., tasks.csv): ").strip()
        df.to_csv(filename, index=False)
        print(f"Tasks saved to {filename}.")

if __name__ == "__main__":
    eisenhower_matrix()
