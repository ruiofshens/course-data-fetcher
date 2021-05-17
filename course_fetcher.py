from bs4 import BeautifulSoup, SoupStrainer
import urllib.request

queryString = "?subj=" + input("Enter course code to query:")
url = 'https://wish.wis.ntu.edu.sg/webexe/owa/aus_vacancy.check_vacancy2' + queryString.strip().upper()

# Generating URL request
req = urllib.request.Request(
    url,
    data=None,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }
)

# Fetch URL
html = urllib.request.urlopen(req).read().decode("utf-8")

# Create a SoupStrainer to only parse <td> tags and ignore other tags
courseDataOnly = SoupStrainer("td")

# Parse document using BeautifulSoup and store in a ResultSet
# Uses lxml's HTML parser - use pip install lxml
# (Can also just use Python's parser by changing 'lxml' below to 'html.parser')
# Do not use html5lib parser, if SoupStrainer class is used.
soup = BeautifulSoup(html, 'lxml', parse_only = courseDataOnly)

# Basic Formatting and printing of course data
# TODO: Proper formatting of data
courseData = []
for data in soup:
     courseData.append(data.text.strip())
del courseData[:8]
courseData = [x for x in courseData if not ('<td>' in x or '</td>' in x or x == '')]

print(courseData)

# for something in soup:
#      print(something.text.strip())