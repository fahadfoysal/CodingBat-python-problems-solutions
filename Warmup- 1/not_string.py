"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
def not_string(str):
    if not "not" in str[:3]:
        new_str = "not " + str
        return new_str
    else:
        return str

#print(not_string("candy"))
