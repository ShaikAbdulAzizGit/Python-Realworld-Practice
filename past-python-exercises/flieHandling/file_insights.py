def get_lines(file):
    with open(file,'r') as f:
        lines=f.readlines()
    return len(lines)
def get_words(file):
    with open(file,'r') as f:
        words=f.read().split()
    return len(words)
def get_characters(file):
    with open(file,'r') as f:
        words=f.read().strip()
    return len(words)
def most_frequent_five(file):
    with open(file,'r') as f:
        data=f.read().strip().split()
    frequency_map={}
    for word in data:
        frequency_map[word]=frequency_map.get(word,0)+1
    high_frequency=[pair[0] for pair in sorted(frequency_map.items(),key=lambda x:x[1],reverse=True) ]
    if len(high_frequency)>5:
        return high_frequency[:5]
    else:
        return high_frequency
def main(file):
    print(f"Total lines : {get_lines(file)}")
    print(f"Total words : {get_words(file)}")
    print(f"Total characters : {get_characters(file)}")
    print(f"The top {'five' if len(most_frequent_five(file))>=5 else 'most'}")
    high_frequency_map=most_frequent_five(file)
    if len(high_frequency_map)>=5:
        for word in high_frequency_map:
            print(f"{word}")


if __name__=="__main__":
    main("sample.txt")