import requests


def scrape_linkedin_profile(url):
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    api_key = os.environ['PROXY_CURL']
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'url': url,
        'fallback_to_cache': 'on-error',
        'use_cache': 'if-present',
        'skills': 'include',
        'inferred_salary': 'include',
        'personal_email': 'include',
        'personal_contact_number': 'include',
        'twitter_profile_id': 'include',
        'facebook_profile_id': 'include',
        'github_profile_id': 'include',
        'extra': 'include',
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


# method iterate all json field and check if field is empty and remove it


# def scrape_linkedin_profile(url):
#     gist = requests.get(
#         "https://gist.githubusercontent.com/gajdaj2/08fb80c2b94b5ff423177d495f97618c/raw/2df77c44081c29686eedc9a8c1fb921adda5670c/gajdaj.json")
#     return gist.json()


if __name__ == '__main__':
    print(scrape_linkedin_profile2("https://www.linkedin.com/in/magdalenawieclaw/"))
