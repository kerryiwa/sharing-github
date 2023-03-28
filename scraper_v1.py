import pandas as pd
urls = pd.read_xml('https://schema.org/docs/sitemap.xml')
urls.head()