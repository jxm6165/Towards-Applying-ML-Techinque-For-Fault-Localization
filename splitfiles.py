with open("goodvec.log", "r") as f:
    i = 1
    for line in f:
        if line.strip() == "":
            continue
        output = open('/Users/jianyumao/Desktop/Linux/code2vec/GoodBlockVec/%d.vectors' % i,'w')
        output.write(line)
        output.close()
        i+=1

