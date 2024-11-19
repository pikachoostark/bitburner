def find_largest_prime_factor(num):
    largest_prime = -1

    i = 2
    while (i ** 2 <= num):
        while (num % i == 0):
            largest_prime = i
            n = n // i
        i = i + 1
    
    if (n > 1):
        largest_prime = n
    
    return largest_prime

def main():
    # contract-793855.cct 2500/factions_amount reputation for each of the following factions
    assert find_largest_prime_factor(489891753) == 2797
    # contract-493258-CyberSec.cct: 2500 faction reputation for CyberSec
    assert find_largest_prime_factor(75261372) == 2971
    # contract-570830-Netburners.cct: 2500 faction reputation for Netburners
    assert find_largest_prime_factor(211489623) == 1861

if __name__ == "__main__":
    main()
