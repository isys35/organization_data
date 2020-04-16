import requests
from requests import Session

headers ={'Host': 'bankrot.fedresurs.ru',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://bankrot.fedresurs.ru/DebtorsSearch.aspx',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'}

def save_html_file(name, r):
    with open(f'{name}.html', 'wb') as html_file:
        html_file.write(r.encode('utf-8'))


if __name__ == '__main__':
    session = Session()
    r = session.get('https://bankrot.fedresurs.ru/DebtorsSearch.aspx')
    save_html_file('page',r.text)
    print(r.text)