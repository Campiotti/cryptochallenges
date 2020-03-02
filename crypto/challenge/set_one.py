import base64
# import binascii
from typing import List


def challenge_one(hex_: str):
    """
    Converts a Hex string to a base64 encoded string.
    prints actual content of hex string also

    See Also:
        https://cryptopals.com/sets/1/challenges/1

    Args:
        hex_: hex str to convert to base64

    Returns: hex_ converted from hex to base64.

    """
    as_bytes = bytearray.fromhex(hex_)
    return base64.b64encode(as_bytes)


def challenge_two(xor1: str, xor2: str = '686974207468652062756c6c277320657965'):
    """
    XOR two hex strings.

    See Also:
        https://cryptopals.com/sets/1/challenges/2
    Args:
        xor1: hex str1
        xor2: hex str2

    Returns: xor of both bytes.fromhex() str by using ord

    """
    in1 = bytes.fromhex(xor1)
    in2 = bytes.fromhex(xor2)
    res = xor_byte_strings(in1, in2)
    return res


def challenge_three_own_sol(encoded_hex: str, return_as_tuple=False):
    """
    Figures out which single char was used to xor encode a hex string by using
    Etaoin shrdlu

    See Also:
        https://cryptopals.com/sets/1/challenges/3
        https://en.wikipedia.org/wiki/Etaoin_shrdlu

    Args:
        encoded_hex: encoded hex str for which only one char was used to encode
        return_as_tuple: whether to return as Tuple with score attached

    Returns:
        max matching result bytes

    """
    encoded = bytes.fromhex(encoded_hex)

    if return_as_tuple:
        return decrypt_with_one_char_xor(encoded)
    return decrypt_with_one_char_xor(encoded)[0]


def challenge_four(potential_encoded: List[bytes]):
    holder = {}
    for potential in potential_encoded:
        decoded, score = challenge_three_own_sol(potential.decode(), True)
        holder[score] = decoded

    max_score = max(holder.keys())
    return holder[max_score]


def challenge_five(to_encode: str, repeating_key: str):
    repeat_len = len(repeating_key)

    repeat_key = repeating_key * int(len(to_encode) / repeat_len)

    # if not perfect match; add the rest of chars manually.
    if len(to_encode) % len(repeat_key) != 0:
        leftover = len(to_encode) % len(repeat_key)
        for i in range(leftover):
            repeat_key += repeating_key[i]

    return xor_byte_strings(to_encode.encode('ascii'), repeat_key.encode()).hex()


def decrypt_with_one_char_xor(encoded: bytes):
    decoded_holder = {}
    limit = 255  # chr uses unicode not ascii or smth along those lines...
    common = b'Etaoin shrdlu'

    for i in range(0, limit):
        decoded = xor_byte_strings(encoded, bytes(chr(i).encode()*len(encoded)))

        score = 0
        for j in range(len(common)):
            score += decoded.count(common[j])
        decoded_holder[score] = decoded

    return decoded_holder[max(decoded_holder.keys())], max(decoded_holder.keys())


def xor_byte_strings(input1: bytes, input2: bytes):
    """
    xor 2 byte strings into one

    Args:
        input1:
        input2:

    Returns:

    """
    return bytes([b1 ^ b2 for b1, b2 in zip(input1, input2)])
