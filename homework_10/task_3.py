import random


def permute(word):
    first, *middle, last = list(word)
    if len(middle) < 2:
        return word
    permuted_middle = random.sample(middle, len(middle))
    if permuted_middle != middle:
        permuted_word = ''.join([first] + permuted_middle + [last])
        return permuted_word
    else:
        return word


def permute(word):
    if len(word) <= 3:
        return word
    else:
        first, *middle, last = list(word)
        shuffled_middle = random.sample(middle, len(middle))
        shuffled_word = ''.join([first] + shuffled_middle + [last])
        if shuffled_word == word:
            return word
        else:
            return shuffled_word


def permute_text(text):
    # Розділяємо текст на слова
    words = text.split()
    permuted_words = [permute(word) for word in words]
    return ' '.join(permuted_words)


text = 'За результатами дослідження одного англійського університету, не має значення,' \
              ' в якому порядку розташовані букви в слові. Головне, щоб перша і остання букви були на місці. ' \
              'Решта букв можуть слідкувати в повному безладі, все одно текст читається без проблем. ' \
              'Причиною цього є те, що ми не читаємо кожну букву окркмо, а все слово цілком.'
permuted_text = permute_text(text)
print(permuted_text)
