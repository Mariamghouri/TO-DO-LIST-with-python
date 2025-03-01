import streamlit as st

# 🎨 Function to set background image with a soft overlay
def add_bg():
    bg_img = "https://images.unsplash.com/photo-1593642634367-d91a135587b5?q=80&w=1920&auto=format&fit=crop"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(20, 20, 20, 0.75), rgba(20, 20, 20, 0.75)), 
                        url({bg_img}) no-repeat center center fixed;
            background-size: cover;
        }}
        .task-container {{
            background: rgba(255, 255, 255, 0.10);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
            margin-bottom: 15px;
        }}
        .sidebar .sidebar-content {{
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 1.2rem;
            border-radius: 12px;
            color: white;
        }}
        .stButton>button {{
            background-color: #444;
            color: white;
            border-radius: 8px;
            border: 1px solid #666;
            padding: 10px;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #666;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# 📝 Title with Cool Emoji
st.title("📌TO-DO LIST APP ")

# 📌 Initialize session state variables
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None  # Store the index of the task being edited

# 🎯 Sidebar Task Manager
st.sidebar.header("📋 Manage Your Tasks 🛠️")
new_task = st.sidebar.text_input("➕ Add a Task:", placeholder="✍️ Type your task here...")

if st.sidebar.button("🚀 Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.sidebar.success("🎉 Task added successfully!")
    else:
        st.sidebar.warning("⚠️ Task cannot be empty!")

# 📂 Main Task List Section
st.markdown("<div class='task-container'>", unsafe_allow_html=True)
st.subheader("📂 Your Tasks 🎯")

if not st.session_state.tasks:
    st.info("📝 No tasks added yet! Start by adding a task from the sidebar.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # ✅ Task completion checkbox
        completed = col1.checkbox(f"{task['task']}", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # ✏ Edit button
        if col2.button("✏ Edit", key=f"edit_{index}"):
            st.session_state.edit_index = index
            st.rerun()  # ✅ Refresh page

        # 🗑 Delete task button
        if col3.button("🗑 Remove", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            st.rerun()  # ✅ Refresh page

# ✨ Show edit input only when a task is being edited
if st.session_state.edit_index is not None:
    edit_index = st.session_state.edit_index
    edited_task = st.text_input("✍️ Edit Task", st.session_state.tasks[edit_index]["task"], key="edit_task_input")

    save_col, cancel_col = st.columns([0.5, 0.5])
    
    if save_col.button("💾 Save Task"):
        if edited_task.strip():
            st.session_state.tasks[edit_index]["task"] = edited_task  # Update task
            st.session_state.edit_index = None  # Exit edit mode
            st.rerun()

    if cancel_col.button("❌ Cancel Edit"):
        st.session_state.edit_index = None  # Exit edit mode
        st.rerun()

# 🧹 Clear All Tasks Button
if st.button("🚮 Clear All Tasks"):
    st.session_state.tasks = []
    st.session_state.edit_index = None  # Reset edit mode
    st.success("🗑️ All tasks deleted successfully!")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")

# 🎯 Footer Caption
st.caption("🚀 Stay productive & smash your goals with this powerful To-Do App! 💪")
