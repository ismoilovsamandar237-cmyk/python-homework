# 1
from threading import Thread

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def check_range(start, end, result_list):
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    result_list.extend(primes)


# MAIN PROGRAM
if __name__ == "__main__":
    start_range = 1
    end_range = 10000
    thread_count = 4

    # range bo‘linadi
    step = (end_range - start_range + 1) // thread_count

    threads = []
    results = []

    for i in range(thread_count):
        s = start_range + i * step
        e = s + step - 1 if i < thread_count - 1 else end_range
        
        t = Thread(target=check_range, args=(s, e, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Prime numbers found:")
    print(sorted(results))

# 2
from threading import Thread
from collections import defaultdict

def count_words(lines, result_dict):
    local_dict = defaultdict(int)

    for line in lines:
        words = line.lower().split()
        for w in words:
            local_dict[w] += 1

    # merge into shared dict
    for w, c in local_dict.items():
        result_dict[w] += c


if __name__ == "__main__":
    file_path = "big_text.txt"
    
    with open(file_path, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    thread_count = 4
    step = len(all_lines) // thread_count

    threads = []
    result = defaultdict(int)

    for i in range(thread_count):
        portion = all_lines[i*step : (i+1)*step] if i < thread_count-1 else all_lines[i*step:]
        t = Thread(target=count_words, args=(portion, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Word occurrences:")
    for word, count in result.items():
        print(word, ":", count)
