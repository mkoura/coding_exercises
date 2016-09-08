#include <stdio.h>
#include <stdlib.h>

// https://www.hackerrank.com/challenges/bigger-is-greater
// https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

int compare(const void * a, const void * b) {
  return (( *(int*)a > *(int*)b ) - ( *(int*)a < *(int*)b ));
}

int main() {
    int t = 0, ch;
    scanf("%d", &t);
    while (((ch = getchar()) != '\n') && (ch != EOF))
        ;

    for (int ti = 0; ti < t; ti++) {
        int w[100] = {0}, length = 0;
        while (((ch = getchar()) != '\n') && (ch != EOF) && (length < 100)) {
            w[length] = ch;
            length++;
        }

        int pivot, suff_begin = length - 1;
        while ((suff_begin > 0) && (w[suff_begin - 1] >= w[suff_begin]))
            suff_begin--;
        if (suff_begin == 0) {
            printf("no answer\n");
            continue;
        }
        pivot = suff_begin - 1;

        int switch_idx = suff_begin;
        for (int i = length - 1; i > pivot; i--) {
            if ((w[i] < w[switch_idx]) && (w[i] > w[pivot]))
                switch_idx = i;
        }

        int tmp = w[switch_idx];
        w[switch_idx] = w[pivot];
        w[pivot] = tmp;

        qsort(&w[suff_begin], length - suff_begin, sizeof(int), compare);

        for (int i = 0; i < length; i++)
            putchar(w[i]);
        printf("\n");
    }
}
