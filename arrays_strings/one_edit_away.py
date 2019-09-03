class OneEditAway:
    """Checks whether or not two strings are at most one edit away (default). This maximum number
    of allowed edits can actually be changed in the init function (to 0, or 2, for example).

    Keyword arguments:
    strA -- [str] the first string to check
    strB -- [str] the second string to check

    Special:
    The class instantiation itself can be printed to give the result (a string representation of
    True or False).
    """

    def __init__(self, strA, strB):
        self.max_edits = 1  # Maximum number of edits that can be made
        self.passed = self.check(strA, strB)  # Call the checking function

    def check(self, strA, strB, edits=0):
        """
        Returns whether or not strA and strB are at most self.max_edits away

        This is a recursive function (using Dynamic Programming principles) which makes the
        necessary edits (removing either the first or last character of one of the strings) whilst
        increasing the edits count until either the remaining strings are the same (True) or we run
        out of edits (False). For this to work, every time the first character of both strings are
        the same, we remove these characters and continue.

        Keyword arguments:
        strA -- [str] the first string to check
        strB -- [str] the second string to check
        edits -- [int] (optional) (default:0) the number of edits already made

        Return values:
        [bool] -- whether or not strA is at most self.max_edits edits away from strB
        """

        if edits > self.max_edits:
            """We've already made too many edits (False)
            """
            return False
        elif strA == strB:
            """The strings are the same (True)
            """
            return True
        elif abs(len(strA) - len(strB)) > self.max_edits:
            """The difference in length of the strings is more than the possible allowed number of
            edits, so the minimal number of edits needed to make for both strings to be equal will
            be at least higher than what is allowed (False)
            """
            return False
        elif len(strA) == 0 or len(strB) == 0:
            """One of the remaining strings is out of characters, so we can't remove any more from
            it. The remaining number of characters in the other string (max_len) is how many more
            edits will be needed to make both strings equal. This plus the current number of edits
            must be less than the maximum number allowed (i.e. edits + max_len <= max_edits for
            True, otherwise False). The equality sign here also works based on the program flow."""
            max_len = max(len(strA), len(strB))
            return edits == self.max_edits - max_len
        elif strA[0] == strB[0]:
            """This is the heart of the recursion. If the starting character of both strings are
            the same, we can return the result from running this checking function on the
            substrings removing these first characters. I.e.
            `check("abc", "abc") = check("bc", "bc")`
            """
            return self.check(strA[1:], strB[1:], edits=edits)
        elif len(strA) > len(strB):
            """The starting characters are different, and string A is greater than string B. So
            let's look at the result of checking string B against string A with the first character
            removed, and the result of checking string B against string A with the last character
            removed. If either of these return True, we return True. This is another recursion
            call. We increase the number of edits here by 1 to keep count.
            """
            return self.check(strA[1:], strB, edits=edits + 1) or self.check(
                strA[:-1], strB, edits=edits + 1
            )
        elif len(strB) > len(strA):
            """Same as the previous check, but swapping string A and B around.
            """
            return self.check(strA, strB[1:], edits=edits + 1) or self.check(
                strA, strB[:-1], edits=edits + 1
            )
        else:
            """If we reach this stage, then we still have at least one edit left, the strings do
            not match, the first characters do not match, and the strings are of the same length.
            In that case, return the result from removing the first character from both strings,
            i.e. making one edit (and therefore also increasing the edit count by 1).
            """
            return self.check(strA[1:], strB[1:], edits=edits + 1)

    def __str__(self):
        """For printing purposes.
        """
        return str(self.passed)


if __name__ == "__main__":
    strA = input("String A? ")
    strB = input("String B? ")
    print(OneEditAway(strA, strB))
