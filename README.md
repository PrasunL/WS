## Web Scraping Documentation

### Overview
This Python script is designed to perform web scraping on a given URL by extracting content from HTML elements such as 'h1' (headings) and 'p' (paragraphs). It utilizes the `requests` library to fetch the HTML content of the specified URL and the `BeautifulSoup` library for parsing the HTML.

### Functions

#### `parser(link)`
This function takes a URL as input and performs the following steps:
1. Sends an HTTP request to the provided link using the `requests.get()` method.
2. If the status code of the HTTP response is less than or equal to 500, it proceeds to parse the HTML content.
3. Utilizes BeautifulSoup to extract data:
   - Retrieves all 'h1' tags (headings) and concatenates them into a string variable named `Header`.
   - Retrieves all 'p' tags (paragraphs) and concatenates them into a string variable named `body`.
4. Writes the extracted headings and paragraphs to a file named "Scrap.txt" using UTF-32 encoding.

#### `main()`
This function serves as the entry point of the program. It prompts the user to input a URL and calls the `parser()` function, passing the provided URL for scraping.

### Libraries Used
- `requests`: Used for making HTTP requests to retrieve web page content.
- `BeautifulSoup` from `bs4`: Used for parsing HTML content and extracting specific elements.

### Usage
1. Run the script.
2. Input the URL of the webpage you want to scrape.
3. The script will extract all 'h1' (headings) and 'p' (paragraphs) tags' content and save it in a file named "Scrap.txt" in UTF-32 encoding.

### Error Handling
- If the HTTP status code is greater than 500, the script will print an error message indicating that the website could not be reached.

### Notes
- Ensure that the provided URL is accessible and contains the desired content in 'h1' and 'p' tags for successful scraping.
- The extracted data will be saved in a file named "Scrap.txt" in the same directory as the script.
- Make sure you have proper permissions to write files in the directory where the script is executed.
