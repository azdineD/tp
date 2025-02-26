def addition(a, b):
    "somme de deux nombres."
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python addition.py <nombre1> <nombre2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f"Résultat : {addition(num1, num2)}")
    except ValueError:
        print("Veuillez entrer deux nombres valides.")
