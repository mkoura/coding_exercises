#include <stdio.h>

// https://www.hackerrank.com/challenges/kangaroo

int main() {
    int x1, v1, x2, v2;
    scanf("%d %d %d %d", &x1, &v1, &x2, &v2);
    printf("%s\n", ((v1 > v2) && ((x1 - x2) % (v2 - v1) == 0)) ? "YES" : "NO");
}
