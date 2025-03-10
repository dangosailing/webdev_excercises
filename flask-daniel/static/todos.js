async function getTodos() {
  try {
    const response = await fetch("http://localhost:5000/todos");

    if (!response.ok) {
      throw new Error(`HTTP ERROR! Status ${response.status}`);
    }
    const todos = await response.json();
    const todoList = document.getElementById("todo-list");
    todoList.innerHTML = "";
    todos.forEach((todo) => {
      const li = document.createElement("li");
      li.textContent = `${todo.title} - ${todo.status ? "Done" : "Not done"}`;
      todoList.appendChild(li);
    });
  } catch (error) {
    console.error("Error fetching todos", error);
  }
}

getTodos();
