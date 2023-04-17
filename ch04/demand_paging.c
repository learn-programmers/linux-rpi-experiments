#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

#define PAGE_SIZE 4096
#define MEM_SIZE (1ul << 30)     //1GB
#define STEP_SIZE (100ul << 20)  //100MB

int main() {
    char *mem = mmap(NULL, MEM_SIZE, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (mem == MAP_FAILED) {
        perror("mmap failed");
        exit(EXIT_FAILURE);
    }
    size_t step_offset = 0;
    size_t touched_size = 0;

    while (touched_size < MEM_SIZE) {
        memset(mem + step_offset, 0, STEP_SIZE);
        touched_size += STEP_SIZE;

        printf("Touched %lu MB\n", touched_size >> 20);

        if (touched_size < MEM_SIZE) {
            printf("Press enter to continue to next step...");
            getchar();
        }

        step_offset += STEP_SIZE;
    }

    if (munmap(mem, MEM_SIZE) == -1) {
        perror("munmap failed");
        exit(EXIT_FAILURE);
    }
    return 0;
}
