#include <stdio.h>

// https://www.hackerrank.com/challenges/lisa-workbook

int main() {
    int n, k, t, page = 0, special = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++){
        scanf("%d", &t);
        page++;
        for (int j = 1; j <= t; j++){
            if (page == j)
                special++;
            if ((j % k == 0) && (j != t))
                page++;
        }
    }

    printf("%d\n", special);
}
