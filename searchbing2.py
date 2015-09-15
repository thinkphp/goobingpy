import urllib2
import json

class Bing:

      def __init__( self, keyBing, searchString):

          self.credentialBing = 'Basic ' + (':%s' % keyBing).encode('base64')[:-1] 

          searchString = '%27' + searchString + '%27'

          top = 20

          offset = 0

          q = 'Query=%s&$top=%d&$skip=%d&$format=json' % (searchString, top, offset)

          self.url = 'https://api.datamarket.azure.com/Bing/Search/Web?'+ q

      def search( self ):

          request = urllib2.Request( self.url )

          request.add_header('Authorization', self.credentialBing )

          requestOpener = urllib2.build_opener()

          response = requestOpener.open( request ) 

          self.results = json.load( response )

          return self.results; 

      def get_html( self ):          

          tracks = self.results['d']['results']

          out = '<div class="yui-u first" id="google"><h2>Bing</h2><ul>'

          for item in tracks:

              desc = item['Url'] or None

              out += '<li><h3><a href="'+ item['Url'] +'">'+ item['Url'] +'</a></h3><p>'+ desc +'</p></li>'

          out += '</ul></div>'

          return out



#appID = 'Hko5cXg5U8h/WIE46pYQjmo/MLXNNkXYr+VXx/a66Ig' #get your AppID from Microsoft Azure

#bing = Bing(appID, 'mootools')

#bing.search();

#print bing.get_html()
  
