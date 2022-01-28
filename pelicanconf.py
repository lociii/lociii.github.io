AUTHOR = 'Jens'
SITENAME = 'Rants about tech, games and stuff'
SITEURL = ''

THEME = 'nest'
PLUGIN_PATHS = ['plugins']

PATH = 'content'
ROBOTS = "index, follow"
USE_FOLDER_AS_CATEGORY = False
TYPOGRIFY = True
TIMEZONE = 'Europe/Berlin'

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Main'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# nest theme
NEST_CSS_MINIFY = True
NEST_REL_CANONICAL_LINK = True
NEST_HEADER_LOGO = '/images/myrmidons.png'
NEST_HEADER_IMAGES = 'header.jpg'

# nest theme - header
NEST_INDEX_CONTENT_TITLE = "Rants"
NEST_INDEX_HEAD_TITLE = 'Homepage'
NEST_INDEX_HEADER_TITLE = 'Rants about tech, games and stuff'
NEST_INDEX_HEADER_SUBTITLE = ''
NEST_INDEX_SHOW_EXCERPT = True

# nest theme - article
NEST_ARTICLE_HEADER_BY = 'Written by '
NEST_ARTICLE_HEADER_CREATED = 'on  '
NEST_ARTICLE_HEADER_MODIFIED = 'last modified on '
NEST_ARTICLE_HEADER_IN = 'Filed under: '

# nest theme - footer
NEST_SITEMAP_COLUMN_TITLE = 'Sitemap'
NEST_SITEMAP_MENU = [
    ('CV', '/pages/cv.html'),
    ('About me', '/pages/about.html'),
    ('Legal', '/pages/legal.html'),
    ('Privacy policy', '/pages/privacy.html'),
]

NEST_SOCIAL_COLUMN_TITLE = 'Social'
SOCIAL = (
    ('Twitter', 'https://twitter.com/lociii'),
    ('GitHub', 'https://github.com/lociii'),
)

# nest theme - pagination
DEFAULT_PAGINATION = 5
NEST_PAGINATION_PREVIOUS = 'Previous rants'
NEST_PAGINATION_NEXT = 'Next rants'
