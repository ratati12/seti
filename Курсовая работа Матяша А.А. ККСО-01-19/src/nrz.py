#!/usr/bin/env python3
import matplotlib.pyplot as plt

def set_settings():
    plt.xlim([-1, 5])
    plt.ylim([-1.2, 1.2])
    plt.xlabel('Time', fontsize=15, color='black')
    plt.ylabel('Voltage', fontsize=15, color='black')
    plt.grid(True)
    plt.title("Oscillogram", fontsize=15)

def print_oscillogram(x_coordinates, y_coordinates):
    set_settings()
    plt.plot(x_coordinates, y_coordinates, 'b', linewidth=3)
    plt.show()

def print_encoded_oscillogram(sequence):
    y_coordinates = get_y_coordinates_for_encoding(get_encoded_sequence(sequence))
    x_coordinates = get_x_coordinates_for_encoding(len(y_coordinates))
    print_oscillogram(x_coordinates, y_coordinates)

def get_encoded_sequence(sequence):
    if sequence == None:
        raise Exception("Your sequence is None!")
    if len(sequence) == 0:
        raise Exception("The size of your sequence is zero!")

    encoded_sequence = []
    for i in range (len(sequence)):
        if sequence[i] != 0 and sequence[i] != 1:
            raise Exception("Incorrect data format!")

        if sequence[i] == 1:
            encoded_sequence.append(1)
        else:
            encoded_sequence.append(0)

    return encoded_sequence

def get_y_coordinates_for_encoding(sequence):
    y_coordinates = []
    y_coordinates.append(0)
    for i in range(0, len(sequence)):
        y_coordinates.append(sequence[i])
        y_coordinates.append(sequence[i])
    return y_coordinates

def get_x_coordinates_for_encoding(length):
    sequence = []
    step = 0
    sequence.append(step)
    for i in range(1, length, 4):
        sequence.append(step)
        step += 1
        sequence.append(step)
        sequence.append(step)
        step += 1
        sequence.append(step)
    return sequence

def print_decoded_oscillogram(sequence):
    y_coordinates = get_y_coordinates_for_decoding(get_decoded_sequence(sequence))
    x_coordinates = get_x_coordinates_for_decoding(len(y_coordinates))
    print_oscillogram(x_coordinates, y_coordinates)

def get_decoded_sequence(sequence):
    if sequence == None:
        raise Exception("Your sequence is None!")
    if len(sequence) == 0:
        raise Exception("The size of your sequence is zero!")
    decoded_sequence = []
    for i in range (len(sequence)):
        if sequence[i] != 0 and sequence[i] != 1:
            raise Exception("Incorrect data format!")
        if sequence[i] == 1:
            decoded_sequence.append(1)
        else:
            decoded_sequence.append(0)

    return decoded_sequence

def get_y_coordinates_for_decoding(sequence):
    y_coordinates = []
    y_coordinates.append(0)
    for i in range(0, len(sequence)):
        y_coordinates.append(sequence[i])
        y_coordinates.append(sequence[i])
    return y_coordinates

def get_x_coordinates_for_decoding(length):
    sequence = []
    step = 0
    sequence.append(step)
    for i in range(1, length, 2):
        sequence.append(step)
        step += 1
        sequence.append(step)
    return sequence
