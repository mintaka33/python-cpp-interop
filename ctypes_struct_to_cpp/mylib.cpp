#include <stdio.h>
#include <stdint.h>

extern "C" {

typedef struct _MyData
{
    int32_t a;
    int8_t  b;
    int16_t c;
} MyData;

void print_struct()
{
    MyData data = {};
    printf("a = %d, b = %d, c = %d\n", data.a, data.b, data.c);
}

int* get_array()
{
    int * p = new int[10];
    for (size_t i = 0; i < 10; i++)
    {
        p[i] = i;
    }
    return p;
}

void print_array(int* buf, int length)
{
    printf("print_array: buf = %x, length = %d\n", buf, length);
    for (size_t i = 0; i < length; i++)
    {
        printf("%d, ", buf[i]);
    }
    printf("\n");
}

}

