from onetoone import Husband, Wife, session

#We create the objects class Husband


husband1 = Husband(husband_id = 54321, husband_name='Andres',husband_lastname='Gimeno')
husband2 = Husband(husband_id = 12345, husband_name='Logan',husband_lastname='Gimeno')

session.add_all(
    [husband1,husband2]
)

session.commit()



#Lets Get Objects that we created


all_husbands = session.query(Husband).all()
print(all_husbands)
for husband in all_husbands:
    print(husband)


#Lets create a child object(Wife) related with the parent objetc (Husband)
married_husband = session.query(Husband).filter(Husband.husband_id == '54321').first()
print(married_husband)

a_wife = Wife(wife_id = 2110, wife_name = 'Someone', wife_lastname = 'Something', husband = married_husband ) #"husband" from relationship defination, equal to the object parent

session.add(a_wife)
session.commit()

print(married_husband.wife) #Show the relationship, in this case the Wife.