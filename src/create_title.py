def url_to_dashed_title(url):
    tokens = url.split('/')
    dashed_title = tokens[-2]
    return dashed_title

def dashed_to_title(url):
    tokens = url.split("-")
    tokens = [token.capitalize() for token in tokens]
    return ' '.join(tokens)

if __name__ == '__main__':
    print (url_to_dashed_title('https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/'))