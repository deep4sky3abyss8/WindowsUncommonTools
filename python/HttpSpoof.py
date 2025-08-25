#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# The SpoofHttpRequest class is designed to generate spoofed HTTP requests with headers that closely mimic those 
# sent by real browsers (Chrome and Firefox) on different operating systems (Windows and Android).

# The main purpose of this class is to create HTTP requests that appear to originate from genuine browsers, which 
# can be useful in scenarios such as web server testing, analyzing server behavior based on client headers, or bypassing 
# simple HTTP header-based restrictions.

# Features:
# - Intelligent selection of User-Agent header based on the chosen platform (Android or Windows)
# - Construction of standard headers typically used by Chrome and Firefox browsers
# - Support for common HTTP methods GET and HEAD
# - Option to specify connection type (keep-alive or close)
# - Produces a complete, well-formed HTTP request string ready to be sent directly to the server

# Note: This class is suitable for basic request spoofing and may require further customization for more advanced or 
# specific use cases.

#   _________________________________________________________

#   Usage Exp :
#   
#   req = SpoofHttpRequest( url , ClientOS , GET/HEAD )          -> can use obj params .
#   req = req.spoof()
# 
#   req = SpoofHttpRequest( url , ClientOS ).spoof()  -> one use of spoofed obj 

#   _________________________________________________________
#
#   HTTP Request sample from Chrome on windows 
#   _________________________________________________________
#
#   GET / HTTP/1.1\r\n
#   self.host: example.com\r\n
#   Connection: keep-alive\r\n
#   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Safari/537.36\r\n
#   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
#   Accept-Encoding: gzip, deflate, br\r\n
#   Accept-Language: en-US,en;q=0.9\r\n
#   Upgrade-Insecure-Requests: 1\r\n   
#   Sec-Fetch-Dest: document\r\n       
#   Sec-Fetch-Mode: navigate\r\n       
#   Sec-Fetch-Site: none\r\n           
#   Sec-Fetch-User: ?1\r\n
#   Cache-Control: max-age=0\r\n
#   \r\n
#   _________________________________________________________

from random import randint , choice
from urllib.parse import urlparse
#   _________________________________________________________

class SpoofHttpRequest :
    
    
    def __init__(self, url="google.com", platform="android" , method=None, conn_type="keep-alive", allow_encode=False ) :
        

        self.url        = url
        self.platform   = platform
        self.path       = urlparse(self.url).path
        self.host       = urlparse(self.url).netloc
        self.scheme     = urlparse(self.url).scheme
        
        
        self.browser    = "Chrome"
        self.method     = "HEAD" if method=="HEAD" else "GET" 
        self.connection = "keep-alive" if conn_type=="keep-alive" else "close"

        
        if allow_encode :
            self.encode = True
        
        if not self.path :                              #----> checking root of site self.path
            self.path = '/'
    #_________________________________________________________
    
    def __spoofUserAgent__(self) :                      #----------> spoofing random user-agent for req : 2 browser and 
        
        user_agent = {
            # firefox
            '0': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",    #----> windows
            '1': "Mozilla/5.0 (Android 13; Mobile; rv:138.0) Gecko/138.0 Firefox/138.0",                #----> android
            # chrome
            '2': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Safari/537.36",        #----> windows
            '3': "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Mobile Safari/537.36"   #----> android
        }
        User = "User-Agent: "
        
        if "android" in self.platform.lower() :
            
            ch = choice(('1','3'))
            if ch=="1" : self.browser = "Firefox"
            User += user_agent[ch]
            
        else :
            ch = choice(('0','2'))
            if ch=="0" : self.browser = "Firefox"
            User += user_agent[ch]
            
        User += "\r\n"
        
        return User
    #_________________________________________________________
    
    def __spoofAccept__(self) :
        
        if self.browser == "Firefox" :
            # ---> sometimes web servers have problem in sending [ image/apng ] to Firefox ...
            return "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"  
        # else if browser was Chrome ...
        return "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n"
    #_________________________________________________________
    
    def spoof(self) : # -> str
        
        # Spoofing HTTP HEAD req ... 
        req = f"{self.method} {self.path} HTTP/1.1\r\n"                 # ----> HEAD req to self.path
        req += f"Host: {self.host}\r\n"                                 # ----> adding self.host to resolve req
        
        req += self.__spoofUserAgent__()                                # ----> User-Agent & browser spoofing
        req += self.__spoofAccept__()                                   # ----> accepting types
        
        req += f"Connection: {self.connection}\r\n"                     # ----> keep connection open and let page think script is a real user
        
        
        if self.encode : req += "Accept-Encoding: gzip, deflate\r\n"    # ----> file compressing formats for client -> if use this must decode gzip or other .
        
        
        req += "Accept-Language: en-US,en;q=0.9\r\n"                    # ----> languages which client prefer
        req += "Upgrade-Insecure-Requests: 1\r\n"                       # ----> upgrade http to https !
        
        if self.browser != "Firefox" :
            req += "Sec-Fetch-Dest: document\r\n"       
            req += "Sec-Fetch-Mode: navigate\r\n"
            req += "Sec-Fetch-Site: none\r\n"
            req += "Sec-Fetch-User: ?1\r\n"
        
        req += "Cache-Control: max-age=0\r\n"                           #-----> clear system cache
        if self.browser=="Firefox" : req += "Pragma: no-cache\r\n"      #-----> firefox old version header
        
        req += "\r\n"                                                   # ----> End of request
        
        return req
    
    #_________________________________________________________
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$