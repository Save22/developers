from __future__ import unicode_literals

AUTHOR = 'edgepi'
SITENAME = 'Edge Price Intelligence Developement Blog'
TAGLINE = 'Development blog'
#USER_LOGO_URL = ''
SITEURL = 'http://developers.edgepi.com'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'
SUMMARY_MAX_LENGTH = (50)

GITHUB_URL = 'https://github.com/bobftw/developers'
#DISQUS_SITENAME = ''
#GOOGLE_ANALYTICS = ''

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

#SOCIAL = (
#    ('email', 'mailto:lebrun.matt@gmail.com'),
#)
#TWITTER_USERNAME = ''

THEME = 'themes/SoMA2'
TIMEZONE = 'Asia/Manila'
DEFAULT_PAGINATION = 5

MARKUP = (('md', 'rst'))
MD_EXTENSIONS = (['codehilite', 'extra'])

