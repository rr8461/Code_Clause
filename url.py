import pyshorteners as shr   #pip install pyshorteners

shortener=shr.Shortener()
URL=input("Enter Url: ") 
shorturl=shortener.tinyurl.short(URL)
print (f'Short URL is {shorturl}')