try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search

query = input("What do you want to search!")

for j in search(query, tld='com',lang='en', num=10,start=0, stop=10, pause=2.0):
    print(j)
