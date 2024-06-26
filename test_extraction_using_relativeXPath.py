""""
Test Extraction using Relative XPath
"""

from extraction_using_relativeXPath import Guvi_InstagramPage
import pytest

web_url = "https://www.instagram.com/guviofficial/"
instagrampage = Guvi_InstagramPage(web_url)


# Test the guvi instagram page url
def test_get_url():
    assert instagrampage.get_url() == True
    print("Success:Guvi Instagram Page is loaded successfully")

#test the total number of followers data
def test_extract_followers():
    assert instagrampage.extract_followers() == True
    print("Success : Total Number of followers has been fetched")

#test the total number of following data
def test_extract_following():
    assert instagrampage.extract_following() == True
    print("Success : Total Number of following has been fetched")

#close the automation
def test_shutdown():
    assert instagrampage.shutdown() == None
    print("Success : Automated Guvi Instagram Page is Closed")


