#include <stdio.h>

// https://www.hackerrank.com/challenges/save-the-prisoner

int main() {
    int t = 0;
    scanf("%d", &t);
    for(int ti = 0; ti < t; ti++) {
        int n = 0, m = 0, s = 0;
        scanf("%d %d %d", &n, &m, &s);
        printf("%d\n", ((s + m - 2) % n) + 1);
    }
}
