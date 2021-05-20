from GoogleNews import GoogleNews
googlenews = GoogleNews()

'''
googlenews.set_lang('en')
googlenews.set_period('7d')
googlenews.set_time_range('02/01/2020','02/28/2020')
googlenews.set_encode('utf-8')
'''

googlenews.search("Apple")
googlenews.getpage(1)
googlenews.result()
print(googlenews.gettext())
