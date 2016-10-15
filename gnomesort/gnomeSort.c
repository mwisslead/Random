#include <stdio.h>
#include <string.h>

void gnomeSort(char *data, int ldata)
{
	int pos = 1;
	while (pos < ldata){
		if (data[pos] >= data[pos-1]){
			pos++;
		}else{
			char t = data[pos];
			data[pos] = data[pos-1];
			data[pos-1] = t;
			if (pos > 1){
				pos--;
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
		fprintf(stdout, "%s : ", argv[i]);
		gnomeSort(argv[i], strlen(argv[i]));
		fprintf(stdout, "%s\n", argv[i]);
	}
}
