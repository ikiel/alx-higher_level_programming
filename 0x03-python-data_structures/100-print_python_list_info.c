#include <Python.h>

/**
 * print_python_list_info - prints basic python list info
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, mem, i = 0;
	PyObject *pyo;

	size = Py_SIZE(p);
	mem = ((PyListObject *) p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", mem);

	while (i < size)
	{
		printf("Element %d: ", i);

		pyo = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(pyo)->tp_name);

		i++;
	}
}
