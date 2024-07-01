import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import sqlite3

# 计算总价函数
def calculate_total_price(orders, prices):
    total = 0
    for item, quantity in orders.items():
        total += quantity * prices.get(item, 0)
    return total

# 初始化数据库并从CSV文件导入数据
def init_db(db_path, csv_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 清空数据库表
    cursor.execute('DROP TABLE IF EXISTS store_inventory')
    cursor.execute('DROP TABLE IF EXISTS store_info')

    # 重新创建数据库表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS store_info (
            store_name TEXT PRIMARY KEY,
            location TEXT,
            manager TEXT,
            contact TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS store_inventory (
            store_name TEXT,
            item_name TEXT,
            quantity INTEGER,
            FOREIGN KEY(store_name) REFERENCES store_info(store_name)
        )
    ''')# 添加了外键约束
    
    # 导入CSV数据
    store_info_df = pd.read_csv(os.path.join(csv_path, 'store_info.csv'))
    store_inventory_df = pd.read_csv(os.path.join(csv_path, 'store_inventory.csv'))

    store_info_df.to_sql('store_info', conn, if_exists='append', index=False)
    store_inventory_df.to_sql('store_inventory', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()

# 从数据库读取数据
def read_store_data(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT store_info.store_name, location, manager, contact, item_name, quantity
        FROM store_info
        LEFT JOIN store_inventory
        ON store_info.store_name = store_inventory.store_name
    ''')# 使用外部左连接，当发送订单的店铺名称本身就存在于数据库store_info中时，进行数据库连接操作。

    store_data = {}
    for row in cursor.fetchall():
        store_name, location, manager, contact, item_name, quantity = row
        if store_name not in store_data:
            store_data[store_name] = {
                '位置': location,
                '店长': manager,
                '联系方式': contact,
                '进货': {}
            }
        if item_name:
            store_data[store_name]['进货'][item_name] = quantity
    conn.close()
    return store_data

# 显示店铺信息函数
def show_store_info():
    store_name = store_listbox.get(store_listbox.curselection())
    info = store_data[store_name]

    info_text = f"位置: {info['位置']}\n"
    info_text += f"店长: {info['店长']}\n"
    info_text += f"联系方式: {info['联系方式']}\n\n"
    info_text += "进货:\n"
    for item, quantity in info['进货'].items():
        info_text += f"{item}: {quantity} 个"
        info_text += f"    共{quantity*item_prices[item]}元\n"

    total_price = calculate_total_price(info['进货'], item_prices)
    info_text += f"\n总价: {total_price} 元"

    store_info_label.config(text=info_text)

# 选择导出类型函数
def chose_export_style():
    child_window = tk.Toplevel(root)
    child_window.geometry("300x200")

    export_all_button = tk.Button(child_window, text="导出所有门店数据", command=export_data_to_excel)
    export_all_button.pack(pady=10)

    export_specific_button = tk.Button(child_window, text="只导出该门店数据", command=export_specific_shop_data_to_excel)
    export_specific_button.pack(pady=10)

    close_button = tk.Button(child_window, text="关闭", command=child_window.destroy)
    close_button.pack(pady=10)

# 导出所有门店数据函数
def export_data_to_excel():
    try:
        rows = []
        for store_name, info in store_data.items():
            row = {
                '店铺': store_name,
                '位置': info['位置'],
                '店长': info['店长'],
                '联系方式': info['联系方式']
            }
            for goods_name, goods_quantity in info['进货'].items():
                row[goods_name] = goods_quantity
                row[goods_name+"总价"] = item_prices[goods_name]*goods_quantity
            row['总价'] = calculate_total_price(info['进货'], item_prices)
            rows.append(row)

        df = pd.DataFrame(rows)

        file_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel files', '.xlsx')])
        if not file_path:
            return

        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            workbook = writer.book
            sheet = writer.sheets['Sheet1']

            sheet.column_dimensions['D'].width = 20

            for cell in sheet['D']:
                cell.number_format = '@'

        messagebox.showinfo("导出成功", f"数据已成功导出至 {file_path}")

    except Exception as e:
        messagebox.showerror("错误", f"你尚未选择数据库！请先选择已经录入的数据库{e}")

# 只导出该本门店数据函数
def export_specific_shop_data_to_excel():
    try:
        store_name = store_listbox.get(store_listbox.curselection())
    except Exception as e:
        messagebox.showerror("错误", f"你尚未选择店铺,请先选择一个店铺！\n计算机抛出异常:{e}")

    else:
        info = store_data[store_name]
        row = {'店铺': store_name,
               '位置': info['位置'],
               '店长': info['店长'],
               '联系方式': info['联系方式']}
        for goods_name, goods_quantity in info['进货'].items():
            row[goods_name] = goods_quantity
            row[goods_name+"总价"] = item_prices[goods_name]*goods_quantity
            row['总价'] = calculate_total_price(info['进货'], item_prices)

        df = pd.DataFrame([row])

        file_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel files', '.xlsx')])
        if not file_path:
            return

        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            workbook = writer.book
            sheet = writer.sheets['Sheet1']

            sheet.column_dimensions['D'].width = 20

            for cell in sheet['D']:
                cell.number_format = '@'

        messagebox.showinfo("导出成功", f"数据已成功导出至 {file_path}")

# 选择数据库文件函数
def select_db_file():

    if db_path:
        global store_data
        store_data = read_store_data(db_path)
        store_listbox.delete(0, tk.END)
        for store in store_data:
            store_listbox.insert(tk.END, store)
        if not store_data:
            messagebox.showwarning("警告", "所选数据库中没有有效的店铺信息。")

# 主函数
def main():
    global root, store_listbox, store_info_label, item_prices, store_data , db_path , csv_path
    item_prices = {'小面筋': 2, '大面筋': 3, '鸡肉肠': 1.5, '冷面': 2.5, '鸡肉串': 20, '特制麻酱': 50, '果仁辣椒': 50}
    
    root = tk.Tk()
    root.title("烤面筋店进货统计")
    root.geometry("800x600")
    
    cwd = os.getcwd()
    db_path = os.path.join(cwd, r"store_info\cvs\kaomianjin_store.db")
    csv_path = os.path.join(cwd, r"store_info\cvs")
    init_db(db_path, csv_path)  # 初始化数据库并导入CSV数据
    
    store_listbox = tk.Listbox(root, font=("Arial", 14))
    store_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    store_listbox.bind("<<ListboxSelect>>", lambda evt: show_store_info())
    
    store_info_label = tk.Label(root, text="", justify=tk.LEFT, font=("Arial", 14))
    store_info_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    select_db_button = tk.Button(root, text="使用已录入的数据库", command=select_db_file, font=("Arial", 14))
    select_db_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    export_button = tk.Button(root, text="导出数据", command=chose_export_style, font=("Arial", 14))
    export_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
