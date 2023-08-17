import time
from datetime import datetime
from datetime import date
countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()

print("--------------------")
print("|                  |")
print("|     Countries    |")
print("|        of        |")
print("|      Africa      |")
print("|                  |")
print("--------------------")
print("")

#complete the code here....
score = 0
lives = 3

lastscore = (input('would you like to knwo what your last score was? y/n: '))


    


if lastscore == 'y':
    with open ('saved scores', 'r' ) as savedscores:
        print(savedscores.read())


print(f'Number of countries is: {len(countries)}')

print(f'your score is:{score}')





#function to check if the country is not in the list and keeps the score the same


while len(countries) > 0:
   

    


    

#while loop constantly checks if the length of the list countries is over 0 meaning every country has been guessed
    country = str(input('Enter the name of a country:'))
    #prompts you to type in the country and stores it into a variable so we can see what is inside that variable

    #store the lenght of countries into a variable so we can easily gain accesss to how many countries there are in the list 


    if country not in countries and country != 'quit':
        
        lives = lives - 1
        print(f'you have lost 1 life you are now on {lives} lives')
        time.sleep(1)
        print(f'not quite, your score is still {score}')
        
    if lives == 0:
        print('you are out')
        time.sleep(1)
        quit()



            

    

        



    if country in countries:
        noofcountries = len(countries)
        print('you guessed ' + country)
        countries.remove(country)
        time.sleep(1)
        print(f'you have {noofcountries - 1 } countries left to guess')
        score = score + 1
        
        time.sleep(1)
        print(f'your score is now {score}')
    #if statement to see if the input is in the list so if it is it adds to the score and removes from the list 
    
    
    
    if country == 'quit' or lives == 0:

        print(f'your score was {score}')
        #prints the score
        time.sleep(2)
        save = input('would you like to save your score Y/N: ')
        #prompts you to save your score if you would like 
        
        
        if save == 'n':
            print('thank you for playing!')
            time.sleep(5)
            quit()
        
        if save == 'y':
            with open('saved scores', 'w') as savedscores:
             
                score = str(score)
                savedscores.write(f'your score was {score} at {current_time} on {today}')
            saved = f'(your score was {score} at {current_time} on {today})'
            print(f'saving as: {saved}')
        #if statement where if you said yes it would save your score and the current time and date of the score in a seperate file
            print('saving...')
            time.sleep(5)
            quit()
        
     
    

        

     

