# python-cpp-interop

### print c/c++ struct layout (note: need to compile *.so with debug options)

```bash
sudo apt install dwarves
pahole ./mylib.so
```
### reference link

https://docs.python.org/3/library/ctypes.html

https://numpy.org/doc/stable/reference/routines.ctypeslib.html