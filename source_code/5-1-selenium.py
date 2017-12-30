from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# firefox plugin
# https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu

# hide browser window
chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless

# add the option when creating driver
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"网页爬虫").click()

print(driver.page_source[:200])
driver.get_screenshot_as_file("./img/sreenshot2.png")
driver.close()
print('finish')