import threading
import time

def chop_sonlar(n):
    for i in range(n):
        print(i)

def chop_sonlar_2(n):
    for i in range(n):
        print(i + n)

def main():
    n = 10
    t1 = threading.Thread(target=chop_sonlar, args=(n,))
    t2 = threading.Thread(target=chop_sonlar_2, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Ishlash davomiyligi: {time.time() - start_time} soniya")
```

```python
import threading
import time

def chop_sonlar(n):
    for i in range(n):
        print(i)

def chop_sonlar_2(n):
    for i in range(n):
        print(i + n)

def main():
    n = 10
    t1 = threading.Thread(target=chop_sonlar, args=(n,))
    t2 = threading.Thread(target=chop_sonlar_2, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Ishlash davomiyligi: {time.time() - start_time} soniya")
