## 1. Overview ##

f = open("movie_metadata.csv","r")
movie_list = f.read()
movie_split = movie_list.split("\n")
movie_data = []

for row in movie_split:
    movie_data.append(row.split(","))
    
print(movie_data[0:5])    

## 3. Writing Our Own Functions ##

def ExtractMovieName(movie_list):
    movie_name = []
    for movie in movie_list:
        movie_name.append(movie[0])
    return movie_name  

movie_names = ExtractMovieName(movie_data)
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(movie):
    if movie[6] == "USA":
        return True
    else:
        return False

wonder_woman_usa =  is_usa(wonder_woman)
    


## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False

def index_equals_str(input_lst,input_idx,input_str):
    if input_lst[input_idx] == input_str:
        return True
    else:
        return False

check_list = index_equals_str(input_str="USA",input_idx=6,input_lst=wonder_woman)

wonder_woman_in_color = index_equals_str(input_str="Color",input_idx=2,input_lst=wonder_woman)

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst,index,input_str,header_row=False):    
    num_elt = 0
    
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]    
    
   
    for each in input_lst:
        if each[index] == input_str:
            num_elt  =num_elt +1
    
    return num_elt
            
num_of_us_movies  = feature_counter(movie_data,6,"USA",True)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(input_lst,header_row=False):
    
    num_japn_films = feature_counter(input_lst,index=6,input_str="Japan",header_row=True)
    num_color_films =  feature_counter(input_lst,index=2,input_str="Color",header_row=True)
    num_films_in_english = feature_counter(input_lst,index=5,input_str="English",header_row=True)
    
    summary_dict = {}
    summary_dict = {'japan_films': num_japn_films,'color_films': num_color_films,'films_in_english':num_films_in_english}
    
    return summary_dict

summary = summary_statistics(movie_data)
    