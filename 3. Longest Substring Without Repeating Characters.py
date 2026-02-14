def lengthOfLongestSubstring(string):
    print("String:", string)

    best = 0
    best_string = []
    new = []

    for step, ch in enumerate(string):
        print("\nSTEP", step, "reading:", ch)
        print("Current window before:", new)

        if ch in new:
            print("Duplicate found:", ch)

            if len(new) > best:
                best = len(new)
                best_string = new.copy()
                print("Updated best:", best, best_string)

            idx = new.index(ch)
            print("Removing till duplicate index:", idx)

            new = new[idx + 1:]
            print("Window after shrink:", new)

        new.append(ch)
        print("Window after append:", new)

    # final check
    if len(new) > best:
        best = len(new)
        best_string = new.copy()

    print("\nFinal best substring:", best_string)
    return best, "".join(best_string)


strn = "abcdfedbdgha"
result = lengthOfLongestSubstring(strn)
print("\nResult:", result)
