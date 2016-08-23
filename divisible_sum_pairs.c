#include <stdio.h>

// https://www.hackerrank.com/challenges/divisible-sum-pairs

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int arr[n];
    for (int arr_i = 0; arr_i < n; arr_i++){
        scanf("%d", &arr[arr_i]);
    }

    int count = 0;
    for (int ind1 = 0; ind1 < n - 1; ++ind1) {
        for (int ind2 = ind1 + 1; ind2 < n; ++ind2) {
            if (((arr[ind1] + arr[ind2]) % k) == 0)
                ++count;
        }
    }
    printf("%d\n", count);
}
