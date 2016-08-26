#include <stdio.h>

// https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

int main() {
    int n, k, E = 100, val = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++){
        scanf("%d", &val);
        if (i % k == 0)
            E -= (val == 0) ? 1 : 3;
    }
    printf("%d\n", E);
}
