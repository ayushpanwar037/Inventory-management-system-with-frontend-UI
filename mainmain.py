import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import mysql.connector

#connection
def create_connection():
    try:
        return mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='', 
            database='Inventory_Management_System'
        )
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None


def fetch_table_names():
    conn = create_connection()
    if conn is not None and conn.is_connected():
        try:
            cur = conn.cursor()
            cur.execute("SHOW TABLES")
            table_names = [table[0] for table in cur.fetchall()]
            return table_names
        finally:
            cur.close()
            conn.close()
    return []

# data collect
def fetch_data(table_name):
    conn = create_connection()
    if conn is not None and conn.is_connected():
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table_name}")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return columns, rows
        finally:
            cur.close()
            conn.close()
    return [], []


def update_table_contents(tree, table_name):
    if not table_name:
        messagebox.showerror("Error", "No table selected!")
        return
    columns, data = fetch_data(table_name)
    tree['columns'] = columns
    tree.delete(*tree.get_children())
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)
    for row in data:
        tree.insert('', tk.END, values=row)

# delete
def delete_selected_row(tree, table_name):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        conn = create_connection()
        if conn is not None and conn.is_connected():
            cur = conn.cursor()
            try:
                # Assuming the first column in your table is the primary key
                cur.execute(f"DELETE FROM {table_name} WHERE {tree['columns'][0]} = %s", (item['values'][0],))
                conn.commit()
                tree.delete(selected_item)
                messagebox.showinfo("Success", "Row deleted successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", str(e))
            finally:
                cur.close()
                conn.close()
    else:
        messagebox.showerror("Error", "No row selected!")

# drop table
def delete_table(table_name, table_names_cb, tree):
    if table_name:
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete the table {table_name}?"):
            conn = create_connection()
            if conn is not None and conn.is_connected():
                cur = conn.cursor()
                try:
                    cur.execute(f"DROP TABLE {table_name}")
                    conn.commit()
                    # Update table names in the combobox
                    table_names_cb['values'] = fetch_table_names()
                    tree.delete(*tree.get_children())
                    messagebox.showinfo("Success", "Table deleted successfully")
                except mysql.connector.Error as e:
                    messagebox.showerror("Error", str(e))
                finally:
                    cur.close()
                    conn.close()
    else:
        messagebox.showerror("Error", "No table selected!")

# tkinter gui
def main_app():
    root = tk.Tk()
    root.title('Database Management System')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

    
    table_names = fetch_table_names()
    selected_table = tk.StringVar()
    table_select = ttk.Combobox(main_frame, textvariable=selected_table, values=table_names)
    table_select.pack(pady=20)

    
    tree_frame = tk.Frame(main_frame)
    tree_frame.pack(fill=tk.BOTH, expand=1)
    tree = ttk.Treeview(tree_frame, show="headings")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Scrollbar
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar.set)

    
    # Buttons 
    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill=tk.X, expand=True, pady=10)

    
    load_button = tk.Button(button_frame, text="Load Table", command=lambda: update_table_contents(tree, selected_table.get()))
    load_button.pack(side=tk.LEFT, padx=10)

    
    delete_row_button = tk.Button(button_frame, text="Delete Selected Row", command=lambda: delete_selected_row(tree, selected_table.get()))
    delete_row_button.pack(side=tk.LEFT, padx=10)

    
    delete_table_button = tk.Button(button_frame, text="Delete Table", command=lambda: delete_table(selected_table.get(), table_select, tree))
    delete_table_button.pack(side=tk.LEFT, padx=10)

    # Update
    update_row_button = tk.Button(button_frame, text="Update Selected Row", command=lambda: update_selected_row(tree, selected_table.get()))
    update_row_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

# Function to updatee
def update_selected_row(tree, table_name):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        
        new_values = simpledialog.askstring("Update Row", "Enter new values separated by commas for columns: " + ", ".join(tree['columns'][1:]))
        if new_values:
            new_values_list = new_values.split(',')
            if len(new_values_list) != len(tree['columns']) - 1:
                messagebox.showerror("Error", "Incorrect number of values provided.")
                return
            conn = create_connection()
            if conn is not None and conn.is_connected():
                cur = conn.cursor()
                try:
                    
                    update_statement = f"UPDATE {table_name} SET "
                    update_statement += ", ".join([f"{col} = %s" for col in tree['columns'][1:]])
                    update_statement += f" WHERE {tree['columns'][0]} = %s"
                    
                    cur.execute(update_statement, (*new_values_list, item['values'][0]))
                    conn.commit()
                    update_table_contents(tree, table_name)  
                    messagebox.showinfo("Success", "Row updated successfully")
                except mysql.connector.Error as e:
                    messagebox.showerror("Error", str(e))
                finally:
                    cur.close()
                    conn.close()
    else:
        messagebox.showerror("Error", "No row selected!")

if __name__ == "__main__":
    main_app()
