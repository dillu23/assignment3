import urllib2, re,sys

#proxy=urllib2.ProxyHandler({'http':'10.10.78.21:3128'})
#opener=urllib2.build_opener(proxy)
#urllib2.install_opener(opener)
#feed=urllib2.urlopen('http://10.22.4.33/csp301')
file=open('text.txt','r')

#file.write(feed.read())
#print feed.read()
#file.close()

regex = r'''</?a((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>\w+<\/a>'''
pattern = re.compile(regex)

links = re.findall(pattern, file.read())
print links
file.close()
