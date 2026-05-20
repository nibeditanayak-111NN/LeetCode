from collections import Counter

class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words

        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            curr_count = {}
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == total_words:
                        result.append(left)

                else:
                    curr_count.clear()
                    count = 0
                    left = right + word_len

        return result