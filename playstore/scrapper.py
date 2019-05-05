from selenium import webdriver
import time


app_url = 'https://play.google.com/store/apps/details?id=com.whatsapp&showAllReviews=true'
jquery_path = 'jquery-3.3.1.min.js'
next_pages_limit = 10000
app_name = 'whatsapp'
progress = 0

driver = webdriver.Chrome()
driver.get(app_url)


with open(jquery_path) as jquery:
    jquery = jquery.read()
    driver.execute_script(jquery)

    for i in range(1, next_pages_limit + 1):
        time.sleep(2)
        try:
            show_more = driver.find_element_by_xpath("//*[contains(text(), 'Show More')]")
            show_more.click()
        except Exception as e:
            pass
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        user_reviews = driver.find_element_by_xpath("//*[contains(text(), 'User reviews')]/following-sibling::div")
        
        '''In future update progress messages in database for UI purposes.'''
        progress = round((i / next_pages_limit) * 100, 2)
        print(progress)

        '''Save data on every number of progress call.'''
        # if (i % 10 == 0):
        #     with open('{0}.txt'.format(app_name), 'w', encoding='utf-8') as f:
        #         f.write(user_reviews.get_attribute('innerHTML'))
    with open('{0}.txt'.format(app_name), 'w', encoding='utf-16') as f:
        f.write(user_reviews.get_attribute('innerHTML'))

    f.close()
    driver.close()

    print('{0} app comment data is saved to {0}.txt'.format(app_name))
