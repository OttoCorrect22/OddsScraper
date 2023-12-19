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

    # find the date element using CSS selector
    date_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)'
    date_element = driver.find_element(By.CSS_SELECTOR, date_css_selector)

    # Extract text from the date element
    date = date_element.text

    # Print the team information
    print(f'{away_team_name}, {away_team_record}')
    print('@')
    print(f'{home_team_name}, {home_team_record}')
    print(f'{date}')

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
    print(f'Opened // {away_team_name}: {opening_spread_sign}{opening_spread_value}')
    print(f'Currently // {away_team_name}: {current_spread_value}')

    # find bet mgm odds
    bet_mgm_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    bet_mgm_spread_element = driver.find_element(By.CSS_SELECTOR, bet_mgm_spread_css_selector)
    bet_mgm_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    bet_mgm_odds_element = driver.find_element(By.CSS_SELECTOR, bet_mgm_odds_css_selector)
    bmgm_open_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
    bmgm_open_element = driver.find_element(By.CSS_SELECTOR, bmgm_open_css_selector)

    hbet_mgm_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(4) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    hbet_mgm_spread_element = driver.find_element(By.CSS_SELECTOR, hbet_mgm_spread_css_selector)
    hbet_mgm_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(4) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    hbet_mgm_odds_element = driver.find_element(By.CSS_SELECTOR, hbet_mgm_odds_css_selector)


    bet_mgm_spread = bet_mgm_spread_element.text
    bet_mgm_odds = bet_mgm_odds_element.text
    bet_mgm_open = bmgm_open_element.text




    hbet_mgm_spread = hbet_mgm_spread_element.text
    hbet_mgm_odds = hbet_mgm_odds_element.text




    print(f'Bet MGM Home // {hbet_mgm_spread} {hbet_mgm_odds}')
    print(f'Bet MGM Away// {bet_mgm_spread} {bet_mgm_odds}')
    print(f'Bet MGM Open // {bet_mgm_open}')


    # find caesars odds
    caesars_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    caesars_spread_element = driver.find_element(By.CSS_SELECTOR, caesars_spread_css_selector)
    caesars_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    caesars_odds_element = driver.find_element(By.CSS_SELECTOR, caesars_odds_css_selector)

    hcaesars_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    hcaesars_spread_element = driver.find_element(By.CSS_SELECTOR, hcaesars_spread_css_selector)
    hcaesars_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    hcaesars_odds_element = driver.find_element(By.CSS_SELECTOR, hcaesars_odds_css_selector)

    caesars_open_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
    caesars_open_element = driver.find_element(By.CSS_SELECTOR, caesars_open_css_selector)



    caesars_spread = caesars_spread_element.text
    caesars_odds = caesars_odds_element.text
    hcaesars_spread = hcaesars_spread_element.text
    hcaesars_odds = hcaesars_odds_element.text
    caesars_open = caesars_open_element.text

    print(f'Caesars Home // {hcaesars_spread} {hcaesars_odds}')

    print(f'Caesars Away // {caesars_spread} {caesars_odds}')

    print(f'Caesars Open // {caesars_open}')

    # find draftkings odds
    draftkings_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    draftkings_spread_element = driver.find_element(By.CSS_SELECTOR, draftkings_spread_css_selector)
    draftkings_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    draftkings_odds_element = driver.find_element(By.CSS_SELECTOR, draftkings_odds_css_selector)


    hdk_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    hdk_spread_element = driver.find_element(By.CSS_SELECTOR, hdk_spread_css_selector)
    hdk_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    hdk_odds_element = driver.find_element(By.CSS_SELECTOR, hdk_odds_css_selector)

    dk_open_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
    dk_open_element = driver.find_element(By.CSS_SELECTOR, dk_open_css_selector)

    hdk_spread = hdk_spread_element.text
    hdk_odds = hdk_odds_element.text
    draftkings_spread = draftkings_spread_element.text
    draftkings_odds = draftkings_odds_element.text
    dk_open = dk_open_element.text

    print(f'DraftKings Away // {draftkings_spread} {draftkings_odds}')
    print(f'DraftKings Home // {hdk_spread} {hdk_odds}')
    print(f'DraftKings Open // {dk_open}')

    # find fanduel odds
    fanduel_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    fanduel_spread_element = driver.find_element(By.CSS_SELECTOR, fanduel_spread_css_selector)
    fanduel_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    fanduel_odds_element = driver.find_element(By.CSS_SELECTOR, fanduel_odds_css_selector)

    hfanduel_spread_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
    hfanduel_spread_element = driver.find_element(By.CSS_SELECTOR, hfanduel_spread_css_selector)
    hfanduel_odds_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    hfanduel_odds_element = driver.find_element(By.CSS_SELECTOR, hfanduel_odds_css_selector)


    fanduel_open_css_selector = '.sc-fc4ee170-2 > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
    fanduel_open_element = driver.find_element(By.CSS_SELECTOR, fanduel_open_css_selector)


    fanduel_open = fanduel_open_element.text
    fanduel_spread = fanduel_spread_element.text
    fanduel_odds = fanduel_odds_element.text
    hfanduel_spread = hfanduel_spread_element.text
    hfanduel_odds = hfanduel_odds_element.text

    print(f'FanDuel Away // {fanduel_spread} {fanduel_odds}')
    print(f'FanDuel Home // {hfanduel_spread} {hfanduel_odds}')
    print(f'FanDuel Open // {fanduel_open}')

finally:
    # Close the browser window
    driver.quit()
