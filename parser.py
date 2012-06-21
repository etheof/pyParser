#initial attempt using httplib2
#import httplib2
import urllib2

#web_pool = ["http://www.google.gr", "http://www.google.com/foo/bar/etc/re", "http://www.facebook.com"]

first_letter = "http://dropbox.com/dropquest2012/c"

#Letters from site
#second_letter = ['k', 'r', 'l', 'c', 't' , 'm', 'p', 'd', 's']
#third_letter = ['p', 'l', 'a', 'k', 'j', 'd']
#fourth_letter = ['s', 'a', 'k', 'r', 'd', 't', 'b',' m', 'g']

#second_letter = ['k','r','l','c','t','m','p','d','s','a','j','b','g']
second_letter = ['r']
third_letter = ['k','a']
fourth_letter = ['n', 'k']
fifth_letter = "e"


for letter in second_letter:
	seconds = first_letter + "%s" % letter
	#print seconds
	for letter in third_letter:
 		thirds =  seconds + "%s" % letter
 		#print thirds
 		for letter in fourth_letter:
 			fourths =   thirds + "%s"  % letter
 			fifths = fourths + fifth_letter
 			uri = fifths
 			print uri
 			try:
 				resp = urllib2.urlopen(uri)
 			except urllib2.URLError, e:
 				if not hasattr(e, "code"):
 					raise
 				resp = e
 			print "Gave", resp.code, resp.msg
 			print "=" * 80
 			
 			 
 			#print resp.read(80)


"""		
for uri in web_pool:
	print uri
	try:
		resp = urllib2.urlopen(uri)  
	except urllib2.URLError, e:
		if not hasattr(e, "code"):
			raise
		resp = e
	print "Gave", resp.code, resp.msg
	print "=" * 80
	print resp.read(80)
"""



#initial attempt using httplib2
#uri = fifths
#h = httplib2.Http(".cache")
#r, content = h.request("%s", "GET") % uri
#print r['status']
#print r['content-type']

#second attempt using urlib2 with direct parsing
#gh_url = '%s' % fifths
#req = urllib2.Request(gh_url)
#handler = urllib2.urlopen(req)
#print handler.getcode()