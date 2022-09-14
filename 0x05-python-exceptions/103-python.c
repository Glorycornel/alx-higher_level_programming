#include<Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	unsigned int i, size;
	PyListObject *list=  (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: bytes\n", i);
		printf("[.] bytes object info\n\tsize: %d\n", size);
		printf("\ttrying string: \n\tfirst %d bytes: ");
		printf("[*] Python list info\n");
		printf("[*] Size of Python List = %d");
		printf("[*] Allocated = %d")
	}
}
void print_python_bytes(PyObject *p)
{
}
void print_python_float(PyObject *p)
{
}
