def get_power(n):
    if(n<=1):
        return 0
    return 1+get_power(n//2)
##wrapping
def wraping(term,m):
    count =0
    for i in range(m):
        if(term[i] != 0 and term[i] !=1):
            count+=1
    if(term[0]==None):
        return (True,count)
    return (False,count)
#gray code to decimal
def convert_grav_to_dec(input):
    l=[]
    n=len(input)
    l.append(input[0])
    for i in range(1,n):
        if(l[i-1]==input[i]):
            l.append(0)
        else:
            l.append(1)
    dec =0
    x=len(input)-1
    for i in range(n):
        dec+=pow(2,x)*l[i]
        x=x-1
    return dec
############################
def get_min(input,n):

    if(n<0):
        return convert_grav_to_dec(input)
    elif(input[n]==0 or input[n]==1):
        return get_min(input,n-1)
    else:

        temp1 = []
        temp2=[]
        for i in range(len(input)):
            temp1.append(input[i])
            temp2.append(input[i])
        temp1[n]=0 
        temp2[n]=1
        return min(get_min(temp1,n-1),get_min(temp2,n-1))

def get_max(input,n):
    if(n<0):
        return convert_grav_to_dec(input)
    elif(input[n]==0 or input[n]==1):
        return get_max(input,n-1)
    else:
        temp1=[]
        temp2=[]
        for i in range(len(input)):
            temp1.append(input[i])
            temp2.append(input[i])
        temp1[n]=0 
        temp2[n]=1
        return max(get_max(temp1,n-1),get_max(temp2,n-1))





##Main function
def is_legal_region(kmap_function, term):
    top_left_x=None
    top_left_y =None
    bottom_right_x =None
    bottom_right_y =None
    islegal = True
    m = len(kmap_function)   ########           rows
    n = len(kmap_function[0])  ####       columns
    no_of_row_term = get_power(m)
    no_of_col_term = get_power(n)
    row_term=[]
    col_term=[]
    for i in range(no_of_col_term):
        col_term.append(term[i])
    for i in range(no_of_row_term):
        row_term.append(term[i+no_of_col_term])
    wrap_x = False
    wrap_y = False
    wraping_in_x = wraping(row_term,no_of_row_term)
    wraping_in_y = wraping(col_term,no_of_col_term)
#############################################################################
    if(wraping_in_x[0]==True):
        if(wraping_in_x[1]==no_of_row_term):
            top_left_x=0
            bottom_right_x=m-1

        else:
            if(get_min(row_term,no_of_row_term-1)==0):
                x = pow(2,wraping_in_x[1])
                top_left_x = m-(x//2)
                bottom_right_x= (x//2)-1
                wrap_x =True
            else:
                top_left_x = get_min(row_term,no_of_row_term-1)
                bottom_right_x = get_max(row_term,no_of_row_term-1)

        ###########
    else:
        top_left_x = get_min(row_term,no_of_row_term-1)
        bottom_right_x = get_max(row_term,no_of_row_term-1)
    ############################
    if(wraping_in_y[0]==True):
        if(wraping_in_y[1]==no_of_col_term):
            top_left_y=0
            bottom_right_y=n-1
        else:
            if(get_min(col_term,no_of_col_term-1)==0):
                x = pow(2,wraping_in_y[1])
                top_left_y = n-(x//2)
                bottom_right_y= (x//2)-1
                wrap_y=True
            else:
                top_left_y = get_min(col_term,no_of_col_term-1)
                bottom_right_y =get_max(col_term,no_of_col_term-1)
    else:
        top_left_y = get_min(col_term,no_of_col_term-1)
        bottom_right_y =get_max(col_term,no_of_col_term-1)
######################################################################################  Checking is legal
    if(wrap_x==True and wrap_y ==True):
        for i in range(m):
            if(i > bottom_right_x and i< top_left_x):
                continue
            else:              
                for j in range(n):
                    if(j > bottom_right_y and j < top_left_y):
                        continue
                    else:
                        if(kmap_function[i][j] ==0):
                            islegal =False
    elif(wrap_x==True):
        for i in range(m):
            if(i > bottom_right_x and i< top_left_x):
                continue
            else: 
                for j in range(n):
                    if(j>= top_left_y and j<= bottom_right_y):
                        if(kmap_function[i][j] ==0):
                            islegal =False
                    
    elif(wrap_y==True):
        for i in range(m):
            if(i >= top_left_x and i<= bottom_right_x): 
                for j in range(n):
                    if(j> bottom_right_y and j<top_left_y):
                        continue
                    else:
                        if(kmap_function[i][j] ==0):
                            islegal =False
    else:
        for i in range(m):
            if(i >= top_left_x and i<= bottom_right_x): 
                for j in range(n):
                    if(j>= top_left_y and j<= bottom_right_y):
                        if(kmap_function[i][j] ==0):
                            islegal =False
        
    return ((top_left_x,top_left_y),(bottom_right_x,bottom_right_y),islegal)
