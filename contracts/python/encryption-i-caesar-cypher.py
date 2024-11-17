UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption_i_caesar_cypher(input_data: list[str, int]) -> str:
    cypher, shift = input_data
    answer = ""

    for symbol in cypher:
        if symbol == ' ':
            answer += symbol
        elif symbol in UPPER_ALPHABET:
            index = UPPER_ALPHABET.index(symbol) - shift
            while index < 0:
                index += len(UPPER_ALPHABET)
            answer += UPPER_ALPHABET[index]
    
    return answer

def main():
    assert encryption_i_caesar_cypher(["DEA", 3]) == "ABX"

    # contract-564273.cct: $75.000m
    assert encryption_i_caesar_cypher(["FRAME ARRAY ENTER PRINT QUEUE", 19]) == "MYHTL HYYHF LUALY WYPUA XBLBL"

if __name__ == "__main__":
    main()