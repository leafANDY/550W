# 更新日志

本文件记录了550W终端模拟器的所有重要变更。

## [当前版本] - 2025-8-14

### 新增功能
- ✨ 完整的用户认证系统
  - 用户注册功能 (`useradd`)
  - 安全登录验证
  - 密码哈希加密存储 (SHA-512双重加密)
  - 登录状态持久化

- 📁 丰富的文件操作命令
  - `ls` - 列出目录内容
  - `cd` - 目录切换，支持盘符切换
  - `pwd` - 显示当前工作目录
  - `rm` - 删除文件
  - `mv` - 移动/重命名文件
  - `cp` - 复制文件
  - `mkdir` - 创建单级目录
  - `makedirs` - 创建多级目录
  - `rmdir` - 删除空目录
  - `rmtree` - 递归删除目录树
  - `chmod` - 修改文件权限

- 🧮 数学表达式计算器
  - 支持基本算术运算 (+, -, *, /, %, **)
  - 支持比较运算符 (==, !=, <, >, <=, >=)
  - 支持整除运算 (//)
  - 实时表达式求值

- 🎨 美观的用户界面
  - ASCII艺术标题显示
  - 基于Rich库的彩色输出
  - 50+种加载动画效果
  - 自定义颜色主题支持
  - 状态指示器和进度显示

- ⚙️ 系统管理功能
  - `time` - 显示当前系统时间
  - `clear` - 清屏功能
  - `reboot` - 系统重启
  - `logout` - 用户登出
  - `quit` - 安全退出程序
  - `userdel` - 删除用户账户

- 🔧 配置管理
  - JSON格式的设置文件 (`setting.json`)
  - 密码文件安全存储 (`pass.json`)
  - 首次启动引导流程
  - 登录状态记忆功能

### 技术特性
- 🔒 **安全性**
  - 密码隐藏输入
  - SHA-512双重哈希加密
  - 安全的文件操作权限检查

- 🎯 **用户体验**
  - 智能命令识别
  - 错误提示音效
  - 友好的错误信息显示
  - 命令参数自动解析

- 🚀 **性能优化**
  - 高效的命令查找机制
  - 最小化文件I/O操作
  - 优化的内存使用

### 支持的加载动画
项目包含以下加载动画效果：
- `aesthetic`, `arc`, `arrow`, `arrow2`, `arrow3`
- `balloon`, `balloon2`, `betaWave`, `bounce`
- `bouncingBall`, `bouncingBar`, `boxBounce`, `boxBounce2`
- `christmas`, `circle`, `circleHalves`, `circleQuarters`
- `clock`, `dots` 系列 (dots1-10)
- `dots8Bit`, `earth`, `fire`, `flip`, `hamburger`
- `hearts`, `layer`, `line`, `moon`, `noise`
- `pipe`, `point`, `pong`, `runner`, `sand`
- `shark`, `simpleDots`, `simpleDotsScrolling`
- `smiley`, `squareCorners`, `star`, `star2`
- `toggle` 系列, `triangle`, `weather`

### 文件结构
```
550W/
├── main.py          # 主程序文件 (17.2KB)
├── setting.json     # 系统设置配置
├── pass.json        # 用户密码存储
├── run.bat         # Windows快速启动脚本
├── 计划.txt         # 开发路线图
├── CHANGELOG.md    # 本更新日志
└── README.md       # 项目文档
```

### 开发计划
未来版本规划中的功能：
- 🔑 密钥更改功能
- 🎤 语音输入支持
- 🔧 KCM (Kernel Configuration Management) 功能
- 🌐 Unicode字符互转工具
-...

### 系统要求
- Python 3.6+
- Rich库 (用于终端美化)
- Windows/Linux/macOS 兼容

### 安装说明
1. 确保安装Python环境
2. 安装依赖: `pip install rich`
3. 运行程序: `python main.py`
4. 首次使用需创建用户账户

---

## 开发信息

- **项目名称**: 550W Terminal Emulator
- **开发语言**: Python
- **主要依赖**: Rich (终端美化库)
- **配置格式**: JSON
- **加密算法**: SHA-512 (双重哈希)

---

*注意: 本更新日志将持续更新，记录项目的所有重要变更和新功能。*
