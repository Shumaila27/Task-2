import pyshorteners  # Import the pyshorteners library to shorten URLs

def shorten_url(long_url):
    # Initialize the Shortener object to use Tinyurl (you can also use other services like Bitly, etc.)
    s = pyshorteners.Shortener()
    
    # Generate the short URL using Tinyurl
    short_url = s.tinyurl.short(long_url)  # Using Tinyurl shortener to shorten the URL
    
    return short_url

def main():
    # Ask the user for a long URL
    long_url = input("Enter the long URL to shorten: ").strip()  # Strip any extra spaces
    
    # Debugging: Print the input URL to check for issues
    print(f"Received URL: '{long_url}'")  # This will show the exact input without extra spaces
    
    # Check if the user entered a valid URL (basic check)
    if not (long_url.startswith("http://") or long_url.startswith("https://")):
        print("Please enter a valid URL starting with http:// or https://")
        return  # Exit the function if the URL is not valid
    
    # Shorten the URL
    short_url = shorten_url(long_url)
    
    # Display the shortened URL
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()  # Call the main function to run the program
