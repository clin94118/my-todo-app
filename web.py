import streamlit as st
import functions

newLine = '\n'
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + newLine)
    functions.write_todos(todos)
    st.session_state.new_todo = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(f"{todo}", key=f"{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo: ", label_visibility='hidden', placeholder="Add new todo... ",
              on_change=add_todo, key="new_todo")

# st.session_state