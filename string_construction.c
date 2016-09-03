#include <stdio.h>

// https://www.hackerrank.com/challenges/string-construction

int main() {
    int n;
    scanf("%d", &n);
    int ch;
    while (((ch = getchar()) != '\n') && (ch != EOF))
        ;

    for (int i = 0; i < n; i++) {
        int idx, count = 0;
        char llet[28] = {0};
        while (((ch = getchar()) != '\n') && (ch != EOF)) {
            idx = ch - 'a';
            if (llet[idx] != 1) {
                count++;
                llet[idx] = 1;
            }
        }
        printf("%d\n", count);
    }
}
