# Web Crawler API

This is a simple web crawler API built with Flask. The API accepts a URL and a crawl depth as input, crawls the website recursively up to the specified depth, and returns a list of all crawled URLs.

## API Endpoint

### POST `/crawl`

#### Request Body:
```json
{
  "root_url": "https://example.com",
  "depth": 3
}


#### Response Body:
```json
{
  "status": "success",
  "root_url": "https://example.com",
  "depth": 3,
  "crawled_links": [
    "https://example.com",
    "https://example.com/about",
    "https://example.com/contact",
    "https://example.com/blog",
    "https://example.com/blog/post1"
  ]
}

