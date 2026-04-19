if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This will check the arguments and print it."
    )

    parser.add_argument(
        "-c", 
        "--color", 
        metavar="color", 
        required=True,
        choices={"red", "yellow"}, 
        help="the color to search for"
    )

    args = parser.parse_args()

    print(args.color)