#include <stdio.h>

// https://www.hackerrank.com/challenges/beautiful-triplets

#define MAXA (2*10*10*10*10+2)

int main() {
    int n, d;
    scanf("%d %d", &n, &d);
    char hashtab[MAXA] = {0};
    int val;
    for (int i = 0; i < n; i++){
        scanf("%d", &val);
        hashtab[val] = 1;
    }
    int count = 0;
    for (int i = 0; i < MAXA - 2 * d; i++){
        if (hashtab[i] == 0)
            continue;
        if ((hashtab[i + d] == 1) && (hashtab[i + d + d] == 1))
            count++;
    }
    printf("%d\n", count);
}
