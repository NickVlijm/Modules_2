from My_Modules import Functions

mytekst = open("names.txt","rt");

for regel in mytekst:
    print(Functions.sanitize(regel))

for lijst in mytekst:
        print(Functions.create_person(lijst))

persons = []
for regel in open("names.txt", 'rt'):
    lst = Functions.sanitize(regel)
    person = Functions.create_person(lst)
    person = Functions.add_fullname(person)
    persons.append(person)

Functions.print_persons(persons)