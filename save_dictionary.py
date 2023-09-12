from bloom_filter import BloomFilter

def main():
    bloom_filter = BloomFilter()

    with open("wiki-100k-cleaned.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word = line.strip()
            bloom_filter.store(word)

    bloom_filter.save_to_file("dictionary_bloom_filter.bin")


if __name__ == "__main__":
    main()
