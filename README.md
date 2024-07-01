# Python编程导论 PBL项目报告

## 项目信息

### 小组成员

杨开心(组长) 

邹汶伦

裴紫豪

陈启轩

### 项目名称

烤面筋店进货信息导出工具 

### 需求分析

小刘是烤面筋店管理部门的员工，平顶山市区各个店铺的店长每天都会通过微信向他发送需要进的货物，比如小面筋，大面筋，鸡肉肠，冷面，鸡肉串，特制麻酱和果仁辣椒的进货数量，每种货物对应不同的单价，他需要统计出不同货物对应的总价，同时，不同的店铺在平顶山对应不同的位置，不同的店长和他们各自的联系方式（手机号），按照以往，小刘会手写手动统计以上各种信息，很麻烦。现在需要使用Python编程语言，使用图形化界面，设计一款实现以上目标（导出各个烤面筋店进货信息，即统计出各个店铺预定的各种原料的总价并显示该店铺位置以及店长姓名和联系方式）。

### 项目分工



## 代码实现

## 软件封装

使用`Pyinstaller`打包

在.py文件目录下执行命令

```bash
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
['C:\\Program Files\\Python311\\Scripts\\pyinstaller.exe',
 'C:\\Program Files\\Python311\\python311.zip',
 'C:\\Program Files\\Python311\\DLLs',
 'C:\\Program Files\\Python311\\Lib',
 'C:\\Program Files\\Python311',
 'C:\\Users\\19707\\AppData\\Roaming\\Python\\Python311\\site-packages',
 'C:\\Users\\19707\\AppData\\Roaming\\Python\\Python311\\site-packages\\win32',
 'C:\\Users\\19707\\AppData\\Roaming\\Python\\Python311\\site-packages\\win32\\lib',
 'C:\\Users\\19707\\AppData\\Roaming\\Python\\Python311\\site-packages\\Pythonwin',
 'C:\\Program Files\\Python311\\Lib\\site-packages',
 'C:\\Users\\19707\\Desktop\\PBL项目']
615 INFO: checking Analysis
615 INFO: Building Analysis because Analysis-00.toc is non existent
615 INFO: Running Analysis Analysis-00.toc
615 INFO: Target bytecode optimization level: 0
615 INFO: Initializing module dependency graph...
615 INFO: Caching module graph hooks...
620 INFO: Analyzing base_library.zip ...
1706 INFO: Loading module hook 'hook-heapq.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
1769 INFO: Loading module hook 'hook-encodings.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
2977 INFO: Loading module hook 'hook-pickle.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
3925 INFO: Caching module dependency graph...
4004 INFO: Looking for Python shared library...
4004 INFO: Using Python shared library: C:\Program Files\Python311\python311.dll
4004 INFO: Analyzing C:\Users\19707\Desktop\PBL项目\main.py
4084 INFO: Loading module hook 'hook-_tkinter.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
4131 INFO: Loading module hook 'hook-pandas.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
5179 INFO: Loading module hook 'hook-platform.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
5186 INFO: Loading module hook 'hook-sysconfig.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
5202 INFO: Loading module hook 'hook-numpy.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\numpy\\_pyinstaller'...
5611 INFO: Loading module hook 'hook-difflib.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
5721 INFO: Loading module hook 'hook-multiprocessing.util.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
5847 INFO: Loading module hook 'hook-xml.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
6545 INFO: Loading module hook 'hook-psutil.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
7789 INFO: Loading module hook 'hook-pytz.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
8105 INFO: Loading module hook 'hook-pkg_resources.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
10392 INFO: Loading module hook 'hook-pandas.io.formats.style.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
11398 INFO: Loading module hook 'hook-botocore.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
13156 INFO: Loading module hook 'hook-IPython.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
14954 INFO: Loading module hook 'hook-xml.dom.domreg.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
15069 INFO: Loading module hook 'hook-matplotlib.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
15415 INFO: Loading module hook 'hook-packaging.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
15637 INFO: Processing pre-safe import module hook gi from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module\\hook-gi.py'.
15699 INFO: Loading module hook 'hook-PIL.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
15746 INFO: Loading module hook 'hook-PIL.Image.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
16168 INFO: Loading module hook 'hook-pycparser.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
16563 INFO: Loading module hook 'hook-setuptools.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
18174 INFO: Processing pre-safe import module hook distutils from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module\\hook-distutils.py'.
18174 INFO: Processing pre-find module path hook distutils from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-distutils.py'.
18599 INFO: Loading module hook 'hook-distutils.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
18643 INFO: Loading module hook 'hook-distutils.util.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
19575 INFO: Loading module hook 'hook-PIL.ImageFilter.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
20156 INFO: Loading module hook 'hook-matplotlib.backends.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
21305 INFO: Processing pre-safe import module hook six.moves from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module\\hook-six.moves.py'.
22559 INFO: Loading module hook 'hook-certifi.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
22590 INFO: Loading module hook 'hook-pygments.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
24399 INFO: Loading module hook 'hook-wcwidth.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
25154 INFO: Loading module hook 'hook-jedi.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
26543 INFO: Loading module hook 'hook-parso.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
27383 INFO: Loading module hook 'hook-sqlite3.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
27917 INFO: Loading module hook 'hook-zmq.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
28751 INFO: Loading module hook 'hook-platformdirs.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
28845 INFO: Loading module hook 'hook-cryptography.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
30019 INFO: Loading module hook 'hook-bcrypt.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
30155 INFO: Loading module hook 'hook-pywintypes.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
30706 INFO: Loading module hook 'hook-nacl.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
31807 INFO: Loading module hook 'hook-pandas.plotting.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
32294 INFO: Loading module hook 'hook-openpyxl.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
32578 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
33602 INFO: Loading module hook 'hook-pandas.io.clipboard.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
34500 INFO: Loading module hook 'hook-charset_normalizer.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
35145 INFO: Processing module hooks...
35176 INFO: Loading module hook 'hook-matplotlib.backends.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
35176 INFO: Matplotlib backend selection method: automatic discovery of used backends
35443 INFO: Trying determine the default backend as first importable candidate from the list: ['QtAgg', 'Qt5Agg', 'Gtk4Agg', 'Gtk3Agg', 'TkAgg', 'WxAgg']
36877 INFO: Selected matplotlib backends: ['TkAgg']
37242 INFO: Loading module hook 'hook-PIL.SpiderImagePlugin.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
37273 INFO: Processing pre-safe import module hook win32com from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\pre_safe_import_module\\hook-win32com.py'.
37320 INFO: Loading module hook 'hook-win32com.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
37320 INFO: Loading module hook 'hook-pythoncom.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
39054 INFO: Loading module hook 'hook-setuptools.msvc.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
39541 INFO: Loading module hook 'hook-setuptools._distutils.command.check.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
39683 INFO: Loading module hook 'hook-_tkinter.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
39683 INFO: checking Tree
39699 INFO: Building Tree because Tree-00.toc is non existent
39699 INFO: Building Tree Tree-00.toc
39793 INFO: checking Tree
39793 INFO: Building Tree because Tree-01.toc is non existent
39793 INFO: Building Tree Tree-01.toc
39810 INFO: checking Tree
39810 INFO: Building Tree because Tree-02.toc is non existent
39810 INFO: Building Tree Tree-02.toc
40061 INFO: Performing binary vs. data reclassification (5215 entries)
41687 INFO: Looking for ctypes DLLs
41837 INFO: Analyzing run-time hooks ...
41844 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_inspect.py'
41844 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_pkgutil.py'
41844 INFO: Processing pre-find module path hook _pyi_rth_utils from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-_pyi_rth_utils.py'.
41844 INFO: Loading module hook 'hook-_pyi_rth_utils.py' from 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks'...
41844 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_multiprocessing.py'
41844 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\rthooks\\pyi_rth_traitlets.py'
41844 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_pkgres.py'
41860 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\rthooks\\pyi_rth_pywintypes.py'
41860 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\rthooks\\pyi_rth_pythoncom.py'
41860 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_setuptools.py'
41860 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_mplconfig.py'
41860 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\rthooks\\pyi_rth_cryptography_openssl.py'
41860 INFO: Including run-time hook 'C:\\Program Files\\Python311\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth__tkinter.py'
42034 INFO: Looking for dynamic libraries
C:\Program Files\Python311\Lib\site-packages\PyInstaller\building\build_main.py:205: UserWarning: The numpy.array_api submodule is still experimental. See NEP 47.
  __import__(package)
0.01s - Debugger warning: It seems that frozen modules are being used, which may
0.00s - make the debugger miss breakpoints. Please pass -Xfrozen_modules=off
0.00s - to python to disable frozen modules.
0.00s - Note: Debugging will proceed. Set PYDEVD_DISABLE_FILE_VALIDATION=1 to disable this validation.
44401 INFO: Extra DLL search directories (AddDllDirectory): ['C:\\Program Files\\Python311\\Lib\\site-packages\\pandas.libs', 'C:\\Program Files\\Python311\\Lib\\site-packages\\numpy.libs', 'C:\\Program Files\\Python311\\Lib\\site-packages\\matplotlib.libs', 'C:\\Program Files\\Python311\\Lib\\site-packages\\matplotlib.libs', 'C:\\Users\\19707\\AppData\\Roaming\\Python\\Python311\\site-packages\\pyzmq.libs']
44401 INFO: Extra DLL search directories (PATH): []
46454 INFO: Warnings written to C:\Users\19707\Desktop\PBL项目\build\main\warn-main.txt
46644 INFO: Graph cross-reference written to C:\Users\19707\Desktop\PBL项目\build\main\xref-main.html
46772 INFO: checking PYZ
46772 INFO: Building PYZ because PYZ-00.toc is non existent
46772 INFO: Building PYZ (ZlibArchive) C:\Users\19707\Desktop\PBL项目\build\main\PYZ-00.pyz
49071 INFO: Building PYZ (ZlibArchive) C:\Users\19707\Desktop\PBL项目\build\main\PYZ-00.pyz completed successfully.
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

## 软件测试

## 修正意见

## 软件运维
