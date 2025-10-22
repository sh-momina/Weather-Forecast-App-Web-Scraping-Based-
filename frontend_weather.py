import streamlit as st
import pandas as pd

st.title("Asia Weather App")
countries_data = pd.read_csv("Countries data")

# england
countries_data = countries_data.drop(63)
# northern island
countries_data = countries_data.drop(152)
# scotland
countries_data = countries_data.drop(177) 
# wales
countries_data = countries_data.drop(223) 

country = st.selectbox("Choose the country",countries_data["Countries_name"])
# st.write(country)

country_index = 0
for i in countries_data["Countries_name"]:
    if i == country:
        st.write("country_index : ", country_index)
        break
    else:
        country_index += 1

cities_data = pd.read_csv("Cities data")
no_of_cities = pd.read_csv("No of cities(in each country)")

# st.write(cities_data)
# st.write(no_of_cities)

value = 0
start = 0
end = 0

for i in range(len(no_of_cities["Number_of_ities"])):
    if i == country_index:
        value = no_of_cities["Number_of_ities"][i]
        break
    else:
        start += no_of_cities["Number_of_ities"][i]

# st.write("no of cities : ",value)
# st.write("cities_before : ",start)

cities_list = []


for i in range(len(cities_data["City_name"])):
    if cities_data["City_name"][i] == cities_data["City_name"][start]:
        # st.write(cities_data["City_name"][start])
        # st.write(cities_data["City_name"][i])
        for j in range(value):
            # st.write(cities_data["City_name"][j+i])
            cities_list.append(cities_data["City_name"][j+i])
        
city_selected = st.selectbox("select the city : " ,  cities_list)

city_start = 0
days_data = pd.read_csv("Days_org_data")
# st.write(days_data)

no_of_days = pd.read_csv("No of days")
# st.write(no_of_days)

city_day = pd.read_csv("City_day")

# st.write(days_data["City_days"][57])
# days_data = days_data["City_days"].drop(57).reset_index(drop=True)


for i in range(len(cities_data["City_name"])):
    if city_selected == cities_data["City_name"][i]:
        # st.write("city index : ", i)
        city_index = i
        city_start = i*7


for i in range(len(cities_data["City_average_temp"])):
    if i == city_index:
        st.write(cities_data["City_name"][i])
        st.write("Average temp : ", cities_data["City_average_temp"][i])

# st.write("index at city day : ", city_day["City_days"][57])
# city_day = city_day.drop(61)

# st.write("###", no_of_days["no_of_days"][city_index])
day_data_count = no_of_days["no_of_days"][city_index]

for k in range(day_data_count):
    st.write(days_data["City_days"].iloc[k+city_start])
    st.write(days_data["min_temp"].iloc[k+city_start])
    st.write(days_data["max_temp"].iloc[k+city_start])

# city_day = city_day.drop(64)
# st.write(days_data)
