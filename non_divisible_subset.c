#include <stdio.h>

// https://www.hackerrank.com/challenges/non-divisible-subset

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int re[k];
    for (int i = 0; i < k; ++i)
        re[i] = 0;

    int val = 0;
    for (int arr_i = 0; arr_i < n; arr_i++){
        scanf("%d", &val);
        re[val % k]++;
    }

    int count = 0;
    int ind1;
    for (ind1 = 1; ind1 < ((k + 1) / 2); ++ind1) {
        int ind2 = k - ind1;
        if (re[ind1] >= re[ind2])
            count += re[ind1];
        else
            count += re[ind2];
    }
    if ((ind1 * 2 == k) && (re[ind1] > 0))
        count++;
    if (re[0] > 0)
        count++;

    printf("%d\n", count);
}
