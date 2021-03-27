
#!/usr/bin/env python
 
'''
                            Date: April 18, 2019
                            Editor: The One 
                            Program: country-capital user-input Q&A                             '''




'''----------------------------------PyCode----------------------------------------------------------'''

print("\n* Let's find out your knowledge about countries and their capitals *")
print("* Enter the name of a country, and guess before getting the answer back! *")

capital = {
        'Afghanistan': 'Kabul', 
        'Albania': 'Tirana', 
        'Algeria': 'Algiers', 
        'Argentina': 'Buenos Aires', 
        'Armenia': 'Yerevan', 
        'Australia': 'Canberra', 
        'Austria': 'Vienna', 
        'Azerbaijan': 'Baku', 
        'The Bahamas': 'Nassau', 
        'Bangladesh':'Dhaka', 
        'Belarus':'Minsk', 
        'Belgium':'Brussels', 
        'Belize':'Belmopan', 
        'Bhutan':'Thimphu', 
        'Brazil':'Brasilia', 
        'Bulgaria':'Sofia', 
        'Cambodia':'Phnom Penh', 
        'Canada':'Ottawa', 
        'China':'Beijing', 
        'Colombia':'Bogota', 
        'Cuba':'Havana', 
        'France':'Paris', 
        'Germany':'Berlin', 
        'Greece':'Athens', 
        'India':'New Delhi', 
        'Indonesia':'Jakarta', 
        'Iran':'Tehran', 
        'Iraq':'Baghdad', 
        'Ireland':'Dublin', 
        'Israel':'Jerusalem', 
        'Italy':'Rome', 
        'Japan':'Tokyo', 
        'South Korea':'Seoul', 
        'Malaysia':'Kuala Lumpur', 
        'Mexico':'Mexico City', 
        'Mongolia':'Ulaanbaatar', 
        'Myanmar':'Rangoon', 
        'Nepal':'Kathmandu', 
        'Philippines':'Manila',
        'Peru':'Lima',
        'Portugal':'Libson', 
        'Russia':'Moscow', 
        'Saudi Arabia':'Riyadh', 
        'South Africa':'Cape Town', 
        'Spain':'Madrid', 
        'Switzerland':'Bern', 
        'Syria':'Damascus', 
        'Thailand':'Bangkok',
        'Tibet': 'Lhasa',  
        'Turkey':'Ankara', 
        'Ukraine':'Kyiv', 
        'United Kingdom':'London', 
        'USA':'Washington D.C', 
        'Vietnam':'Hanoi', 
        'Zimbabwe':'Harare', 

}


while country: 

    country = input("\nType the country here: ")
    country = country.capitalize()
    country = country.strip()
    
    try:
        print(f"\nMr.Genius: * {capital[country]} * is the capital of {country}!\n")
        break

    except KeyError:
        print("\n* Mr.Bond, what's going through your mind? Give it a valid entry! *\n")
        break