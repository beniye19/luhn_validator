import argparse
from luhn import luhn_algorithm

MIN_LENGTH = 10  # Minimum allowed digits
MAX_LENGTH = 16  # Maximum allowed digits

def main():
    parser = argparse.ArgumentParser(description="Luhn's Algorithm Number Validator")
    parser.add_argument("number", type=str, help="Number to validate")
    args = parser.parse_args()

    if not args.number.isdigit():
        print("❌ Invalid input! Please enter digits only.")
        return

    if len(args.number) > MAX_LENGTH:
        print(f"❌ Number too long! Maximum allowed length is {MAX_LENGTH} digits.")
        return

    if len(args.number) < MIN_LENGTH:
        print(f"❌ Number too short! Minimum allowed length is {MIN_LENGTH} digits.")
        return

    result = luhn_algorithm(args.number)
    if result:
        print(f"✅ {args.number} is a VALID number.")
    else:
        print(f"❌ {args.number} is an INVALID number.")

if __name__ == "__main__":
    main()
