#!/usr/bin/env python3

def print_fibonacci(length):
        fibonacci_sequence = []
        a, b = 0, 1

        if length == 0:
          print([])
          return
        elif length == 1:
          print([a])
          return
        elif length == 2:
          print([a,b])
          return

        for _ in range(length):
          fibonacci_sequence.append(a)
          a, b = b, a + b

        print(fibonacci_sequence)
        pass


print_fibonacci(10)