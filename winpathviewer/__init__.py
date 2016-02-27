"""
winpathviewer - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'winpathviewer.schema'
    flow_module   = 'winpathviewer.flow'
    javascripts   = [
        'js/winpathviewer/routes.js',
        'js/opal/controllers/discharge.js'
    ]