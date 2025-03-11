class UserSystem:
    def __init__(self):
        self.users = {}
        self.logged_in_users = {}
        self.failed_attempts = {}
    
    def register_user(self, username, password, email, full_name):
        if username in self.users:
            print("Error: Username already exists")
            return False
        
        if len(password) < 8:
            print("Error: Password must be at least 8 characters")
            return False
        

        user_data = {
            "username": username,
            "password": password, 
            "email": email,
            "full_name": full_name,
            "created_at": "2023-01-01", 
            "is_active": True
        }
        
        self.users[username] = user_data
        print("User registration successful")
        
  
        print("Sending welcome email to " + email)

        return True
    
    def login(self, username, password):
        if username not in self.users:
            print("Error: User not found")

            if username in self.failed_attempts:
                self.failed_attempts[username] += 1
            else:
                self.failed_attempts[username] = 1
            
            return False
        
        user = self.users[username]
        
        if user["password"] != password:
            print("Error: Incorrect password")
            
            if username in self.failed_attempts:
                self.failed_attempts[username] += 1
            else:
                self.failed_attempts[username] = 1
            
        
            if self.failed_attempts[username] >= 3:
                print("Account locked due to too many failed attempts")
                user["is_active"] = False
            
            return False
        
        if not user["is_active"]:
            print("Error: Account is locked")
            return False
        
        self.logged_in_users[username] = True
        print("Login successful")
       
        if username in self.failed_attempts:
            self.failed_attempts[username] = 0
        
  
        user["last_login"] = "2023-01-02" 
        
        return True
    
    def logout(self, username):
        if username not in self.logged_in_users:
            print("Error: User not logged in")
            return False
        
        del self.logged_in_users[username]
        print("Logout successful")
        return True
    
    def reset_password(self, username, old_password, new_password):
        if username not in self.users:
            print("Error: User not found")
            return False
        
        user = self.users[username]
        
        if user["password"] != old_password:
            print("Error: Incorrect password")
            return False
        
        if len(new_password) < 8:
            print("Error: New password must be at least 8 characters")
            return False
        
        user["password"] = new_password
        print("Password reset successful")
        

        print("Sending confirmation email to " + user["email"])
        
        return True