# 📝 Task Manager (CLI-based in Python)

A simple and interactive **Command-Line Interface (CLI)** based Task Manager built entirely in one Python file. This application lets you manage tasks by adding, completing, and viewing them — all stored in a JSON file for persistence.

---

## 🚀 Features

- ✅ Add tasks
- 🟨 Mark tasks as complete
- 📋 View all tasks
- 📌 View incomplete tasks
- 🏁 View completed tasks
- 💾 Stores tasks in a `tasks.json` file
- 📂 All features bundled into a single Python script

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required (only built-in modules: `json`, `time`)

---

## 📂 Project Structure

```
task_manager.py     # Main application file
tasks.json          # JSON file to store tasks (auto-created on first run)
```

---

## 💻 How to Use

1. **Run the application**  
   Open a terminal or command prompt and run:

   ```bash
   python main.py
   ```

2. **Choose an option from the menu**:
   ```
   1 - Add a new task
   2 - Mark a task as complete
   3 - View all tasks
   4 - View incomplete tasks
   5 - View completed tasks
   6 - Exit the application
   ```

3. **Task storage format** in `tasks.json`:
   ```json
   {
     "tasks": [
       {"task": "Buy groceries", "status": false},
       {"task": "Finish project", "status": true}
     ]
   }
   ```

---

## 📌 Notes

- The application will auto-create a `tasks.json` file in the same directory if it doesn't exist.
- It handles basic errors like file not found or invalid input gracefully.
- Task names are treated as unique identifiers while marking them as complete.

---

## 📷 Sample Output

```
Welcome back! Here's your to-do list.
Enter 1 to add task
Enter 2 to mark task as complete
Enter 3 to view all tasks
Enter 4 to view incomplete tasks
Enter 5 to view complete tasks
Enter 6 to exit
Enter your choice: 1
Enter task to add: Study Python
Task Added
Returning to home in 3 2 1
```

---

## 📜 License

This project is free to use and modify under the **MIT License**.

---

## 🙌 Author

Made with ❤️ by [Piyush Raj]

---