## WebBrowser in Python
- import webbrowser in the python
- Use webbrowser.open() function to open website and input complete string of website "https://github.com/afraz-hassan/python"

## Downloading from the Web with Request Module
- The requests module is a third-party module for downloading web pages and files.
- requests. get() returns a Response object.
- The raise_for_status() Response method will raise an exception if the download failed.
- You can save a downloaded file to your hard drive with calls to the iter_content() method.

## Parsing HTML with Beautiful Method
- Web pages are plaintext files formatted as HTML.
- HTML can be parsed with the BeautifulSoup module.
- BeautifulSoup is imported with the name bs4.
- Pass the string with the HTML to the bs4. BeautifulSoup() function to get a Soup object.
- The Soup object has a select) method that can be passed a string of the CSS selector for an HTML tag.
- You can get a CSS selector string from the browser's developer tools by right-clicking the element and selecting Copy CSS Path.
- The select) method will return a list of matching Element objects.


## Controlling the Browser with Selenium Module
- To import selenium, you need to run: from selenium import webdriver
• To open the browser, run: browser = webdriver.Firefox()
- To send the browser to a URL, run: browser.get ('http://inventwithpython.com')
- The browser.find_elements_by_css_selector() method will return a list of WebElement objects.
- WebElement objects have a text variable that contains the element's HTML in a string.
- The click() method will click on an element in the browser.
- The send_keys) method will type into a specific element in the browser.
- The submit) method will simulate clicking on the Submit button for a form.
- The browser can also be controlled with these methods: back), forward), refresh), quit().


## Selenium's WebDriver Methods for Finding Elements  
| Method Name                                      | WebElement Object/List Returned                                                                 |
|--------------------------------------------------|------------------------------------------------------------------------------------------------|
| browser.find_element_by_class_name(name)          | Elements that use the CSS class name                                                            |
| browser.find_elements_by_class_name(name)         | Elements that use the CSS class name (list)                                                     |
| browser.find_element_by_css_selector(selector)   | Elements that match the CSS selector                                                           |
| browser.find_elements_by_css_selector(selector)  | Elements that match the CSS selector (list)                                                    |
| browser.find_element_by_id(id)                   | Elements with a matching id attribute value                                                    |
| browser.find_elements_by_id(id)                  | Elements with a matching id attribute value (list)                                             |
| browser.find_element_by_link_text(text)          | `<a>` elements that completely match the text provided                                         |
| browser.find_elements_by_link_text(text)         | `<a>` elements that completely match the text provided (list)                                  |
| browser.find_element_by_partial_link_text(text)  | `<a>` elements that contain the text provided                                                  |
| browser.find_elements_by_partial_link_text(text) | `<a>` elements that contain the text provided (list)                                           |
| browser.find_element_by_name(name)               | Elements with a matching name attribute value                                                  |
| browser.find_elements_by_name(name)              | Elements with a matching name attribute value (list)                                           |
| browser.find_element_by_tag_name(name)           | Elements with a matching tag name (case insensitive; e.g., 'a' and 'A')                        |
| browser.find_elements_by_tag_name(name)          | Elements with a matching tag name (list)                                                       |
