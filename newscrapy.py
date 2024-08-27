# Check if the request was successful
if response.status_code == 200:
    print("Successfully retrieved the article.")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('meta', attrs={'name': 'twitter:title'})['content']
    
    
    
    article_paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text() for para in article_paragraphs])
    
    
    updated_date = soup.find('time')
    if updated_date:
        updated_date = updated_date.get_text()
    
    byline = soup.find(class_='byline')
    if byline:
        byline = byline.get_text()
    
    return {
        'title': title,
        'content': content,
        'updated_date': updated_date,
        'byline': byline
    }
else:
    return "Failed to retrieve the article."
