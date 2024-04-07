# CRAWL DATA sanfoundry.com

> This is a crawler to crawl data from sanfoundry.com and store it in a json file.
> This crawler is written in python using Flask to create a REST API to crawl data from sanfoundry.com.

## Installation

1. Clone the repository
```bash
git clone https://github.com/TienNHM/crawl-sanfoundry-mcqs.git
```

2. Install the dependencies
```bash
pip install Flask
pip install requests
pip install beautifulsoup4
pip install jsonify
```

3. Run the server
```bash
python app.py
```

## API Endpoints

```bash
GET /mcqs/<url>
```

Example:
```bash
GET /mcqs/operating-system-mcqs-memory-management-swapping-1
```

Note: The url is the last part of the url of the page on sanfoundry.com. For example, the url of the page `https://www.sanfoundry.com/operating-system-questions-answers-memory-management-swapping-1/` is `operating-system-mcqs-memory-management-swapping-1`.