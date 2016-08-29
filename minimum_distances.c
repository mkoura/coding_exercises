#include <stdio.h>
#include <string.h>
#include <limits.h>

// https://www.hackerrank.com/challenges/minimum-distances

int main() {
    int n;
    scanf("%d", &n);

    int dis[n];
    memset(dis, ~0, sizeof(dis));

    int arr[n], min_dist = INT_MAX, val = 0, p_i = 0, sub = 0;
    for (int i = 0; i < n; ++i){
        scanf("%d", &arr[i]);
        val = arr[i] % n;
        p_i = dis[val];
        if ((p_i > ~0) && (arr[i] == arr[p_i])){
            sub = i - p_i;
            if (sub < min_dist)
                min_dist = sub;
        }
        dis[val] = i;
    }

    printf("%d\n", (min_dist < INT_MAX) ? min_dist : -1);
}
