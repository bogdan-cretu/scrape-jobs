from bs4 import BeautifulSoup
import requests

current_link = 'https://www.hipo.ro/locuri-de-munca/cautajob/Toate-Domeniile/Toate-Orasele/python/'
slug = 0
def scrape(current_link):
    global html_text,soup,jobs
    html_text = requests.get(current_link).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('tr', itemtype="http://schema.org/JobPosting")
scrape(current_link)


def list_jobs():
    for job in jobs:
        global job_title
        job_title = job.find('a', class_='job-title').text
        company_name = job.find('td', class_='cell-company').text
        company_address = job.find('td', class_='cell-city').text
        job_date = job.find(itemprop='datePosted').text
        job_type = job.find(itemprop='employmentType').text
        job_experience = job.find(itemprop='experienceRequirements').text
        job_page = soup.find('span', class_="page page-current").text
        for link in soup.findAll('a', {'class': 'job-title'}):
            partial_slug = link['href']
            link_final = "https://www.hipo.ro" + partial_slug
        print(f'''
            Company name: {company_name}
            Job name: {job_title}
            Company address: {company_address}
            Job type: {job_type}
            Required experience: {job_experience}
            Posted on: {job_date}
            Current page: {job_page}
            Link: {link_final}
        ''')
        print('------------------------------------------------------------')

for i in range(5):
    if slug == 0:
        list_jobs()
        slug += 2
    else:
        new_web_address = current_link + str(slug)
        scrape(new_web_address)
        list_jobs()
        slug += 1
