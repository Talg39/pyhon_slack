from Functions import f

if __name__ == "__main__":
    # Initialize variables - read input from user
    print("Please enter url with the syntax like 'https://mobideo.com'")
    url = input()
    print('Received url:', url)
    if f.is_valid(url):
        info = f.get_url(url)
        status = (f.decipher_status(info.status_code))
        if status == "OK":
            print("Status code is 200. continue...")
            # Send slack message
        else:
            print("===== Status code is not 200 (", status,"). please provide a url that is up and working, example: "
                  "https://mobideo.com =====")
            # Send slack message
    else:
        print("===== dns is not valid, Please use the syntax as 'https://mobideo.com' =====")
        # Send slack message