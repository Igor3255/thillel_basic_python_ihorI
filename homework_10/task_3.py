def pemrtuate(text):
    words = text.split()
    
    for i in range(len(words)):
        if len(words[i]) > 3:
            first, *middle, last = words[i]
            new_middle = []
            
            for j in range(0, len(middle), 3):
                if j + 3 <= len(middle):
                    original_triple = middle[j:j + 3]
                    permuted_triple = sample(original_triple, 3)
                    while permuted_triple == original_triple:
                        permuted_triple = sample(original_triple, 3)
                    new_middle += permuted_triple
                else:
                    new_middle += middle[j:]
            
            new_word = "".join([first] + new_middle + [last])
            words[i] = new_word
            
    return " ".join(words)
