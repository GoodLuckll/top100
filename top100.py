import requests
import parsel
def getHtml(url, headers):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('ERROR')
def fillList(html):
    html = parsel.Selector(html)
    title = html.xpath('//p[@class="name"]/a/text()').extract()
    star = html.xpath('//p[@class="star"]/text()').extract()
    releasetime = html.xpath('//p[@class="releasetime"]/text()').extract()
    a=html.xpath('//p[@class="score"]/i[@class="integer"]/text()').extract()
    b=html.xpath('//p[@class="score"]/i[@class="fraction"]/text()').extract()
    for i in range(len(title)):
        temp={"标题":title[i],"主演":star[i].strip(),"日期":releasetime[i],"评分":a[i]+b[i]}
        print(temp)
    
def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    deep=10
    for i in range(deep):
        url = 'http://maoyan.com/board/4?offset='+str(i*10)
        html = getHtml(url, headers)
        fillList(html)
main()

