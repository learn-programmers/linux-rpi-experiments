#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
#define MAX_NUM 1000000000

void *summing(void *arg) {
    int start = 0;
    int end = start + MAX_NUM/NUM_THREADS;
    int sum = 0;

    for (int i = start; i < end; i++) {
	   sum += 1;
    }
    printf("sum %d\n",sum);
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];
    int thread_args[NUM_THREADS];
    int i;

    for (i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, summing, &thread_args[i]);
    }

    for (i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
