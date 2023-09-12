from bloom_filter import BloomFilter
from time import perf_counter_ns


def main():
    print("Reading dictionary data from disk")
    start = perf_counter_ns()
    bf = BloomFilter.from_file("dictionary_bloom_filter.bin")
    end = perf_counter_ns() - start
    print("Done reading", end)

    words = ["hello", "world", "pie", "xyz", "incor", "incorrect"]
    for word in words:
        start = perf_counter_ns()
        exists = bf.exists(word)
        end = perf_counter_ns()
        print(word, exists, end-start)


if __name__ == "__main__":
    main()
