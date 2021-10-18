
// #include <stdio.h>

typedef enum _MyEnum {
    ZERO = 0,
    ONE = 1,
    TWO = 2,
} MyEnum;

typedef struct _MyStruct
{
    int a;
    char b;
    float c;
    MyEnum d;
    MyEnum e;

} MyStruct;

int main()
{
    MyStruct s = {};
    // printf("done\n");
    return 0;
}