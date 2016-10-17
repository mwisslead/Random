#include <stdio.h>
#include <string.h>

#include "gnomeSort.h"

int compChar(void *data1, void *data2)
{
	return *((char*) data1) >= *((char*) data2);
}

void swapChar(void *mem1, void *mem2)
{
	char *data1 = mem1, *data2 = mem2;
	*data1 ^= *data2;
	*data2 ^= *data1;
	*data1 ^= *data2;
}

int main(int argc, char *argv[])
{
	int i;
	if (argc < 2){
		fprintf(stderr, "Enter some strings\n");
		return -1;
	}
	for(i = 1; i < argc; i++){
		char *s = argv[i];
		fprintf(stdout, "%s : ", s);
		gnomeSort(s, sizeof(*s), strlen(s), compChar, swapChar);
		fprintf(stdout, "%s\n", s);
	}
	int x[5] = {255, 2, 257, 256, 1};
	for(i = 0; i < 5; i++){
		fprintf(stdout, "%d, ", x[i]);
	}
	fprintf(stdout, "\n");
	int compInt(void *data1, void *data2)
	{
		return *((int*) data1) >= *((int*) data2);
	}
	void swapInt(void *mem1, void *mem2)
	{
		int *data1 = mem1, *data2 = mem2;
		*data1 ^= *data2;
		*data2 ^= *data1;
		*data1 ^= *data2;
	}
	gnomeSort(x, sizeof(*x), sizeof(x)/sizeof(*x), compInt, swapInt);
	for(i = 0; i < 5; i++){
		fprintf(stdout, "%d, ", x[i]);
	}
	fprintf(stdout, "\n");
}
