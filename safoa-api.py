import requests, os

os.system("clear")
print("LAUNCHING...")

try:
    response = requests.get("https://bs-tech.herokuapp.com/accounts/").json()
    try:
        count = -1
        product_key = input("ENTER PRODUCT KEY: ")
        found_product_key = False
        for i in range(len(response)):
            count += 1
            if response[count]['product_key'] == product_key:
                found_product_key=True
                email = response[count]['email']
        if found_product_key:
            print(email+", YOUR ACCOUNT HAS BEEN SUCCESSFULLY ACTIVATED")
        else:
            print("INVALID PRODUCT KEY")
    except Exception as e:
        print(e)
except:
    print("CONNECT TO THE INTERNET AND TRY AGAIN!")
