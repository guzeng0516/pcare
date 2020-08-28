class Solution:
    def __init__(self, char_number_pairs):
        """
        Solution takes character number pairs tuples for initialize mappings
        this provided more flexibility if we have other mapping strategies.
        """
        self.char_number_mappings = dict(char_number_pairs)
        self.number_char_mappings = dict([(num, letter) for letter, num in char_number_pairs])

    def encrypt_or_decrypt(self, message):
        """
        validate input message, decrypt message if message contains any number, encrypted it otherwise
        """
        if not message:
            return message

        if any(char.isdigit() for char in message):
            return self._decrypt_message(message)

        return self._encrypt_message(message)

    def _encrypt_message(self, original_massage):
        """
        :param original_massage: str
        :return: encrypted_massage: str
        """

        def _encrypt_char(char):
            if char in self.char_number_mappings:
                return str(self.char_number_mappings[char])
            return char

        encrypted_chars = [_encrypt_char(char) for char in original_massage]
        return ''.join(encrypted_chars)

    def _decrypt_message(self, encrypted_massage):
        """
        :param encrypted_massage: str
        :return: decrypted_message: str
        """

        def _decrypt_char(char):
            if char in self.number_char_mappings:
                return self.number_char_mappings[char]
            return char

        decrypted_chars = [_decrypt_char(char) for char in encrypted_massage]
        return ''.join(decrypted_chars)


# code runner
LETTER_NUMBER_PAIRS = [
    ('a', '1'),
    ('e', '2'),
    ('i', '3'),
    ('o', '4'),
    ('u', '5'),
]
solution = Solution(LETTER_NUMBER_PAIRS)

# test runner
test_cases = [
    ("", ""),
    ("this is a message.", "th3s 3s 1 m2ss1g2."),
    ("1n4th2r m2ss1g2 h2r2!", "another message here!"),
    ("aaa", "111")
]

for test_case in test_cases:
    """
    for each test case, encrypted message should be equal to expected value
    decrypted encrypted message should be equal to original value
    """
    encrypted_message = solution.encrypt_or_decrypt(test_case[0])
    assert encrypted_message == test_case[1]

    decrypted_message = solution.encrypt_or_decrypt(encrypted_message)
    assert decrypted_message == test_case[0]

print("ALL TEST PASSED!")
