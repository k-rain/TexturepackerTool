#### 使用步骤:

1. 运行**TexturePackerTool_single.exe**
2. 键入或选择输入输出路径
          输入路径: 存放小图的文件夹
          输出路径: 打出的plist存放的文件夹
3. 点击开始合图

#### 其他:

1. 没有config.js, 工具也能正常使用

2. 输入框内默认路径可通过config.js修改

3. 工具使用绝对路径, 放哪里都能用

4. 重新打包:

   脚本与ui都在DGZ-A\client\Tools\TexturePackerTool_single文件夹下, 打包命令:
   
   ```bash
   pyinstaller -w -i rain.ico -F TexturePackerTool_single.py
   ```
   
   

