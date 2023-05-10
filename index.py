from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import unittest



class TestTitle(unittest.TestCase):
    
    def setUp(self):
        # Start the browser
        self.driver = webdriver.Firefox()
        
    def test_title(self):
        # Navigate to the Pins Application page
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        # Verify that the title of the page is "Pins System"
        self.assertIn("Pins System", self.driver.title)

    def test_table(self):
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        
        #wait until the table is loaded
        sleep(5)

        # Find the table element by tag name
        table = self.driver.find_element(By.TAG_NAME, "table")
        
        # check if the table is displayed
        self.assertTrue(table.is_displayed())
        
    def test_table_headers(self):
        
        # Navigate to the Pins Application page
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')

        # wait until the table is loaded
        sleep(5)

        # Check if the table headers are displayed by XPATH
        headers_row = self.driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr[1]")

        #check the text of the headers
        headers = headers_row[0].find_elements(By.TAG_NAME, "td")
        #check if the headers length is 4
        self.assertEqual(len(headers), 4)
        #check if the headers are correct
        self.assertEqual(headers[0].text, 'Pin ID')
        self.assertEqual(headers[1].text, 'Title')
        self.assertEqual(headers[2].text, 'Body')
        self.assertEqual(headers[3].text, 'User ID')
    
    def test_row_length(self):
        # Navigate to the Pins Application page
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')

        # wait until the table is loaded
        sleep(5)

        #check the number of rows
        rows = self.driver.find_elements(By.TAG_NAME, "tr")
        self.assertEqual(len(rows), 17)

    def test_application_header(self):
        #Navigate to the Pins Application page
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        #wait until the page is loaded
        sleep(2)
        #check the heading name
        heading = self.driver.find_elements(By.XPATH, "/html/body/h1")
        self.assertEqual(len(heading), 1)
        self.assertEqual(heading[0].text, 'Pins Application')

    def test_modal(self):
        #navigate to the Pins Application page
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        # wait until the table is loaded
        sleep(3)

        #click on the second row
        rows = self.driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]")
        sleep(3)

        # scroll to the element using JavaScript
        actions = ActionChains(self.driver)
        actions.move_to_element(rows[0]).perform()

        # click on the element
        rows[0].click()

        #wait until the modal is loaded
        sleep(3)

        #wait until the modal is loaded
        sleep(3)
        #check if the modal is displayed
        modal = self.driver.find_elements(By.XPATH, "/html/body/div[1]")

        self.assertTrue(modal[0].is_displayed())
    def test_modal_close(self):
        #navigate to the Pins Application page
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        # wait until the table is loaded
        sleep(3)

        #click on the second row
        rows = self.driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]")
        sleep(3)

        # scroll to the element using JavaScript
        actions = ActionChains(self.driver)
        actions.move_to_element(rows[0]).perform()

        # click on the element
        rows[0].click()

        #wait until the modal is loaded
        sleep(3)
        #check if the modal is displayed
        modal = self.driver.find_elements(By.XPATH, "/html/body/div[1]")

        #click on the close button
        close_button = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/span")
        close_button[0].click()
        #wait until the modal is closed
        sleep(3)
        assert modal[0].is_displayed() == False

    def test_modal_content(self):
        #navigate to the Pins Application page
        self.driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        # wait until the table is loaded
        sleep(3)
        
        #click on the second row
        rows = self.driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]")
        sleep(3)
        
        # scroll to the element using JavaScript
        actions = ActionChains(self.driver)
        actions.move_to_element(rows[0]).perform()

        # click on the element
        rows[0].click()

        #wait until the modal is loaded
        sleep(3)
        #check if the modal is displayed
        modal = self.driver.find_elements(By.XPATH, "/html/body/div[1]")
        

        if modal[0].is_displayed():
            #check if the modal content is correct
            modal_content_h2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/h2")
            
            assert modal_content_h2[0].text == 'Title Updated'
            modal_content_body = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/p[1]")
            assert modal_content_body[0].text == 'My Body Updated'
            
            modal_content_user = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/p[2]")
            assert modal_content_user[0].text == 'User ID: 3'
            modal_content_image = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/img")
            assert modal_content_image[0].get_attribute('src') == 'https://www.codimite.com/wp-content/uploads/2021/04/logo-with-slogan.png'
            

    
    def tearDown(self):
        # Close the browser
        self.driver.quit()



if __name__ == "__main__":
   unittest.main()