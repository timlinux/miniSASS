# -*- coding: utf-8 -*-
from .base import *  # noqa

# Extra installed apps
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',  # enable Raven plugin
    'tinymce',
    'cms',
    'mptt',
    'easy_thumbnails',
    'menus',
    'south',
    'sekizai',
    'cms.plugins.link',
    'cms.plugins.text',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cms.plugins.twitter',
    #'cmsplugin_blog',
    'cmsplugin_contact',
    'djangocms_utils',
    'simple_translation',
    'tagging',
    'reversion',
    'monitor',
    'cmsplugin_rssfeed',
)


AUTHENTICATION_BACKENDS = (
    'social.backends.openstreetmap.OpenStreetMapOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)



TEMPLATE_CONTEXT_PROCESSORS += (
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (

    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)



# Django CMS configuration settings
# CMS_LANGUAGES = {
#         1: [
#             {
#                 'code': 'en',
#                 'name': gettext('English'),
#                 'fallbacks': [],
#                 'public': True,
#                 'hide_untranslated': True,
#                 'redirect_on_fallback': False
#                 }
#             ],
#         'default': {
#             'fallbacks': ['en'],
#             'redirect_on_fallback': True,
#             'public': False,
#             'hide_untranslated': False
#             }
#         }

CMS_TEMPLATES = (
    ('site_page.html', 'Site Page'),
    ('map_page.html', 'Map Page'),
    ('resource_page.html', 'Resources Page'),
    ('footer_content.html', 'Footer Content Only'),
)
CMS_TEMPLATE_INHERITANCE = True

CMS_PLACEHOLDER_CONF = {
    'links': {
            'plugins': ['LinkPlugin'],
            'name': gettext("Links"),
            'limits': {
                'LinkPlugin': 10
                }
            },
    'bottom-links': {
            'plugins': ['LinkPlugin'],
            'name': gettext("Bottom of Page Links"),
            'limits': {
                'LinkPlugin': 7,
                }
            }
    }

CMS_PLUGIN_CONTEXT_PROCESSORS = []
CMS_PLUGIN_PROCESSORS = []
CMS_APPHOOKS = (
    'monitor.cms_app.MonitorApp',
    #'cmsplugin_blog.cms_app.BlogApphook'
)

PLACEHOLDER_FRONTEND_EDITING = True

CMS_UNIHANDECODE_HOST = None
CMS_UNIHANDECODE_VERSION = None
# CMS_UNIHANDECODE_DECODERS = []
# CMS_UNIHANDECODE_DEFAULT_DECODER = []

CMS_MEDIA_PATH = 'cms/'
CMS_MEDIA_ROOT = MEDIA_ROOT + CMS_MEDIA_PATH
CMS_MEDIA_URL = MEDIA_URL + CMS_MEDIA_PATH
CMS_PAGE_MEDIA_PATH = 'cms_page_media/'

CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = False
CMS_REDIRECTS = False
CMS_SOFTROOT = False

CMS_PERMISSIONS = True
CMS_RAW_ID_USERS = True
CMS_PUBLIC_FOR = 'all'

CMS_SHOW_START_DATE = False
CMS_SHOW_END_DATE = False
CMS_SEO_FIELDS = False

CMS_CACHE_DURATIONS = {
        'content': 60,
        'menus': 3600,
        'permissions': 3600
        }
CMS_CACHE_PREFIX = 'minisass-dev'
CMS_MAX_PAGE_PUBLISH_REVERSIONS = 25

# WYM Editor settings
# WYM_TOOLS
# WYM_CONTAINERS
# WYM_CLASSES
# WYM_STYLES
# WYM_STYLESHEET

# filer, easy_thumbnails settings
FILER_DEBUG = True
FILER_ENABLE_LOGGING = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# blog plugin settings
JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'

# reCAPTCHA keys for minisass.org
RECAPTCHA_PUBLIC_KEY = '6LfMquASAAAAAOHqdGSV9f_7MxgsU5apGmq6NXDh'
RECAPTCHA_PRIVATE_KEY = '6LfMquASAAAAAAFQXjSQFex-IR7tVeUAgBzAica1'

# tiny-MCE settings
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'simple',
    'relative_urls': False,
    'width': 800,
    'height': 600,
    'resize': True
}



