from dbhelper import DBHelper
def main():
    db = DBHelper()
    while True:
        print("********WELCOME********")
        print("PRESS 1 to Insert new user")
        print("PRESS 2 to Display all user")
        print("PRESS 3 to Delete user")
        print("PRESS 4 to Update user")
        print("PRESS 5 to Exit program")
        try:
            choice = int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter user id: "))
                username=input("Enter user name: ")
                userphone=input("Enter user phone: ")
                db.insert_user(uid,username,userphone)
                
            elif choice == 2:
                #display user
                db.fetch_all()
                
            elif choice == 3:
                #delete user
                userid=int(input("enter user id to which you want to delete"))
                db.delete_user(userid)
                
            elif choice == 4:
                #update user
                uid=int(input("Enter id of user: "))
                newName=input("Enter New name: ")
                newPhone=input("Enter New phone: ")
                db.update_user(uid, newName, newPhone)
            elif choice == 5:
                break
            else:
                print("Invalid Input ! Try Again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try Again")



if __name__ == "__main__":
    main()

































"""
    
    # def fetch_one(self, userid):
        
    #     query = "select * from user where userId = %s"
    #     cur = self.con.cursor()
        
    #     cur.execute(query, (userid,))
    #     row = cur.fetchone()
        
    #     if row:
    #         print("User Id:", row[0])
    #         print("User Name:", row[1])
    #         print("Phone:", row[2])
    #     else:
    #         print("User not found")
            

    
#main coding
helper = DBHellper()
# helper.insert_user(1453, "Aniket", "2345678")
# helper.insert_user(1454, "Akit", "2345679")
# helper.insert_user(1455, "Abay", "2345670")
# helper.insert_user(1456, "Ashutosh", "2345671")
# helper.fetch_all()
# helper.fetch_one(1453)
# helper.delete_user(1455)
helper.update_user(1453, 'Anshul', '2345675')
helper.fetch_all()
"""