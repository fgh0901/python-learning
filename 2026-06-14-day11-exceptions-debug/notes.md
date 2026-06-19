对于python的异常处理，首先，try中存放的是可能会抛出异常的代码块
对于我们希望出现某种错误主动抛出异常的部分，可以使用raise Exception（），括号中的参数可以是一个字符串，表示异常信息是什么，便于在后续中通过except接收到后打印错误信息
通过except Exception as e来将抛出的异常进行捕获，并且赋值为e

除了自定义抛出的一场，还有系统异常，except ZeroDivisionError as e，同样可以通过捕获来进行操作

对于else模块，如果不报错，没有进入except会进入else模块，是可选的

finally:#无论如何都会执行的模块