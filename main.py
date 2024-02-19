from modules.sites import profile_links, check_profile

def main():
    input_url = input("Enter the profile URL: ")
    profiles = profile_links(input_url)
    check_profile(profiles)

if __name__ == "__main__":
    main()
