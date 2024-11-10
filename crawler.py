import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_page(url, depth, visited):
    # Base case: stop recursion if depth is 0 or if the URL has already been visited
    if depth == 0 or url in visited:
        return []

    visited.add(url)
    links = []
    
    try:
        # Fetch the page
        response = requests.get(url)
        if response.status_code != 200:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all links on the page
        for link_tag in soup.find_all('a', href=True):
            link = link_tag['href']
            full_link = urljoin(url, link)  # Handle relative URLs
            if urlparse(full_link).netloc == urlparse(url).netloc:  # Only stay within the same domain
                links.append(full_link)
                
        # Crawl the links recursively
        nested_links = []
        for link in links:
            nested_links.extend(crawl_page(link, depth - 1, visited))
        
        return links + nested_links

    except requests.RequestException:
        return []

def start_crawl(root_url, depth):
    visited = set()
    crawled_links = crawl_page(root_url, depth, visited)
    return crawled_links
