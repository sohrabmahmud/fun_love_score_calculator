def calculate_love_score(name1, name2):
    let_t = "T"
    let_r= "R"
    let_u = "U"
    let_e1 = "E"
    
    t_c = 0
    r_c = 0
    u_c = 0
    e1_c = 0
    
    let_l = "L"
    let_o = "O"
    let_v = "V"
    let_e2 = "E"
    
    l_c = 0
    o_c = 0
    v_c = 0
    e2_c = 0
    
    for name in list(name1 + name2):
        if name.upper() == let_t:
            t_c += 1
        if name.upper() == let_r:
            r_c += 1
        if name.upper() == let_u:
            u_c += 1
        if name.upper() == let_e1:
            e1_c += 1
            
    for name in list(name1 + name2):
        if name.upper() == let_l:
            l_c += 1
        if name.upper() == let_o:
            o_c += 1
        if name.upper() == let_v:
            v_c += 1
        if name.upper() == let_e2:
            e2_c += 1        
            
    true_occurs = str(t_c + r_c + u_c + e1_c)
    love_occurs = str(l_c + o_c + v_c + e2_c)
    
    love_score = (true_occurs + love_occurs)
    return love_score
    #print(love_score)
    
name1 = input("Enter the first name:\n")
name2 = input("Enter the second name:\n")
love_score = str(calculate_love_score(name1, name2))
print(f"The true love score between {name1} and {name2} is {love_score}")
