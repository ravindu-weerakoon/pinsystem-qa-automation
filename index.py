from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



def test_title():
    try:
        # Start the browser
        driver = webdriver.Firefox()
        # Navigate to the Pins Application page
        driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        # Verify that the title of the page is "Pins System"
        assert "Pins System" in driver.title
        # Close the browser
        driver.quit()
        return ['Test Title','Passed']
    
    except AssertionError as e:
        return ['Test Title','AssertionError']
    
    except Exception as e:
        return ['Test Title','Failed']

def test_table():
    try:
        # Start the browser
        driver = webdriver.Firefox()
        # Navigate to the Pins Application page
        driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')
        
        #wait until the table is loaded
        sleep(5)

        # Find the table element by tag name
        table = driver.find_element(By.TAG_NAME, "table")
        
        # check if the table is displayed
        assert table.is_displayed()
        # Close the browser
        
        return ['Test Table','Passed']
        
    
    except AssertionError as e:
        print(e)
        
        return ['Test Table','AssertionError']
    
    except Exception as e:
        print(e)
        
        return ['Test Table','Failed']



def test_table_headers():
    try:
        # Start the browser
        driver = webdriver.Firefox()
        # Navigate to the Pins Application page
        driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')

        # wait until the table is loaded
        sleep(5)

        # Check if the table headers are displayed by XPATH
        headers_row = driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr[1]")
        
        #check the text of the headers
        headers = headers_row[0].find_elements(By.TAG_NAME, "td")
        #check if the headers length is 4
        assert len(headers) == 4
        #check if the headers are correct
        assert headers[0].text == 'Pin ID'
        assert headers[1].text == 'Title'
        assert headers[2].text == 'Body'
        assert headers[3].text == 'User ID'
        # Close the browser
        driver.quit()
        return ['Test Table Headers','Passed']

    except AssertionError as e:
        driver.quit()
        return ['Test Table Headers','AssertionError']

    except Exception as e:
        print(e)
        driver.quit()
        return ['Test Table Headers','Failed']

def test_row_length():
    try:
        # Start the browser
        driver = webdriver.Firefox()
        # Navigate to the Pins Application page
        driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')

        # wait until the table is loaded
        sleep(5)

        #check the number of rows
        rows = driver.find_elements(By.TAG_NAME, "tr")
        print(rows)
        assert len(rows) == 16
        
        # Close the browser
        driver.quit()
        return ['Test Row Length','Passed']

    except AssertionError as e:
        return ['Test Row Length','AssertionError']

    except Exception as e:
        return ['Test Row Length','Failed']

def  test_application_header():
    try:
        # Start the browser
        driver = webdriver.Firefox()
        # Navigate to the Pins Application page
        driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')

        # wait until the table is loaded
        sleep(3)

        #check the heading name
        rows = driver.find_elements(By.XPATH, "/html/body/h1")
        assert len(rows) == 1
        assert rows[0].text == 'Pins Application'
        
        # Close the browser
        driver.quit()
        return ['Test Application Header','Passed']

    except AssertionError as e:
        return ['Test Application Header','AssertionError']

    except Exception as e:
        return ['Test Application Header','Failed']

def test_modal():
    try:
        # Start the browser
        driver = webdriver.Firefox()
        # Navigate to the Pins Application page
        driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')

        # wait until the table is loaded
        sleep(3)
        
        #click on the second row
        rows = driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]")
        sleep(3)
        
        # scroll to the element using JavaScript
        actions = ActionChains(driver)
        actions.move_to_element(rows[0]).perform()

        # click on the element
        rows[0].click()

        #wait until the modal is loaded
        sleep(3)

        #wait until the modal is loaded
        sleep(3)
        #check if the modal is displayed
        modal = driver.find_elements(By.XPATH, "/html/body/div[1]")

        assert modal[0].is_displayed()

        # Close the browser
        driver.quit()
        return ['Test Modal Visibility','Passed']

    except AssertionError as e:
        print(e)
        return ['Test Modal Visibility','AssertionError']

    except Exception as e:
        print(e)
        return ['Test Modal Visibility','Failed']

def test_close_modal():
    try:
        # Start the browser
        driver = webdriver.Firefox()
        # Navigate to the Pins Application page
        driver.get('file:///home/ravihansa/Documents/pinsystem-frontend/index.html')

        # wait until the table is loaded
        sleep(3)
        
        #click on the second row
        rows = driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]")
        sleep(3)
        
        # scroll to the element using JavaScript
        actions = ActionChains(driver)
        actions.move_to_element(rows[0]).perform()

        # click on the element
        rows[0].click()

        #wait until the modal is loaded
        sleep(3)
        #check if the modal is displayed
        modal = driver.find_elements(By.XPATH, "/html/body/div[1]")
        
       
        #click on the close button
        close_button = driver.find_elements(By.XPATH, "/html/body/div[1]/div/span")
        close_button[0].click()
        #wait until the modal is closed
        sleep(3)
        assert modal[0].is_displayed() == False

        # Close the browser
        driver.quit()
        return ['Test Modal Close','Passed']

    except AssertionError as e:
        print(e)
        return ['Test Modal Close','AssertionError']

    except Exception as e:
        print(e)
        return ['Test Modal Close','Failed']



if __name__ == "__main__":
    title_test = test_title()
    table_test = test_table()
    header_test = test_table_headers()
    row_test = test_row_length()
    heading_test = test_application_header()
    display_modal_test = test_modal()
    close_modal_test = test_close_modal()
    pandas_data = pd.DataFrame([close_modal_test], columns=['Test Name', 'Result']).to_csv('test_results.csv', index=False)
    
    