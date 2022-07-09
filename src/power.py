def main():
    print("This is a cli tool")
    from sys import argv
    try:
        if argv[1] == "-a":
            print("Exra option selected")
    except:
        pass
