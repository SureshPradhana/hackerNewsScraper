import requests
from bs4 import BeautifulSoup

res=requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.titleline')
votes=soup.select('.subtext')
#lists length check
print(len(links),len(votes))
#custom hackernew which has points greeter than 99
def create_custom_hn(links,votes):
    hn=[]
    for idx,item in enumerate(links):
        points=votes[idx].select('.score')
        if len(points):
            title=links[idx].select('a')[0].getText()
            href=links[idx].select('a')[0].get('href',None)
            point=int(points[0].getText().replace(' points',''))
            if point > 99:
                hn.append({'titie':title,'link':href,'points':point})
    # print(hn)
    return hn
res=create_custom_hn(links,votes)
f=open("result.txt","w")
f.write(''.join(str(e) for e in res))
f.close()