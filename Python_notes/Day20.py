def simple_generator():
    print("Start")
    yield 1
    yield 2
    yield 3
print("End")
#Simple generator
def count_up_to(n):
 count = 1
 while count <= n:
  yield count
  count += 1
counter = count_up_to(5)
print(next(counter)) # Output: 1
print(next(counter))
#next() in generator
def countdown(n):
    while n > 0:
     yield n
     n -= 1
cd = countdown(3)
print(next(cd)) 
print(next(cd)) 
print(next(cd)) 
print(next(cd))
#Infinite news in instagram
def fetch_posts():
    post_id = 1
    while True:
     yield f"Post {post_id}"
     post_id += 1
news_feed = fetch_posts()
print(next(news_feed)) 
print(next(news_feed))