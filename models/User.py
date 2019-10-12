import dateutil.parser
from models.DBase import connection

class User(object):

    def __init__(self):
        self.userID = 0
        self.user_id = 0
        self.email = "NOT SET"
        self.lastName = "NOT SET"
        self.firstName = "NOT SET"
        self.password = "NOT SET"
        self.salt = ""
        self.telephone_number = ""
        self.is_authenticated=False
        self.is_active=False
        self.is_anonymous=False 
        self.user_id=0

        # AdminLTE Components
        self.full_name = ""
        self.avatar = "#"
        self.created_at = dateutil.parser.parse("November 12, 2019")

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def get_id(self):
        return self.user_id

    def setCreds(self, email, password):
        self.email = email
        self.password = password 

    def makeUserFromCreds(self):
        try:
            c, conn = connection()
            c.execute("SELECT userid, email, lastName, firstName, password, salt FROM systemuser WHERE email='{}';".format(self.getEmail()))
            result_set = c.fetchall()
            conn.close()

            # Check the results
            if(len(result_set) == 1):
                for row in result_set:
                    self.userID = row['userid']
                    self.email = row['email']
                    self.firstName = row['firstname']
                    self.lastName = row['lastname']
                    self.user_id = chr(row['userid'])
                    realPassword = row['password']
                    self.salt = row['salt']
                    hashedPassword = hashlib.sha512(self.password+self.salt.encode('utf-8')).hexdigest()
                    if hashedPassword == realPassword:
                        self.is_authenticated = True
                        self.is_anonymous = True
                        self.is_active = True
                        return True
                    else:
                        return False
            else:
                # Something isn't right
                return False

        except Exception as e:
            return(e)

    def get(self, user_id):
        try:
            c, conn = connection()
            c.execute("SELECT userid, email, lastname, firstname, password FROM systemuser WHERE userid={};".format(int(ord(user_id))))
            result_set = c.fetchall()
            conn.close()

            # Check the results
            if(len(result_set) == 1):
                for row in result_set:
                    self.userID = row['userid']
                    self.email = row['email']
                    self.firstName = row['firstname']
                    self.lastName = row['lastname']
                    self.user_id = chr(row['userid'])
                    self.is_authenticated = True
                    self.is_anonymous = True
                    self.is_active = True
                    sys.stderr.write('User ID is: {}'.format(self.userID))
                    return self
            else:
                # Something isn't right
                return None

        except Exception as e:
            sys.stderr.write(str(e))
            return(self)

    def createUser(self):
        try:
            c, conn = connection()
            c.execute("INSERT INTO systemuser (email,lastname,firstname,password,salt) VALUES (%s,%s,%s,%s,%s);",(self.email,self.lastName,self.firstName,self.password,self.salt))
            conn.commit()
            conn.close()
            return "<p> Create Successfully </p>"
        except Exception as e:
            return str(e)


    def fetch(self, user_id):
        try:
            c, conn = connection()
            c.execute("SELECT userid, email, lastname, firstname, email, telephone_number FROM systemuser WHERE userid={};".format(int(ord(user_id))))
            result_set = c.fetchall()
            conn.close()

            # Check the results
            if(len(result_set) == 1):
                for row in result_set:
                    self.userID = row['userid']
                    self.email = row['email']
                    self.firstName = row['firstname']
                    self.lastName = row['lastname']
                    self.user_id = chr(row['userid'])
                    self.telephone_number = row['telephone_number']
                    return self
            else:
                # Something isn't right
                return None

        except Exception as e:
            sys.stderr.write(str(e))
            return(self)


    def update(self):
        try:
            c, conn = connection()
            c.execute("UPDATE systemuser SET email=%s, firstname=%s, lastname=%s, telephone_number=%s WHERE userid = %s;",(self.email,self.firstName,self.lastName,self.telephone_number,self.userID))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return False

