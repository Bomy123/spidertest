import urllib.request
opener = urllib.request.build_opener()
path = "https://www.qiushibaike.com/"
user_agent = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063")
opener.addheaders = [user_agent]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(path,"./糗事百科.txt")
