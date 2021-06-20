#include <stdio.h>
#include <stdint.h>

extern "C" {

typedef struct _MyData
{
    int32_t a : 5;
    int32_t b : 11;
    int32_t c : 16;
    int8_t  d;
    int16_t e;
    int16_t f;
} MyData;

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
    printf("print_array: buf = %llx, length = %d\n", buf, length);
    for (size_t i = 0; i < length; i++)
    {
        printf("%d, ", buf[i]);
    }
    printf("\n");
}

void print_struct(char* buf, int length)
{
    printf("#### print_struct: buf = 0x%llx, length = %d\n", buf, length);
    for (size_t i = 0; i < length; i++)
    {
        printf("%d, ", buf[i]);
    }
    printf("\n");

    MyData* data = (MyData*)buf;
    printf("MyData: a = %d, b = %d, c = %d, d = %d, e = %d, f = %d\n", data->a, data->b, data->c, data->d, data->e, data->f);
}

}

