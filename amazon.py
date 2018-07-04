import selenium.webdriver as webdriver

def get_result(search_term):
    url='https://www.amazon.in/'
    browser=webdriver.Chrome()
    browser.get(url)
    search_box=browser.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(search_term)
    search_box.submit()
    links=browser.find_element_by_xpath("//h2//a")
    results=[]
    for i in links:
        href = i.get_attribute("href")
        print(href)
        results.append(href)
    browser.close()
    return results
get_result("sony xperia r1 plus")
