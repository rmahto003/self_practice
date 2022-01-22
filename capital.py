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
                    'West Bengal'       : 'Kolkata'    }



d =input('Enter State : ').title()

if d in states_capitals:
    print('capital is : ', states_capitals[d])
else:
    print('plese enter correct state')








