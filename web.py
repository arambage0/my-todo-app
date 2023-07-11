import streamlit as st
import  functions

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Your new todo task", placeholder="Add new todo here.",
              on_change=add_todo, key="new_todo")
# Command to run streamlit web app
#  streamlit.cmd run .\web.py