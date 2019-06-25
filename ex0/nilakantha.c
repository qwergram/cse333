/**
 * Excercise 0
 * Copyright 2019 Norton Pengra
 * nortonjp@uw.edu
 * Student ID: 0542002
 */

#include <stdlib.h>
#include <stdio.h>

#define THROW_ERROR fprintf(stderr,  \
    "Usage: ./ex0 n, where n >= 0. " \
    "Prints Pi estimated to n "      \
    "terms of the Nilakantha series. \n");

#define ANOUNCE_RESULT(n) printf("Our estimate of Pi is %.20f", nilakantha(n));


/* Approximates pi using nilakantha's method up to n steps. */
double nilakantha(int n) {
    double result = 3.0;
    double twicei, delta;
    for (int i = 1; i < n + 1; i++) {
        twicei = 2.0 * (double)i;
        delta = 4.0 / twicei / (twicei + 1.0) / (twicei + 2.0);
        if (i % 2 == 1)
            result += delta;
        else
            result -= delta;
    }
    return result;
}

/* Takes in a number via command line and submits to nilakantha. */
int main(int argc, char* argv[]) {
    // Let the user know this ain't right
    if (argc != 2)
        THROW_ERROR;

    int n = atoi(argv[1]);

    // if n actually was a number, anounce the result
    if (n > 0 || (n == 0 && *argv[1] == '0')) {
        ANOUNCE_RESULT(n);
    } else {
        THROW_ERROR;
    }
}
