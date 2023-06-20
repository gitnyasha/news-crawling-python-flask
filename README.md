# News Crawler Project - Summary

The News Crawler project is a Python-based web scraping application that extracts headlines from popular news sources, including CNN, NBC, and Yahoo. The project utilizes the Flask web framework and the ScrapingBee API to schedule the crawling process and display the news on a webpage.

Here's a summary of the project code:

1. **Setting up ScrapingBee:** The project begins with signing up for a ScrapingBee account and obtaining an API key. The ScrapingBee library is installed to facilitate the scraping process.

2. **Identifying Websites to Scrape:** The code identifies the URLs of the news sources, along with the extract rules required to retrieve the headlines from each source.

3. **Creating the News Crawler:** The news_crawler.py file is created, and the necessary modules are imported. The ScrapingBee client is initialized with the API key, and the URLs and extract rules are defined for each news source.

4. **Scheduling and Displaying News with Flask:** Flask and the APScheduler library are utilized to schedule the crawling process and showcase the headlines on a webpage. Flask routes are created, and functions are implemented to retrieve the headlines and update the webpage with the latest news. The scheduler is configured to run the crawling process at regular intervals.

By following the project code, you can learn how to set up ScrapingBee, scrape news headlines from different sources, and use Flask to display the extracted news on a webpage. The code provides a foundation for building a customizable news crawler and automating the process of retrieving headlines.

Feel free to modify the code to suit your specific needs and explore additional features to enhance the scraping and display capabilities. Happy scraping!
