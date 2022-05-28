#!/usr/bin/env python3
import nrz

def main():
    data = [1, 0, 1, 0, 1, 1, 0, 0]
    print(nrz.get_encoded_sequence(data))

if __name__ == "__main__":
    main()


