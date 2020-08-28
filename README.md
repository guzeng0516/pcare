## Some Thought Processes:
1. we are only looking for one function to do both en/decrypt message
1. first step is to determine if we want to encrypt or decrypt input message,
`_encrypt` and `_decrypt` helper functions could help
1. we could abstract these functions into a object(or not)
1. list comprehension could help to simplify my code, makes it looks neat
1. assume `type(input_message) == str`, handle empty string input edge case.
1. use python list as stringBuilder, and `''.join()` for good ; )
1. use python `assert` to provide basic testing ability


# Simple Design
A solution wrapper class is created for a scope to hold mappings, 
so we could have different mapping for different instances if needed.

main function `encrypt_or_decrypt` validate input message, 
decrypt message if message contains any number, encrypted it otherwise



```
class solution:
     char_num_mappings: dict
     num_char_mappings: dict
     
     encrypt_or_decrypt(message: str): str
     
     # helpers
     _is_encrypted_message(message:str): bool
     _encrypt(original_message: str): str
     _decrypt(encrypted_message: str): str

```


## How to test
a code runner and simple test runner code is included, 
if all tests passed, we should see "All tests passed" after we execute this script.

