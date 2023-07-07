import requests


def scrape_linkedin_profile(url):
    gist = requests.get("https://gist.githubusercontent.com/gajdaj2/08fb80c2b94b5ff423177d495f97618c/raw/2df77c44081c29686eedc9a8c1fb921adda5670c/gajdaj.json")
    return gist.json()



if __name__ == '__main__':
    print(scrape_linkedin_profile("https://www.linkedin.com/in/alexander-gajdaj-2b0b0b1b3/"))