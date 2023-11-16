"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
def cigar_party(cigers, is_weekend):
    if is_weekend:
        if cigers >= 40 or cigers >= 60:
            return True
        return False
    else:
        if cigers >= 40 and cigers <= 60:
            return True
        else:
            return False
    return True

