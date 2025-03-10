async function addTodo(title, status) {
  data = { title: title, status: status };
  const response = await fetch("http://localhost:5000/todos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return await response.json();
}

document
  .getElementById("add-todo-form")
  .addEventListener("submit", async function (event) {
    // Even with async the it tries to set the text content before we get the result
    //event.preventDefault();

    const title = document.getElementById("todo-title").value;
    const status = false;

    const result = await addTodo(title, status);
    document.getElementById["message"].textContent =
      await result.message || "Todo Created!";
  });
