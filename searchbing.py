import urllib
import urllib2
import json
import requests

class Bing:

      ENDPOINT = 'http://api.bing.net/format.aspx'
      #ENDPOINT = 'http://api.search.live.net/json.aspx'

      def __init__(self, appid, format='json'):

          self.appid = appid
          self.format = format

      def search(self,**params):
 
          self.ENDPOINT = self.ENDPOINT.replace('format',self.format)

          data = {}

          for k,v in params.items():

              data.update({k.replace('_','.'):v.replace(' ','+')})

          qs = urllib.urlencode(data).replace('%2B','+')

          url = '%s?Appid=%s&%s' % (self.ENDPOINT, self.appid, qs) 

          f = urllib2.urlopen(url)
   
          if self.format == 'json':
             try:  
               print f.read()
               self.res = json.loads(f.read())
               #return self.res  

             except IOError:
               return "Cannot Open URL"

      def get_html(self):          
          tracks = self.res['SearchResponse']['Web']['Results']
          out = '<ul>'
          for track in tracks: 
              out += '';
          out += '<ul>'
          return tracks[2]


#bing = Bing('49EB4B94127F7C7836C96DEB3F2CD8A6D12BDB71')

#bing.search(query='jquery',sources='web')

#print bing.get_html()


