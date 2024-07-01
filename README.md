# Python编程导论 PBL项目报告

## 项目信息

### 项目名称

进货信息导出(SQLite3数据库)

### 项目功能

- 支持店铺进货信息导入和导出
- 商品自动价格计算

### 项目优势

- 使用**SQLite3**数据库，储存量大，稳定性强
- 舍弃使用命令行shell向数据库中插入数据，选择通过CSV文件，通过WPS Excel向数据库表中填写数据，各类人群均可轻松操作，对用户更友好。
- **使用Pandas向Excel写入，读出数据**
- 选用与Python贴合度很高的Thinker库，无需安装第三方库。简单易操作，运行速度快。
- **使用Pyinstaller封装,高稳定性,不依赖外界库,可以在任何环境运行!!!**
- 程序添加了**异常处理机制**,可以增加容错率,方便用户使用

### 需求分析

小刘是烤面筋店管理部门的员工，平顶山市区各个店铺的店长每天都会通过微信向他发送需要进的货物，比如小面筋，大面筋，鸡肉肠，冷面，鸡肉串，特制麻酱和果仁辣椒的进货数量，每种货物对应不同的单价，他需要统计出不同货物对应的总价，同时，不同的店铺在平顶山对应不同的位置，不同的店长和他们各自的联系方式（手机号），按照以往，小刘会手写手动统计以上各种信息，很麻烦。现在需要使用Python编程语言，使用图形化界面，设计一款实现以上目标（导出各个烤面筋店进货信息，即统计出各个店铺预定的各种原料的总价并显示该店铺位置以及店长姓名和联系方式）。

### 项目分工

- 学习SQLite3,提供SQLite3数据库函数算法：

包括:

| 序号 | 提供的算法                          |
| ---- | ----------------------------------- |
| 1    | 初始化数据库并从CSV文件导入数据函数 |
| 2    | 从数据库读取数据函数                |
| 3    | 选择数据库文件函数                  |

- 提供显示店铺信息函数算法
- 提供导出所有门店数据函数算法
- 提供只导出该本门店数据函数算法
- 提供主函数算法
- 提供使用Pandas库的函数算法
- Thinker界面部分设计
- 软件封装(Pyinstaller)
- 程序运行的视频录制和制作
- 软件测试
- 修正意见
- 软件运维

- 提供计算总价函数算法
- 查询Pandas库资料
- 提供商品价格数据处理办法

- 选择导出类型函数
- 查询OS库资料
- 提供系统文件处理方法

- Thinker界面部分设计

## 代码实现

### 源代码

```py
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
```

### 源代码注释

这段代码主要是一个使用Tkinter建立的图形用户界面（GUI）应用程序，用于管理烤面筋店的进货信息，并可以导出数据到Excel文件。下面我将逐步解释代码的各个部分：

**导入模块**

```python
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import sqlite3
```

- `os`: 操作系统相关的接口。
- `tkinter`: 标准的Python GUI库。
- `pandas`: 用于数据处理和分析。
- `sqlite3`: SQLite数据库的接口。

**核心函数**

1. **计算总价函数**

```python
def calculate_total_price(orders, prices):
    total = 0
    for item, quantity in orders.items():
        total += quantity * prices.get(item, 0)
    return total
```

这个函数计算订单的总价，其中`orders`是一个字典，表示每种商品的数量，`prices`是一个字典，表示每种商品的单价。

2. **初始化数据库并从CSV文件导入数据**

```python
def init_db(db_path, csv_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS store_inventory')
    cursor.execute('DROP TABLE IF EXISTS store_info')

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
    ''')
    
    store_info_df = pd.read_csv(os.path.join(csv_path, 'store_info.csv'))
    store_inventory_df = pd.read_csv(os.path.join(csv_path, 'store_inventory.csv'))

    store_info_df.to_sql('store_info', conn, if_exists='append', index=False)
    store_inventory_df.to_sql('store_inventory', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()
```

这个函数会初始化数据库，并将CSV文件的数据导入到SQLite数据库中。

3. **从数据库读取数据**

```python
def read_store_data(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT store_info.store_name, location, manager, contact, item_name, quantity
        FROM store_info
        LEFT JOIN store_inventory
        ON store_info.store_name = store_inventory.store_name
    ''')
    
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
```

