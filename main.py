import sys
import requests

def memorizer(verse):
    # verse = 'Mark 1:10-12'
    url = 'https://api.esv.org/v3/passage/text/'
    params = {
        'q': verse,
        'include-passage-references': True,
        'include-verse-numbers': False,
        'include-footnotes': False,
        'include-footnote-body': False,
        'include-headings': False,
        'include-short-copyright': False,
        'include-copyright': False,
        'include-chapter-numbers': False,
        }
    token = {'Authorization': 'Token d073af62f207d309cbcf6d7cae83300902fa7df9'}
    res = requests.get(url, params=params, headers=token)
    res_json = res.json()

    print(res_json['passages'][0])

if __name__ == '__main__':
    memorizer(sys.argv[1])
