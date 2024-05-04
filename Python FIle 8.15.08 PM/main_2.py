
class raval():
        import json
        import requests
        from main import yagna
        
        for site in yagna.indicators:
                
                params={'apikey':yagna.api,'resource':yagna.indicators}
                page= requests.get(yagna.url, params=params)
                response= json.loads(page.content)
                
        # print(response['positives'])
                #print(response['total'])
                result=response['positives']
                
                test_cases=response['total']
                
               
                