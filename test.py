from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/title/tt9764362/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=ea4e08e1-c8a3-47b5-ac3a-75026647c16e&pf_rd_r=4RS8RSZY8RSX0CZDBA6H&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_tt_6'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('h1').get_text()
role = soup.find_all('li', {'role': 'presentation'})
date = role[2].get_text()[0:4]
rating = soup.find('div', {'data-testid': 'hero-rating-bar__popularity__score'}).get_text()
plot_text = soup.find_all('span', {'role': 'presentation'})[-1].get_text().strip()

print(title)
print(date)
print(rating)
print(plot_text)
