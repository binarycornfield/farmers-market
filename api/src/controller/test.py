import account_controller as account
# Example Usage:
data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'johndoe@exampel.com',
    'password': 'securepassword'
}
new_user = account.create_user(data)
print(new_user.user_id)

# user1 = User(first_name="John", last_name="Doe", email="johndoe@example.com", password="securepassword")
# user1.create()
# print(user1.user_id)  # Newly created user ID

# fetched_user = User(user_id=user1.user_id)
# print(fetched_user.find_one())

# all_users = User().find_all()
# print(all_users)

# user1.delete()  # Deleting the user by ID only