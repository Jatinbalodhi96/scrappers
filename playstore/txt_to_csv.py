from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

cols = ['username', 'date', 'rating', 'upvotes', 'comment']
data = list()
file_name = 'whatsapp.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

jscontroller = soup.find()['jscontroller']

all_comments_divs = soup.find_all('div', {'jscontroller': jscontroller})

for comment_section in all_comments_divs:
    
    '''first get user info'''
    user_info_div = comment_section.div.div.nextSibling.div
    user_name = user_info_div.div.span.get_text()
    date = user_info_div.div.div.span.nextSibling.get_text()
    date = datetime.strptime(date, '%B %d, %Y')
    rating = user_info_div.div.div.span.div.div['aria-label']

    upvotes = user_info_div.div.nextSibling.span.span.div.getText()

    '''Second get comment text.'''
    comment = user_info_div.nextSibling.getText()
    data.append({'username' : user_name,
                 'date': date,
                 'rating': rating[6],
                 'upvotes': upvotes,
                 'comment': comment})

df = pd.DataFrame(data)
df.to_csv('{}.csv'.format('whatsapp'), encoding='utf-16', index=False, sep='\t', columns=cols)