import unittest
from url_shortener_shell import URLShortener


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.shortener = URLShortener()


    def test_shorten_url(self):
        """Test URL shortening functionality."""
        long_url = "https://samlewis347.github.io./" #using my personal websites url to test the url shortener

        #shorten the original url
        short_url = self.shortener.shorten_url(long_url)

        self.assertTrue(short_url.startswith(self.shortener.base_url))  #shortened url should start with base_url
        self.assertEqual(self.shortener.url_dict.get(short_url.replace(self.shortener.base_url, '')), long_url) #are the long url maps to the correct url code


    def test_get_original_url(self):
        """Test URL retrieval functionality."""
        long_url = "https://samlewis347.github.io./"
        short_url = self.shortener.shorten_url(long_url)
        
        #getting the url code from the shortened url
        url_code = short_url.replace(self.shortener.base_url, '')
        
        #getting the original url using the url code
        retrieved_url = self.shortener.get_original_url(url_code)
        
        #making sure that the retrieved URL matches the original URL
        self.assertEqual(retrieved_url, long_url)
        
        #testing for a potential case where the url code does not exist
        with self.assertRaises(ValueError):
            self.shortener.get_original_url("nonexistenturlcode")


    def test_invalid_url(self):
        """Test handling of invalid URLs."""
        invalid_urls = [
            "www.missingScheme.com",  # Missing scheme
            "ftp://invalidScheme.com",  # Invalid scheme
            "https://missingDomain",  # Missing domain
        ]
        
        for url in invalid_urls:
            with self.assertRaises(ValueError):
                self.shortener.shorten_url(url)


if __name__ == "__main__":
    unittest.main()