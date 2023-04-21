import selenium.webdriver as webdriver

def GetResultMethod(search_term):
    url = "https://www.startpage.com/"
    browser = webdriver.Chrome()
    browser.get(url)
    searchBox = browser.find_element_by_id("q")
    searchBox.send_keys(search_term)
    searchBox.submit()
    try:
        links = browser.find_elements_by.xpath("/ol[@class='web_regular_result']//a/h3")
    except:
        links = browser.find_elements_by.xpath("//a/h3")
    result = []
    for link in links:
        href = link.get_attribute("href")
        print(href)
        result.append(href)
    browser.close()
    return result
GetResultMethod("Dog")