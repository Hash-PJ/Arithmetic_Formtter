def arithmetic_arranger(problems, arg2=False):
    if len(problems)>5:
        return "Error: Too many problems."
    line1 = [prob.split(' ')[0] for prob in problems]
    oper = [prob.split(' ')[1] for prob in problems]
    line2 = [prob.split(' ')[2] for prob in problems]

    if ('*' in oper or '/' in oper):
        return "Error: Operator must be '+' or '-'."
    else:
        oper = [o+' ' for o in oper]
    spaces = ' '*4
    max_len = ['']*len(problems)
    for i in range(len(problems)):
        max_len[i] = max([len(line1[i]), len(line2[i])])
        if max_len[i]>4:
            return "Error: Numbers cannot be more than four digits."
    
    line1 = spaces.join([line1[i].rjust(max_len[i]+2) for i in range(len(max_len))])+'\n'
    line2 = spaces.join([oper[i]+line2[i].rjust(max_len[i]) for i in range(len(max_len))])+'\n'
    line3 = spaces.join(['-'*(i+2) for i in max_len])
    try:
        ans = '\n'+spaces.join([str(eval(problems[i])).rjust(max_len[i]+2) for i in range(len(max_len))])
    except:
        return "Error: Numbers must only contain digits."
    if arg2:
        return line1+line2+line3+ans
    return line1+line2+line3