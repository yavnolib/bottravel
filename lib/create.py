class Create_user:
        def __init__(self,id):
                self.user_id=str(id)
        def create(self):
                already=0
                r=open('users.txt',mode='r')
                bylo=''
                for line in r:
                        if self.user_id in line:
                                r.close()
                                return(0)
                        bylo+=line

                r.close()

                bylo=bylo+'\n'+self.user_id+':'
                w=open('users.txt',mode='w')
                w.write(bylo)
class Create_feedback:
        def __init__(self,id,msg):
                self.user_id=str(id)
                self.msg=msg
        def create(self):
                already=0
                r=open('feedback.txt',mode='r')
                bylo=''
                for line in r:

                        bylo+=line

                r.close()

                bylo=bylo+'\n'+str(self.user_id)+':'+self.msg
                w=open('feedback.txt',mode='w')
                w.write(bylo)

#Create_user('').create()
