#include <stdio.h>

// https://www.hackerrank.com/challenges/jumping-on-the-clouds

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int arr_i = 0; arr_i < n; arr_i++){
        scanf("%d", &arr[arr_i]);
    }

    int jumps = 0;
    int pos = 0;
    while (pos < n - 3) {
        if (arr[pos + 2] == 0)
            pos += 2;
        else
            pos += 1;
        ++jumps;
    }
    printf("%d\n", ++jumps);
    return 0;
}
