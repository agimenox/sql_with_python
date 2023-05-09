from onetoone import Husband, Wife, session

print(f'Husband: {session.query(Husband).all()}')
print(f'Wife: {session.query(Wife).all()}')

parent_to_delete = session.query(Husband).filter(Husband.husband_id == '54321').first()
print(parent_to_delete)
print(parent_to_delete.wife)

#To delete
#Like this objetc are in Cascade on Delete. both will be eliminated from the database.

session.delete(parent_to_delete)
session.commit()