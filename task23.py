# Drag and Drop operation

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# ActionChain
from selenium.webdriver import ActionChains


class DragAndDrop:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait(5)

    def wait(self, secs):
        sleep(secs)

    def quit(self):
        self.driver.quit()

    def dragAndDrop(self):
        self.boot()
        self.driver.switch_to.frame(0)
        source1 = self.driver.find_element(By.ID, "draggable")
        target1 = self.driver.find_element(By.ID, "droppable")
        self.action.drag_and_drop(source1, target1).perform()
        self.wait(3)


url = "https://jqueryui.com/droppable/"
obj = DragAndDrop(url)
obj.dragAndDrop()
obj.quit()
