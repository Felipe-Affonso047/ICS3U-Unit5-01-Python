#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program converts celsius to fahrenheit


def fahrenheit():
    # this function converts celsius to fahrenheit
    celsius = float(input("Insert degrees in celsius: "))

    fahrenheit_output = (celsius * 9 / 5) + 32

    print("{0} C = {1} F".format(celsius, fahrenheit_output))


def main():
    # Is the main function
    try:
        fahrenheit()
    except Exception:
        print("\nThis input is invalid, please, insert a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
