import codecs  # Pour l'unicode


def file_to_list(filename: str) -> list:
    """Return a list of strings separated by a new line 
    Args:
        filename is a string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        string_line_list = []
        i = 0
        for line in f:
            string_line_list.append(line[:len(line) - 1])  # We slice the '\n'
    return string_line_list


def find_similar_length(string_searched: str, list_of_string: list) -> list:
    """Args
        string_searched : the string to compare
        list_of_string : The list to search
    Return 
        The results
    """
    result_list = []
    for strings in list_of_string:
        if len(strings) == len(string_searched):
            result_list.append(strings)
    return result_list


def code_newtone(coded_char: chr) -> list:
    match coded_char:
        case '0': return ['B']
        case '1': return ['L']
        case '2': return ['A']
        case '3': return ['E', 'D', 'F']
        case '4': return ['G', 'H', 'I']
        case '5': return ['J', 'K', 'L']
        case '6': return ['M', 'N', 'O']
        case '7': return ['P', 'Q', 'S']
        case '8': return ['T', 'U', 'V']
        case '9': return ['X', 'Y', 'Z']


def decode_cipher(cipher: str, decoded_cipher: str, string_cursor=0, voyel=['A', 'E', 'I', 'O', 'U']):
    if string_cursor >= len(cipher):
        print(decoded_cipher)
        return

    if cipher[string_cursor] == 'A' or cipher[string_cursor] == 'E':
        decoded_cipher = decoded_cipher + cipher[string_cursor]
        return decode_cipher(cipher, decoded_cipher, string_cursor + 1)

    char_possibilities = code_newtone(cipher[string_cursor])
    for char in char_possibilities:
        decoded_cipher_copy = decoded_cipher + char
        decode_cipher(cipher, decoded_cipher_copy, string_cursor + 1)
    return


def main():
    artist_list = file_to_list("artist.txt")
    code_list = file_to_list("artists_code.txt")
    """
    for code in code_list:
        result = find_similar_length(code, artist_list)
        if code == "E546E":
            continue
        for i in range(len(result)):
            print(f" {code} |", end="")
        print()
        for i in range(len(result)):
            print(f" {result[i]} |", end="")
        print()
        print('----------------------------------------------')
    """
    decode_cipher("123118419", ' :')
    return 0


if __name__ == "__main__":
    main()
