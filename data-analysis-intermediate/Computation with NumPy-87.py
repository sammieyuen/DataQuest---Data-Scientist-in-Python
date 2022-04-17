## 2. Array Comparisons ##

countries_canada = world_alcohol[:,2] == "Canada"
years_1984 = world_alcohol[:,0]=="1984"


## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:,2] =="Algeria"
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2]=="Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

vector = numpy.array([5,10,15,20])

eqal_to_ten_and_five = (vector[1] == 10)|(vector[1] == 5)
vector2 = vector[eqal_to_ten_and_five]

## 5. Replacing Values ##

year_1986 = world_alcohol[:,0] == '1986'
world_alcohol[year_1986,0] = '2014'

wine_type = world_alcohol[:,3] =='Wine'
world_alcohol[wine_type,3] = 'Grog'


## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] ==''
world_alcohol[is_value_empty,4]=0

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alalcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

matrix = numpy.array([[5,10,15],[20,25,30],[35,40,45]])
print(matrix.sum(axis=1).sum(axis=0))

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,0]=='1986') & (world_alcohol[:,2] =='Canada' )
print(is_canada_1986)
canada_1986 = world_alcohol[is_canada_1986,:]
print(canada_1986)
is_value_empty = canada_1986[:,4] == ''
canada_1986[is_value_empty,4] = "0"
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
#print(countries)
all_1989 = world_alcohol[:,0] == '1989'
alcohol_1989 = world_alcohol[all_1989,:]
#print(alcohol_1989)

for country in countries:
    is_country = alcohol_1989[:,2] == country    
    country_consumption = alcohol_1989[is_country,4]    
    is_empty = country_consumption == ''
    country_consumption[is_empty]='0'
    #print(is_empty)
    country_consumption = country_consumption.astype(float)
    #print(country_consumption)
    totals[country] = country_consumption.sum()
print(totals)    
    
        
    
    
    

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None

for k,v in totals.items():
    print(k,v)
    if  v > highest_value :
        highest_value = v
        highest_key = k    
        
    