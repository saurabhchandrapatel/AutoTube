GIT_HUB = [

'https://raw.githubusercontent.com/django/django/main/README.rst',


]
target_url = 'https://raw.githubusercontent.com/django/django/main/README.rst'
import urllib2  # the lib that handles the url stuff

data = urllib2.urlopen(target_url).read(20000)
data = data.split("\n") 