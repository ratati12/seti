#!/usr/bin/env python3
import nrz

def main():
    data = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    nrz.print_decoded_oscillogram(data)

if __name__ == "__main__":
    main()


