#include <stdio.h>

// https://www.hackerrank.com/challenges/strange-code

int main() {
    long time;
    long value = 3;
    scanf("%ld", &time);

    while (time + 3 > value)
        value *= 2;
    printf("%ld\n", value - 2 - time);
    return 0;
}
