from graph.workflow import app

task = input("Enter coding task: ")

result = app.invoke({"task": task})

print("\nGenerated Code:\n")
print(result["code"])

print("\nTests:\n")
print(result["tests"])

print("\nDocumentation:\n")
print(result["docs"])