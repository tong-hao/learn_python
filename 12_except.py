try:
    v = 1/1
    print("result:" + str(v))

except ValueError:
    print("遇到了ValueError错误")
except ZeroDivisionError:
    print("遇到了ZeroDivisionError错误")
except:
    print("遇到了其他错误")
else:
    print("执行没有出错！")
    