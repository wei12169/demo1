def cn_weekday(weekId):
    weekStr="一二三四五六日"
    return "星期"+weekStr[weekId-1]

weekId = int(input("今天星期几？\n"))
print(cn_weekday(weekId))
