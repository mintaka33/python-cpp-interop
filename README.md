# python-cpp-interop

### print c/c++ struct layout (note: need to compile *.so with debug options)

```bash
sudo apt install dwarves
pahole ./mylib.so
```

Note: if encounter below error, may need use newer pahole version
```
ie__process_class: tag not supported 0x2f (template_type_parameter)!
die__process_class: tag not supported 0x30 (template_value_parameter)!
Segmentation fault
```

build pahole from source code
```bash
sudo apt update
sudo apt install libdw-dev

git clone https://git.kernel.org/pub/scm/devel/pahole/pahole.git
git checkout v1.22

cd pahole
mkdir build
cd build
cmake ..
make -j8
```

### reference link

https://docs.python.org/3/library/ctypes.html

https://numpy.org/doc/stable/reference/routines.ctypeslib.html
