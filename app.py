from flask import Flask, request, jsonify
from crawler import start_crawl

app = Flask(__name__)

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()

    # Validate input parameters
    root_url = data.get('root_url')
    depth = data.get('depth')

    if not root_url or not depth:
        return jsonify({"status": "error", "message": "Missing required parameters"}), 400

    try:
        depth = int(depth)
        if depth < 1 or depth > 5:
            raise ValueError("Depth must be between 1 and 5.")
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400

    # Start the crawling process
    crawled_links = start_crawl(root_url, depth)

    # Prepare the response
    response = {
        "status": "success",
        "root_url": root_url,
        "depth": depth,
        "crawled_links": crawled_links
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
