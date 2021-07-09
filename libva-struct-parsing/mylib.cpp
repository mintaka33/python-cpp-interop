#include <stdio.h>
#include <stdint.h>

#include <vector>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

using namespace std;

typedef struct _MyData
{
    int32_t a : 5;
    int32_t b : 11;
    int32_t c : 16;
    int8_t  d;
    int16_t e;
    int16_t f;
} MyData;

void print_struct(py::array_t<uint8_t, py::array::c_style | py::array::forcecast> mydata)
{
    printf("pymylib: ndim = %d, size = %dx%d, data_ptr = %llx\n", mydata.ndim(), mydata.shape()[1], mydata.shape()[0], mydata.data());
    int size = mydata.shape()[0];
    uint8_t* buf = (uint8_t*)mydata.data();

    for (size_t i = 0; i < size; i++)
    {
        printf("%d, ", buf[i]);
    }
    printf("\n");

    MyData* data = (MyData*)buf;
    printf("MyData: a = %d, b = %d, c = %d, d = %d, e = %d, f = %d\n", data->a, data->b, data->c, data->d, data->e, data->f);
}

PYBIND11_MODULE(pymylib, m) {
    m.doc() = "libva python bindings"; 
    m.def("print_struct", &print_struct);
}
