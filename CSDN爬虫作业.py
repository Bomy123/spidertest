import re
import urllib.request
import time
PATH_HOME = "D:/pythonwork/"
CSDN_HOME = "http://blog.csdn.net"
bad_url_dict = {}
def writefile(path,content):
    f = open(path,"w")
    f.write(content)
    f.close
    
def writefileinline(path,lines:str):
    with open(path,"a+") as f:
        for line in lines:
            f.write(line)
            f.write("\n")
        f.close
        
def readfile(path):
    with open(path,"r") as f:
        return f.read().decode("utf-8")
    
def readfileinline(path) -> str:
    return f.readlines()

def readurl(url):
    return urllib.request.urlopen(url,timeout=10)

def geturlindata(data:str):
    rst_d = {}
    pat_csdn = "<h3.*?</h3>"
    pat_csdn_title = '_blank">(.*?)</a></h3>'
    pat_csdn_url = "http://blog.csdn.net/.*?/article/details/\d+"
    datalist = re.compile(pat_csdn).findall(data)
    for line in datalist:
        title = re.compile(pat_csdn_title).findall(line)
        #print(title)
        url = re.compile(pat_csdn_url).findall(line)
        rst_d[url[0]] = title[0]
    return rst_d
netfile = readurl(CSDN_HOME)
#print(netfile.info())
data = netfile.read().decode("utf-8")
writefile(PATH_HOME+"rst/csdnhomepage.html",data)
url_dict = geturlindata(data)
try:
    for key in url_dict:
        try:
            time.sleep(1)
            #print(key)
            netfile = readurl(key)
            if netfile.getcode() == 200:
                print(netfile.getcode())
                data = netfile.read().decode("utf-8")
                writefile(PATH_HOME+"rst/"+url_dict[key],data)
            else:
                bad_url_dict[key] = url_dict[key]
            
        except Exception as e:
            bad_url_dict[key] = url_dict[key]
    print(bad_url_dict)
    url_dict = bad_url_dict
    for key in bad_url_dict:
        try:
            time.sleep(5)
            print(key)
            netfile = readurl(key)
            data = netfile.read().decode("utf-8")
            writefile(PATH_HOME+"rst/"+url_dict[key],data)
        except Exception as e:
            print(e.__str__())
except Exception as e:
    print(e.__str__())


