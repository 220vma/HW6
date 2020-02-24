def ap2():
    Str = "Help ELephant learn LOops. While's and fOrs. RLD!"
    List_upper = []
    

    for i in Str:
        if i.isupper():
            List_upper.append(i)

    List_upper = ''.join(List_upper)
    
    return List_upper
    
print(ap2())