from difflib import SequenceMatcher

s = SequenceMatcher(None, "Zenit St. Petersburg - Villarreal CF", "Zenit - Villarreal")

print(s.ratio())
