
# littlePyTools

Some Little Python Tools

## Pyinstaller 打包

- 用法举例

```shell
lvin

pyinstaller -F -w .\ctrlTuyaPlug\ctrlTuyaPlug.py

deactivate
```

说明：

  -F：打包成单独的EXE文件
  -w：运行时不要弹出console窗口

## 在Windows下布置周期性任务

```shell
schtasks.exe /create /sc minute /mo 10 /tn "断电防过" /tr "D:\Prj\littlePyTools\dist\ctrlTuyaPlug.exe"
```

说明：

  /create ： 创建任务
  /sc     ： /SC  schedule，指定计划频率。有效计划任务:  MINUTE、 HOURLY、DAILY、WEEKLY、MONTHLY, ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.
  /mo     ： 改进计划类型以允许更好地控制计划重复周期。有效值列于下面“修改者”部分中。
  /tn     ： 指定 TASK 名称
  /tr     ： 指定 TASK 执行路径full path.