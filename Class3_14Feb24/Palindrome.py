def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c +rev_str
    return rev_str

original_str = input("Enter string to reverse\n")
original_str = original_str.lower()
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")