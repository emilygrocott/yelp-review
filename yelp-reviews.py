import lab05_util

import webbrowser 

restaurants= lab05_util.read_yelp('yelp.txt')

def print_info(restaurant):
    name, lat, long, address, url, type_res, list_scores = restaurant
    address = address.split('+')
    street, city= address
    avg_score = sum(list_scores)/len(list_scores)
    information = ("{} ({}) \n\t{} \n\t{} \nAverage Score: {:.2f}".format(name, type_res, street, city, avg_score))
    return information

restaurant = restaurants[int(input("ID of restaurant (pick a number 1 through 155) => "))-1]
print(print_info(restaurant))
review = restaurant[-1]
if len(review) > 3:
    average_review = (sum(review)-min(review)-max(review))/len(review)
else:
    average_review = sum(review) / len(review)
    
if 0 <= average_review < 2:
    print("This restaurant is rated bad, based on {} reviews".format(len(review)))
elif 2 <= average_review < 3:
    print("This restaurant is rated average, based on {} reviews".format(len(review)))
elif 3 <= average_review < 4:
    print("This restaurant is rated above average, based on {} reviews".format(len(review)))
elif 4 <= average_review < 5:
    print("This restaurant is rated average, based on {} reviews".format(len(review)))

print("What would you like to do next? \n1. Visit the homepage\n2. Show on Google Maps\n3. Show directions to this restaurant")
user_next = input("Your choice (1-3)? ==> ")

if user_next == '1':
    webbrowser.open(restaurant[-3])
elif user_next == '2':
    url = 'http://www.google.com/maps/place/'+restaurant[3]
    webbrowser.open(url)
elif user_next == '3':
    address = input("Your address: ")
    url = 'http://www.google.com/maps/dir/'+address+'/'+restaurant[3]
    webbrowser.open(url)

    