从数据库中读取店铺信息和进货信息，并以字典的形式返回结果。

4. **显示店铺信息函数**

```python
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
```

根据当前选中的店铺，显示对应的详细信息。

5. **选择导出类型函数**

```python
def chose_export_style():
    child_window = tk.Toplevel(root)
    child_window.geometry("300x200")

    export_all_button = tk.Button(child_window, text="导出所有门店数据", command=export_data_to_excel)
    export_all_button.pack(pady=10)

    export_specific_button = tk.Button(child_window, text="只导出该门店数据", command=export_specific_shop_data_to_excel)
    export_specific_button.pack(pady=10)

    close_button = tk.Button(child_window, text="关闭", command=child_window.destroy)
    close_button.pack(pady=10)
```

提供选择导出数据类型的窗口。

6. **导出数据到Excel函数**

```python
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
```

将所有门店的数据导出到Excel文件。

7. **导出特定门店数据函数**

```python
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
```

将特定店铺的数据导出到Excel文件。

8. **选择数据库文件函数**

```python
def select_db_file():

    if db_path:
        global store_data
        store_data = read_store_data(db_path)
        store_listbox.delete(0, tk.END)
        for store in store_data:
            store_listbox.insert(tk.END, store)
        if not store_data:
            messagebox.showwarning("警告", "所选数据库中没有有效的店铺信息。")
```

选择数据库文件并加载店铺数据。

**主函数**

```python
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
```

这个主函数配置并运行了Tkinter GUI应用程序的所有组件。最后一部分使用了`main()`函数启动应用程序。



## 软件封装

### 方式一：使用`Pyinstaller`打包

在.py文件目录下执行命令

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=GenshenImpact.ico main.py
```

运行过程

```bash
PS C:\Users\19707\Desktop\PBL项目> pyinstaller --onefile main.py
375 INFO: PyInstaller: 6.8.0, contrib hooks: 2024.7
376 INFO: Python: 3.11.7
379 INFO: Platform: Windows-10-10.0.22621-SP0
379 INFO: Python environment: C:\Program Files\Python311
379 INFO: wrote C:\Users\19707\Desktop\PBL项目\main.spec
379 INFO: Module search paths (PYTHONPATH):
......
此处省略输出
......
49248 INFO: checking PKG
49248 INFO: Building PKG because PKG-00.toc is non existent
49249 INFO: Building PKG (CArchive) main.pkg
61597 INFO: Building PKG (CArchive) main.pkg completed successfully.
61663 INFO: Bootloader C:\Program Files\Python311\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\run.exe
61663 INFO: checking EXE
61663 INFO: Building EXE because EXE-00.toc is non existent
61663 INFO: Building EXE from EXE-00.toc
61663 INFO: Copying bootloader EXE to C:\Users\19707\Desktop\PBL项目\dist\main.exe
61806 INFO: Copying icon to EXE
61951 INFO: Copying 0 resources to EXE
61951 INFO: Embedding manifest in EXE
62092 INFO: Appending PKG archive to EXE
62203 INFO: Fixing EXE headers
62521 INFO: Building EXE from EXE-00.toc completed successfully.

```

可得到不依赖外界库可以独立运行的EXE程序，并可以在桌面创建快捷方式。

![image-20240625162618724](assets/image-20240625162618724-17193040016321.png)

### 方式二：直接运行源代码

- 步骤1：安装依赖库

```bash
pip install -r requirements.txt
```

- 步骤2：命令行执行

```bash
cd C:\Users\19707\Desktop\PBL
python main.py
```

## 软件测试

### 触发异常处理

**源代码专门设计有异常处理部分用来指导顾客操作，提高程序的容错率**

#### 错误1：未选择数据库

![](assets/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-06-25%20165737.png)

#### 错误2：未选择对应店铺就尝试导出数据

![屏幕截图 2024-06-25 165753](assets/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-06-25%20165753.png)

### 运行视频

直接上传chaoxing了.

<video src="../../Videos/Desktop/WeChat_20240625175652.mp4"></video>

## 修正意见

考虑到实际的商品交易过程较为复杂，可能会加上优惠券，打折等等优惠操作，希望代码今后可以增添这些功能。

## 软件运维

### 更新

如果商品价格有调整，直接在源代码的字典中更改对应的价格即可。

### 回馈

积极相应用户的反馈，在代码中进行更改。

