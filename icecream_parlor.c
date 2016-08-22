#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int m;
        int n;
        scanf("%d", &m);
        scanf("%d", &n);
        int arr[n];
        for (int arr_i = 0; arr_i < n; arr_i++){
            scanf("%d", &arr[arr_i]);
        }
        int mindif = INT_MAX;
        int curdif = -1;
        int num1, num2;
        for (int ind1 = 0; ind1 < n - 1; ++ind1) {
            for (int ind2 = ind1 + 1; ind2 < n; ++ind2) {
                curdif = m - (arr[ind1] + arr[ind2]);
                if (curdif == 0) {
                    num1 = ind1;
                    num2 = ind2;
                    goto DONE;
                }
                else if ((curdif < mindif) && (curdif > 0)) {
                    num1 = ind1;
                    num2 = ind2;
                    mindif = curdif;
                }
            }
        }
        DONE:
        printf("%d %d\n", ++num1, ++num2);
    }
    return 0;
}
