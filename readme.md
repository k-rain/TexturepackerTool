#### 使用步骤:

1. 运行**TexturePacker打单图工具.exe**
2. 键入或选择输入输出路径
          输入路径: 存放小图的文件夹
          输出路径: 打出的plist存放的文件夹
3. 点击开始合图

#### 其他:

1. 没有config.js工具也能正常使用

2. 输入框内默认路径可通过工具根目录下config.js修改

3. 使用绝对路径, 是方便工具打别的图, 而不是只适用打我们项目的图

4. 重新打包命令:

   ```bash
   pyinstaller -F -w -i rain.ico TexturePackerTool_single.py
   ```

   

