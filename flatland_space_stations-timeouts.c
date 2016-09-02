#include <stdio.h>
#include <string.h>

// https://www.hackerrank.com/challenges/flatland-space-stations

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int n_arr[n], val;
    memset(n_arr, 0, sizeof(n_arr));
    for(int i = 0; i < m; i++) {
        scanf("%d", &val);
        n_arr[val] = 1;
    }

    int max_dis = 0;
    for(int i = 0; i < n; i++) {
        int f = i, b = i, dis = 0;
        while((b >= 0) || (f <= n)) {
            if((n_arr[f] == 1) || (n_arr[b] == 1)) {
                if (max_dis < dis)
                    max_dis = dis;
                break;
            } else {
                dis++;
            }
            if(f < n)
                f++;
            if(b > 0)
                b--;
        }
    }
    printf("%d\n", max_dis);
}
