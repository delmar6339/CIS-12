def display_names(names):
    for name in names:
        print(name)
def display_names_reverse(names):
    for name in reversed(names):
        print(name)
def main():
    last_names = ["Konnor", "Kyle", "Kriek", "Aaron", "Bella", "Lilli", "Megan", "Michael", "Sara", "Tyrion"]
    print("Original order:")
    display_names(last_names)
    print("\nReverse order:")
    display_names_reverse(last_names)
if __name__ == "__main__":
      main()