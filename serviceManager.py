
import time

class sessionManager():
    Global_session = 0
    def __init__(self, configTime = 5): # value in hrs
        self.configTime = configTime
        self.Global_session = 0
        self.sessionList = []
        self.sessionManagement = {}
    
    def generateSession(self, time):
        self.Global_session = self.Global_session + 1
        self.sessionManagement[self.Global_session] = time  #discuss
        return self.Global_session

    def validateSession(self, sessionKey):
        """
        check based on time limit of session less than equal 5
        session key value shouldn't be None
        session key exist in sessionList as well
        """
        currentTime = time.time()
        if self.sessionManagement[sessionKey] and currentTime - self.sessionManagement[sessionKey] <= self.configTime:
            self.sessionManagement[sessionKey] = currentTime
            return True
        else:
            self.deleteSessionTimebase(self.sessionManagement, sessionKey)
            
        return False
        
    def deleteSession(self, sessionKey):
        
        if sessionKey in self.sessionManagement:
            self.deleteSessionTimebase(self.sessionManagement, sessionKey)
            return True
        return "invalid sessionkey"
            
            
    def deleteSessionTimebase(self,sessionManagement, sessionKey):
        if sessionKey in self.sessionManagement:
            self.sessionManagement[sessionKey] = None
        else:
            return "invalid session key"
            
            
        



    
        
        

        
