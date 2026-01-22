from string import punctuation
def word_frequency_counter(sentences,n):
    splitted_words=word_splitter(sentences)
    frequency_map=get_frequency_map(splitted_words)
    n_high_frequencies=get_n_high_frequencies(frequency_map,n)
    high_frequencies_map={}
    for _ in n_high_frequencies:
        high_frequencies_map[_]=frequency_map[_]
    return high_frequencies_map

def word_splitter(sentences):
    all_words=[]
    for s in sentences:
        words=s.lower().split()
        for word in words:
            cleaned_word=word.strip(punctuation)
            all_words.append(cleaned_word)
    return all_words
def get_frequency_map(sample_list):
    frequency_map={}
    for l in sample_list:
        frequency_map[l]=frequency_map.get(l,0)+1
    return frequency_map

def get_n_high_frequencies(frequency_map,n):
    if n>=0:
        sorted_frequency_map=[pair[0] for pair in sorted(frequency_map.items(),key=lambda x:x[1],reverse=True)]
    return sorted_frequency_map[:n]
def main():
    high_frequent_words=word_frequency_counter(sentences,n)

    print(f"Top {n} most frequent words:")
    i=1
    for pair in high_frequent_words:
        print(f"{i}. {pair} → {high_frequent_words[pair]}")
        i+=1

if __name__=="__main__":
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "The dog was not amused.",
        "Why did the fox jump over the dog again?"
    ]
    n = 3
    main()


