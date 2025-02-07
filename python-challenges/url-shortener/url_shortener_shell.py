import string
import random
from urllib.parse import urlparse

class URLShortener:
    def __init__(self, storage_file: str = "urls.json"):
        """Initialize the URL shortener with a storage file."""
        self.url_dict = {} #Declaring the dictionary that I will use to store both the shortened urls and the original length urls
        self.base_url = "http://shortened.co" #base url for the shortened links to be given


    #additional function generate_shortened_url_key to create the hash key for each shortened url
    def generate_shortened_url_key(self):
        characters = string.ascii_letters + string.digits #creating a string of all characters (lower case a-z, upper case A-Z and all numbers 0-9)
        shortened_url_key = ''.join(random.choice(characters) for i in range(6)) #picks a random character 6 times and adds it to the key string
        return shortened_url_key


    #additional function to handle the validation of urls
    def validate_url(self, long_url: str) -> bool:
        #using the urlparse library to break up the inputed url into its components
        parsed_url = urlparse(long_url)
        #checking to make sure the the url has a scheme and a netloc present
        if not parsed_url.scheme or not parsed_url.netloc:
            return False
        #checking to make sure that the urls scheme is either http or https
        if parsed_url.scheme not in ['http', 'https']:
            return False
        #checking to make sure that the domain is not empty
        if '.' not in parsed_url.netloc:
            return False
        #if the provided url passes all of the tests for validity then return true
        return True


    def shorten_url(self, long_url: str) -> str:
        """
        Convert a long URL into a short code.

        Args:
            long_url: The URL to shorten

        Returns:
            str: A unique short code for the URL

        Raises:
            ValueError: If the URL is invalid
        """
        #runs the validation fuction on the provided url and if it is not valid then it raises a ValueError
        if not self.validate_url(long_url):
            raise ValueError("Invalid URL was provided. Please enter a valid URL")
        #if the url is valid (it makes it to this point in the code) then generate a key unique to the provided long url
        url_key = self.generate_shortened_url_key()
        #make sure that the key is unique (attempt at preventing collisions)
        while url_key in self.url_dict:
            url_key = self.generate_shortened_url_key() #regenerates a new key of a collision is found
        #storing the url along with its key in the dictionary
        self.url_dict[url_key] = long_url
        #returning the base url with the unique key
        return self.base_url + url_key


    def get_original_url(self, short_code: str) -> str:
        """
        Retrieve the original URL from a short code.

        Args:
            short_code: The short code to look up

        Returns:
            str: The original URL

        Raises:
            ValueError: If the short code is not found
        """
        #checking for if the short code is in the dictionary
        if short_code not in self.url_dict:
            #if it is not found raise a ValueError
            raise ValueError("Short code was not found.")
        #if the error was not raised then return the original url associated with that short code
        return self.url_dict[short_code]


def main():
    """Main function to run the URL shortener."""
    #creating an instance of the URLShortener class
    url_shortener = URLShortener()

    #while true loop so that the program remains active until the user enters the exit command
    while True:
        print("Welcome to the URL shortener!")
        print("Choose an option:")
        print("1: Shorten a URL")
        print("2: Retrieve original URL from a short code")
        print("Type 'exit' to quit")

        #getting the users choice as an input
        choice = input("Enter your choice (1, 2, or 'exit'): ")

        #making an action based on that users choice
        if choice == "1":
            # Ask the user for the long URL to shorten
            long_url = input("Enter the long URL to shorten: ")
            try:
                # Shorten the URL and print the result
                short_url = url_shortener.shorten_url(long_url)
                print(f"Shortened URL: {short_url}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            # Ask the user for the short code to retrieve the original URL
            short_code = input("Enter the short code to retrieve the original URL: ")
            try:
                # Retrieve the original URL from the short code
                original_url = url_shortener.get_original_url(short_code)
                print(f"Original URL: {original_url}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice.lower() == "exit":
            print("Exiting the URL shortener. Goodbye!")
            break  # Exit the loop and stop the program

        else:
            print("Invalid choice. Please enter 1, 2, or 'exit'.")


if __name__ == "__main__":
    main()