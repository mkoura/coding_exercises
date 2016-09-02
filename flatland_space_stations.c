#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// https://www.hackerrank.com/challenges/flatland-space-stations

int compare(const void * a, const void * b) {
  return (( *(int*)a > *(int*)b ) - ( *(int*)a < *(int*)b ));
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int m_arr[m];
    for(int i = 0; i < m; i++)
        scanf("%d", &m_arr[i]);
    qsort(m_arr, m, sizeof(int), compare);

    int max_dis = 0, dis = 0, last_idx = m_arr[0];
    for(int i = 1; i < m; i++) {
        dis = m_arr[i] - last_idx - 1;
        if(dis > max_dis)
            max_dis = dis;
        last_idx = m_arr[i];
    }
    max_dis = (max_dis + 1) / 2;

    dis = n - last_idx - 1;
    if(dis > max_dis)
        max_dis = dis;
    dis = m_arr[0];
    if(dis > max_dis)
        max_dis = dis;
    printf("%d\n", max_dis);
}
