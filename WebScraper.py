import requests
from bs4 import BeautifulSoup


def parser(link):
    r = requests.get(link)
    if r.status_code <= 500:#here 500 is just a an arbitrary number
        readhtml = r.text
        soup = BeautifulSoup(readhtml, 'html.parser')

        # Reads all h1 tags in website
        Header = ""
        titles = soup.find_all("h1")
        for title in titles:
            Header += "Title :" + title.text + "\n"

        # reads all p tags in website
        body = ""
        pgraphs = soup.find_all("p")
        for pgraph in pgraphs:
            body += "Content :" + pgraph.text + "\n"


        # create a file named scrap
        f = open("Scrap.txt", 'w', encoding='utf-32')
        f.write(Header)#writes all headings in page
        f.write(body)#writes all paragraphs in page
        f.close()
    else:
        print("The website could not be Reached. Status: ", r.status_code)


def main():
    # Takes link and passes to parser function
    link = input("Enter Link for scraping: ")
    parser(link)


if __name__ == '__main__':
    main()

