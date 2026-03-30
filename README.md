# ZB_tools — 招投标制作工具

一个基于 PyQt5 的桌面应用，用于管理、浏览和检索招投标资料库，支持文件名搜索、内容全文搜索以及 DOCX 文件预览。

---

## 功能特性

- 📁 **资料库管理** — 打开本地文件夹作为资料库，分层展示目录结构
- 🔍 **文件名检索** — 基于通配符的文件名模糊搜索（支持 `*keyword*` 模式）
- 📄 **内容搜索** — 遍历资料库内所有文件，搜索文件名中包含关键词的文件列表（多线程后台扫描，不阻塞界面）
- 📖 **DOCX 预览** — 在右侧面板直接查看 `.docx` 文件的段落文本内容
- ⚙️ **进度条** — 文件扫描过程实时显示进度
- 🎨 **UI 动效** — 搜索框警示动画（左右抖动），提升交互反馈感
- 🧠 **学习资源** — 内置 Study/ 目录，提供 PyQt5 核心模块的学习代码（QThread、Model-View、TreeView 等）

---

## 目录结构

```
ZB_tools/
├── main.py                 # 程序入口，启动 QApplication 并实例化主窗口
├── MainWindow.py           # 主窗口类，定义基础窗口结构和 UI 动效方法
├── MainWindow_Ui.py        # PyQt5 UI 代码生成器（由 .ui 文件自动生成，勿手动编辑）
├── MainWindow_Ui.ui        # Qt Designer 界面设计文件
├── slot_func.py           # 核心槽函数实现（继承 MainWindow），包含搜索、预览、线程等功能
├── test.ui                 # 测试用 UI 文件
├── pyvenv.cfg              # 虚拟环境配置
└── Study/                  # PyQt5 学习代码集
    ├── 线程学习.py          # threading 模块多线程实战
    ├── Qthread学习.py       # QThread 线程学习
    ├── 标准模型演示.py      # QFileSystemModel / QStringListModel / QSortFilterProxyModel 演示
    ├── treeview学习.py      # QTreeView 组件学习
    ├── 构造函数.py          # 类与构造函数学习
    ├── 多重继承类.py         # Python 多重继承示例
    ├── Class_study.py       # Python 类基础学习
    ├── test_func.py         # 函数测试
    ├── test.py / test2.py   # 测试文件
    └── ...
```

---

## 快速开始

### 环境要求

- Python 3.9+
- PyQt5
- python-docx

### 安装依赖

```bash
pip install PyQt5 python-docx
```

### 运行

```bash
python main.py
```

> 程序窗口大小为 1440×785，最佳在 1080p 及以上显示器使用。

---

## 使用说明

1. **打开资料库** — 点击工具栏「资料库」按钮，选择本地一个文件夹作为资料库根目录，左侧树形视图将加载目录结构。
2. **文件名检索** — 在搜索框输入关键词，按回车或点击「检索」，左侧视图将过滤出文件名包含该关键词的文件。
3. **内容搜索** — 首次打开资料库后，点击「内容」按钮，后台多线程扫描目录，扫描完成后在下拉列表中展示所有匹配文件。
4. **预览文档** — 在左侧树形视图或列表中双击任意 `.docx` 文件，右侧面板将显示其段落文本内容。

---

## 核心模块说明

| 文件 | 职责 |
|------|------|
| `main.py` | 程序入口，负责创建 QApplication 和实例化 Slotfunc 主窗口 |
| `MainWindow.py` | 基础窗口类（继承 QMainWindow），定义 `Alert_animation()` 等 UI 工具方法 |
| `slot_func.py` | 核心业务逻辑，继承 MainWindow，包含所有槽函数（搜索、预览、线程控制等） |
| `MainWindow_Ui.py` | PyUIC 自动生成，定义 UI 控件布局（不可手动编辑） |
| `Study/` | PyQt5 组件学习代码，供开发者参考学习 |

---

## 技术栈

- **GUI 框架**: PyQt5 5.15
- **文档读取**: python-docx
- **并发**: QThread（Qt 原生线程，避免 GUI 阻塞）
- **Model-View**: QFileSystemModel / QStandardItemModel / QSortFilterProxyModel
- **Python**: 3.9+

---

## 适用场景

- 招投标从业者管理大量投标资料文件
- 需要快速在本地资料库中检索文件或内容
- 学习 PyQt5 桌面应用开发（Study/ 目录提供了丰富的示例代码）

---

## 代码质量评注

- ✅ **UI 与业务逻辑分离**: 使用 `loadUi` 模式，UI 代码由 Designer 生成，业务逻辑集中在 `slot_func.py`，结构清晰
- ✅ **多线程设计**: 目录扫描使用 QThread，后台运行不阻塞 UI，体验流畅
- ✅ **信号槽机制**: 使用 PyQt5 原生 `pyqtSignal` 实现线程与主线程通信，可靠且规范
- ✅ **代码注释丰富**: 主要函数均有中文注释，便于理解和维护
- ⚠️ **日志开关**: logging 已在 main.py 开启 DEBUG 级别，生产环境建议调整为 WARNING 或 ERROR
- ⚠️ **动画变量累积 Bug**: `Alert_animation` 中坐标计算存在轻微 bug（二次执行时 x 值会累积偏移），可进一步优化

---

## 待优化方向（供贡献者参考）

- [ ] 支持正则表达式搜索
- [ ] 支持非 DOCX 格式（如 PDF、TXT）的文档预览
- [ ] 搜索结果高亮显示
- [ ] 添加国际化（i18n）支持
- [ ] 修复 `Alert_animation` 二次执行坐标偏移问题
