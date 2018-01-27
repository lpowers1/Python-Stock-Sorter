#By: Logan Powers
#R11446104
#12-1-16

#name: get_data_list
#param: FILE_NAME <str> - the file's name you saved for the stock's prices
#brief: get a list of the stock's records' lists
#return: a list of lists <list>
def get_data_list(FILE_NAME):
    #setting up needed variables
    file_temp = open(FILE_NAME, "r")
    #transfered the data betwen 3 different files to ensure no data was lost instead of manipulating a single list, still comes out as you wanted
    list_major = []
    list_minor = []
    list_final = []
    #making the csv file into a list of lists without unnecessary parts like the "\n"s
    for x in file_temp:
        hold = x.replace("\n", "")
        list_minor.append(hold)
    for x in list_minor:
        list_major.append(x.split(','))
    #close file and return
    file_temp.close()
    return list_major
    
#name: get_monthly_averages
#param: data_list <list> - the list that you will process
#brief: get a list of the stock's monthly averages and their corresponding dates
#return: a list <list>
def get_monthly_averages(data_list):
    #Setting up variables needed in future
    monthly_averages_list = []
    #made a second list of teh same information to make calculating easier
    same_list = []
    for x in data_list:
        same_list.append(x)
    monthly_average = 0
    #deleting the begginning of the file where it has unneeded strings like "volume" and "date"
    del data_list[0]
    del same_list[0]
    conti = True
    here = 9
    years = 2008
    count = 0
    answer = 0
    sum_of_all_daily = 0
    #calculating final year to find the stopping point for the loop
    final_year = data_list[-1][0][0] + "-" + data_list[-1][0][5:]
    
    #Monthly Average Finding
    #used a while loop so after I calculate for a single month itll do the same for the rest of the months
    while (conti == True):
        #Again setting up the needed variables
        answer = 0
        sum_of_all_daily = 0
        date = data_list[0][0].split("/")
        hello = str(here) + "-" + str(years)
        month_tuple = (hello,)
        #checking to see if the dates match and putting them in proper order to compare
        for x in data_list:
            pls = x[0].split("/")
            check = pls[0] + "-" + pls[2]
            if (check == hello):
                sum_of_all_daily += float(x[1])
        for x2 in same_list:
            pls = x2[0].split("/")
            check = pls[0] + "-" + pls[2]
            if (check == hello):
                answer += (float(x2[1])*float(x2[2]))
        #creatign tuple of the date and adding it to the list
        monthly_average = answer/sum_of_all_daily
        second_tuple = (round(monthly_average,2),)
        final_tuple = month_tuple + second_tuple
        monthly_averages_list.append(final_tuple)
        #checking to see if the year needs to be decremented and also seeing if the date has gone out of the context of the file
        if (here < 2):
            years -=1
            here = 12
        else:
            here -=1
        if (hello == final_year):
            return monthly_averages_list
            conti = False
    

#name: print_info
#param: monthly_average_list <list> - the list that you will process
#brief: print the top 6 and bottom 6 months for Google stock
#return: None
def print_info(monthly_averages_list):
    #setting up needed variables and lists
    write_to = open("monthly_averages.txt", "w")
    write_to.write("6 best months for Google stock: \n")
    monthly_averages_list2 = monthly_averages_list
    save = monthly_averages_list[0][1]
    save2 = monthly_averages_list2[0][1]
    float(save)
    list_of_biggest = []
    list_of_smallest = []
    #finding best 6 months
    count = 0
    #used a while loop so that after we find the first month I can do the same for the next 5 months
    while(count < 6):
        for x in monthly_averages_list:
            hold = float(x[1])
            if (hold > save):
                save = hold
        for x in monthly_averages_list:
            if (x[1] == save):
                #printing the months to the file
                write_to.write(str(x))
                write_to.write("\n")
                monthly_averages_list.remove(x)
        list_of_biggest.append(save)
        count+=1
        save = monthly_averages_list[0][1]
        
    # using same way, finding worst 6 months
    write_to.write("6 worst months for Google stock: \n")
    count2 = 0
    while(count2 < 6):
        for x in monthly_averages_list2:
            hold = float(x[1])
            if (hold < save2):
                save2 = hold
        for x in monthly_averages_list2:
            if (x[1] == save2):
                #printing the months to the file
                write_to.write(str(x))
                write_to.write("\n")
                monthly_averages_list2.remove(x)
        list_of_smallest.append(save2)
        count2+=1
        save2 = monthly_averages_list2[0][1]
        
    # closing file
    write_to.close()

# call get_data_list function to get the data list, save the return in data_list
data_list = get_data_list("stocks.csv")
# call get_monthly_averages function with the data_list from above, save the 
# return in monthly_average_list
monthly_averages_list = get_monthly_averages(data_list)
# call print_info function with the monthly_average_list from above
print_info(monthly_averages_list)

