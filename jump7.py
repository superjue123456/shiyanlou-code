for t in range(1,101):
    if t%7 == 0 or t%10 == 7 or int(t/10) == 7:
        continue
    else:
        print(t)
