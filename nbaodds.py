from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the URL
url = 'https://www.sportsline.com/nba/odds'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load (you may need to adjust the wait time)
    driver.implicitly_wait(10)

    # Find the home team name element using CSS selector
    home_team_name_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
    home_team_name_element = driver.find_element(By.CSS_SELECTOR, home_team_name_css_selector)

    # Extract text from the home team name element
    home_team_name = home_team_name_element.text

    # Find the home team record element using CSS selector
    home_team_record_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    home_team_record_element = driver.find_element(By.CSS_SELECTOR, home_team_record_css_selector)

    # Extract text from the home team record element
    home_team_record = home_team_record_element.text

    # Find the away team name element using CSS selector
    away_team_name_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
    away_team_name_element = driver.find_element(By.CSS_SELECTOR, away_team_name_css_selector)

    # Extract text from the away team element
    away_team_name = away_team_name_element.text

    # Find the away team record element using CSS selector
    away_team_record_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    away_team_record_element = driver.find_element(By.CSS_SELECTOR, away_team_record_css_selector)

    # Extract text from the away team record element
    away_team_record = away_team_record_element.text

    # Print the team information
    print(f'{away_team_name}, {away_team_record}')
    print('@')
    print(f'{home_team_name}, {home_team_record}')
    print()

    # Find the opening spread element using CSS selector
    opening_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)'
    opening_spread_element = driver.find_element(By.CSS_SELECTOR, opening_spread_css_selector)

    # Extract text from the opening spread element
    opening_spread = opening_spread_element.text

    # Find the current match spread element using CSS selector
    current_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
    current_spread_element = driver.find_element(By.CSS_SELECTOR, current_spread_css_selector)

    # Extract text from the current match spread element
    current_spread = current_spread_element.text

    # Extract the sign and value from the opening spread
    opening_spread_parts = opening_spread.split(' ')
    opening_spread_sign = opening_spread_parts[0]
    opening_spread_value = opening_spread_parts[1]

    # Extract the value from the current spread
    current_spread_parts = current_spread.split(' ')
    current_spread_value = current_spread_parts[0]

    # Print the consensus information with the desired format
    print('Consensus:')
    print(f'Opened // {home_team_name}: {opening_spread_sign}{opening_spread_value}')
    print(f'Currently // {home_team_name}: {current_spread_value}')

finally:
    # Close the browser window
    driver.quit()
