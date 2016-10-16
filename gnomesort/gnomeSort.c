#include <stdio.h>
#include <string.h>

int comparisonFunction(void *data1, void *data2)
{
	return *((char*) data1) >= *((char*) data2);
}

void swapMemory(void *mem1, void *mem2, int numBytes)
{
	char *data1 = mem1, *data2 = mem2;
	for(int i = 0; i < numBytes; i++){
		char t = data1[i];
		data1[i] = data2[i];
		data2[i] = t;
	}
}

void gnomeSort(void *data, int size, int nmemb, int (comp)(void *, void*))
{
	int pos = size;
	while (pos < nmemb*size){
		if (comp(data+pos, data+pos-size)){
			pos += size;
		}else{
			swapMemory(data+pos, data+pos-size, size);
			if (pos > size){
				pos -= size;
			}
		}
	}
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
		gnomeSort(s, sizeof(*s), strlen(s), comparisonFunction);
		fprintf(stdout, "%s\n", s);
	}
	int x[5] = {1, 2, 255, 256, 257};
	gnomeSort(x, sizeof(*x), sizeof(x)/sizeof(*x), comparisonFunction);
	fprintf(stdout, "Sorted by first byte cast to char only: ");
	for(i = 0; i < 5; i++){
		fprintf(stdout, "%d, ", x[i]);
	}
	fprintf(stdout, "\n");
}
