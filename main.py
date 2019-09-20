import time
from _Palindromes import _palindromes
from _BerlinClock import Clock, print_berlin_clock

def main():
    text = input("input palindrome:\n")
    print("-> isPalindrome: ", _palindromes(text))
    text = input("\ninput non-palindrome:\n")
    print("-> isPalindrome: ", _palindromes(text))
    input("Press Enter to continue...")
    print("\nwOW ThAt wAs CoOL, nOw CHeckOuT ThIs ClOcK...\n")
    input("Press Enter to continue...")

    clock = Clock()
    print_berlin_clock(clock)

    for i in range(5):
        clock = Clock()
        print_berlin_clock(clock)
        input("\nPress Enter to update time...")

if __name__ == "__main__":
    main()