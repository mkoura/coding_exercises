#include <stdio.h>

// https://www.hackerrank.com/challenges/fair-rations

int main() {
    int n;
    scanf("%d", &n);
    int in;
    int oddcount = 0;
    int gaps = 0;
    for (int i = 0; i < n; i++){
        scanf("%d", &in);
        if (in % 2)
            oddcount++;
        else if (oddcount % 2)
            gaps++;
    }
    if (oddcount % 2)
        printf("NO\n");
    else
        printf("%d\n", oddcount + gaps * 2);
}
