import requests
import heapq

def get_articles(limit):
    result = []
    articles = []
    page = 1
    total_pages = 1

    # O(n)
    while page <= total_pages:
        response = requests.get(f'http://mock-api.hypnobox.com.br:4011/teste/api/articles?page={page}')
        total_pages = response.json()['total_pages']
        page += 1
        articles.extend(response.json()['data'])

    # O(n)
    aux =[]
    for article in articles:
        if article['title'] is None and article['story_title'] is None:
            continue
        if article['num_comments'] is None:
            article['num_comments'] = 0
        
        if article['title'] is None:
            article['title'] = article['story_title']
        
        aux.append({'num_comments': article['num_comments'], 'title': article['title']})

    # O(n log n)
    result = sorted(aux, key=lambda d: d['num_comments'], reverse=True) 


    # # O(n log limit)
    # heap = []
    # for article in articles:
    #     if article['title'] is None and article['story_title'] is None:
    #         continue
    #     if article['num_comments'] is None:
    #         article['num_comments'] = 0
    #     if article['title'] is not None:
    #         heapq.heappush(heap, (article['num_comments'], article['title']))
    #     else:
    #         heapq.heappush(heap, (article['num_comments'], article['story_title']))

    #     if len(heap) > limit:
    #         heapq.heappop(heap)

    # # O(n)
    # for pairs in heap:
    #     result.append(f'{pairs[1]} , {pairs[0]}')

    return result[:limit]


print(get_articles(7))