# import requests;

# data = requests.get('https://swapi.dev/api/people/1/').json();

# print(data['films']);

# films = data['films']

# for i in films :
#     filmsData = requests.get(i).json();
#     print(filmsData['title']);


# *args = list, **kwargs = dictionary

# def fun(*lst, **dic) : 
#     print('lst : ', lst);
#     print('dic : ', dic);
#     print("Type of *lst : ",type(lst));
#     print("Type of *dic : ",type(dic));

# fun(1,2,3,4,name='Aman', Age='21');

# person = {
#     'name' : 'Aman', 
#     'age' : 15,
#     'value' : 'vada Pav'
# }

# print(person.get('age'))

