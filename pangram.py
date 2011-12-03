def ispangram(s):
    s_set = set(s)

    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    if alphabet < s_set:
        return "NULL"
    else:
        missing_chars = ""
        unsorted_missing_chars = ""
        for c in alphabet - s_set:
            unsorted_missing_chars += c

        for c in sorted(unsorted_missing_chars):
            missing_chars += c

        return missing_chars


print(ispangram("A quick brown fox jumps over the lazy dog"))
print(ispangram("A slow yellow fox crawls under the proactive dog"))
