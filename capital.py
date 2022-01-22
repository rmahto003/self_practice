# states and capitals
states_capitals = { 'Andra Pradesh'     : 'Amaravati' ,
                    'Arunachal Pradesh' : 'Itanagar' ,
                    'Assan'             : 'Dispur' ,
                    'Bihar'             : 'Patna' ,
                    'Chhatisgarh'       : 'Raipur' ,
                    'Goa'               : 'Panji' ,
                    'Gujrat'            : 'Gandhinagar' ,
                    'Haryana'           : 'Chandigarh' ,
                    'Himachal Pradesh'  : 'Shimla' ,
                    'Jharkhand'         : 'Ranchi' ,
                    'Karnataka'         : 'Benguluru' ,
                    'Kerala'            : 'Thiruvanthapuram' ,
                    'Madhya Pradesh'    : 'Bhopal' ,
                    'Maharashtra'       : 'Mumbai' ,
                    'Manipur'           : 'Imphal' ,
                    'Meghalaya'         : 'Shilong' ,
                    'Mizoram'           : 'Aizwal' ,
                    'Nagaland'          : 'Kohima' ,
                    'Odisha'            : 'Bhubaneswar' ,
                    'Punjab'            : 'Chandigarh' ,
                    'Rajasthan'         : 'Jaipur' ,
                    'Sikkim'            : 'Gangtok' ,
                    'Tamil Nadu'        : 'Chennai' ,
                    'Telangana'         : 'Hydrabad' ,
                    'Tripura'           : 'Agartala' ,
                    'Uttar Pradesh'     : 'Lucknow' ,
                    'Uttarakhand'       : 'Dehradun' ,
                    'West Bengal'       : 'Kolkata'    
                    }


print("What do you want to do ?")
option = int(input("Search capital (press 1) \nSearch State (Press 2) \nEnter your choice : "))

if option == 1:
    d =input('Enter State : ')
    if d.title() in states_capitals:
        print('capital is : ', states_capitals[d])
    else:
        print('plese enter correct state')
        
if option == 2:
    city = input("Enter a city name : ")

    result = ''

    for k,v in states_capitals.items():
        if v.lower() == city.lower():
            result = k
            break
        else:
            result = ''

    if len(result)==0:
        print(city, " is not in the list of State Capitals")
    else:
        print(city.title(), " is capital of ", result)
