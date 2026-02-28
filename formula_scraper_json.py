from bs4 import BeautifulSoup
import time
import json
import requests

results = []
t1 = time.perf_counter()

url = 'https://formulae.brew.sh/formula'
json_path = '/home/empire/Empire_DevOps/bs_scraping/test1.json'

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "lxml")
    
    body = soup.find('body')
    paragragh = body.select_one('#default p')
    # clean_paragragh = " ".join(paragragh.get_text().split())
    # links = [a.get('href') for a in paragragh.select('a')]
    
    tables = body.select_one('#default table')
    rows = tables.find_all('tr')
    for row in rows:
        row_start = time.perf_counter()
        cells = row.find_all('td')
        if len(cells) == 3:
            name = cells[0].get_text(strip=True) if cells[0] else None
            version = cells[1].get_text(strip=True) if cells[1] else None
            desc = cells[2].get_text(strip=True) if cells[2] else None

            new_url = f'https://formulae.brew.sh/api/formula/{name}.json'

            try:
                r = requests.get(new_url)
                r.raise_for_status()
                package_json = r.json()

            except (requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
                print(f"Skipping {name}: {e}")
                continue

            analytics = package_json.get('analytics', {})
            install_30_value = analytics.get('install_on_request', {}).get('30d', {}).get(name, 0)
            install_90_value = analytics.get('install_on_request', {}).get('90d', {}).get(name, 0)
            install_365_value = analytics.get('install_on_request', {}).get('365d', {}).get(name, 0)

            data = {
            'name' : name,
            'version': version,
            'description': desc,
            'analytics': {
                '30d': install_30_value,
                '90d': install_90_value,
                '365': install_365_value
                }
            }

            results.append(data)
            row_end = time.perf_counter()
            print(f'Got {name} in {row_end - row_start:.2f} seconds')

    t2 = time.perf_counter()
    print(f"Finished in {t2 - t1:.2f} seconds")

    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

except Exception as e:
    print(f'Http Error: {e}')

