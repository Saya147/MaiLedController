# MaiLedController

一个基于 Python 的 8 灯珠圆环控制器，协议逻辑参考自 [MajdataPlay](https://github.com/LingFeng-bbben/MajdataPlay)。

## 🚀 功能特性
- **基础控制** (`main.py`): 通过串口发送指令，精确控制单个灯珠的颜色与亮度。
- **参数格式**: `灯号(0-7),R,G,B,亮度(0.0-1.0)`。
- **高效传输**: 采用精简的二进制协议，响应速度极快。

## 🛠️ 如何使用
1. **安装依赖**:
   ```bash
   pip install pyserial
配置串口: 打开 main.py，将 com_port 修改为你的实际端口号（如 COM21 或 /dev/ttyUSB0）。

运行:

Bash
python main.py
⚖️ 开源协议与致谢
本项目采用 GPL-3.0 协议开源。

感谢 MajdataPlay 提供的协议参考。
