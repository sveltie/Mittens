from mittens.tensor import tensor


def main() -> None:
    my_tensor = tensor([1, 2, 3], dtype=int)

    print(f"__str__: {str(my_tensor)}")
    print(f"__repr__: {repr(my_tensor)}")
    print(f"__len__: {len(my_tensor)}")


if __name__ == "__main__":
    main()
